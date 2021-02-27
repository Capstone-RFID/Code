from sllurp import llrp
from twisted.internet import reactor
import pyodbc

from pytz import timezone
import pytz
import datetime

from threading import Thread
import subprocess
import keyboard
import logging
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import pandas as pd
import sys
from Etek_main_window_v2 import Ui_MainWindow
from AdminInterface import Admin_Interface
import time

from password_prompt import Ui_Dialog
from alreadyCheckedOut import checkMsg
from configparser import ConfigParser
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread
Event_Log_Entry = []
reading = "off"


@pyqtSlot(list)
def update_RFID(result):
    if Employee_ID_Check(window.ui.Employee_ID_Input.text()):
        for tag in result:
            rfid_check_query = '''SELECT TOP 1 * FROM [RFID Table] WHERE TagID = (?);'''  # '?' is a placeholder
            cursor.execute(rfid_check_query, str(tag))
            if cursor.fetchone():
                get_asset_query = '''SELECT AssetID FROM [RFID Table] WHERE TagID = (?);'''  # '?' is a placeholder
                cursor.execute(get_asset_query, str(tag))
                assetID = cursor.fetchone()
                global reading
                reading = "off"
                window.rfid_insert(assetID[0])
                reading = "on"

class WorkerThread(QThread):
    signal_update = pyqtSignal(list)
    def __init__(self):
        QThread.__init__(self)
        # self.signals = Communicate()
        self.signal_update.connect(update_RFID)

    def cb(self, tagReport):
        global readFlag
        if reading == "on":
            tags = tagReport.msgdict['RO_ACCESS_REPORT']['TagReportData']
            # global result
            result = [sub['EPC-96'] for sub in tags]
            print(result)
            if len(tags) != 0:
                # taglist.append(tags[0]['EPC-96'])
                # if tags[0]['EPC-96'] not in taglist:
                # RFID(tags[0]['EPC-96'])
                # RFID(result)
                self.signal_update.emit(result)
            result.clear()  ####very important
        else:
            return


def snapshot():
    subprocess.run(
        ["C:\\Program Files\\Microsoft SQL Server\\150\\COM\\snapshot.exe",
         "-Publisher", "[BALKARAN09]", "-PublisherDB", "[TEST]",
         "-Distributor", "[BALKARAN09]", "-Publication", "[please_merge]",
         "-ReplicationType", "2", "-DistributorSecurityMode", "1"],
        # probably add this
        check=True)


def Employee_ID_Check(input):
    check_query = '''SELECT TOP 1 * FROM [Employee Table] WHERE EmployeeID = (?);'''  # '?' is a placeholder
    cursor.execute(check_query, str(input))
    if cursor.fetchone():
        return True
    else:
        return False

def Asset_Check(input):
    check_query = '''SELECT TOP 1 * FROM [Asset Table] WHERE AssetID = (?);'''  # '?' is a placeholder
    cursor.execute(check_query, str(input))
    if cursor.fetchone():
        return True
    else:
        return False

def Permission_Check(employee):
    check_query = '''SELECT EMPLOYEEID FROM [Employee Access Table] WHERE (PERMISSION = '2' OR PERMISSION = '3') AND EMPLOYEEID = (?);'''  # '?' is a placeholder
    cursor.execute(check_query, str(employee))
    if cursor.fetchone():
        return True
    else:
        return False

def getEmployeeName(employeeID):
    get_query = '''SELECT NAME FROM [Employee Table] WHERE EMPLOYEEID = (?);'''  # '?' is a placeholder
    cursor.execute(get_query, str(employeeID))
    name = cursor.fetchone()
    return name[0]

class alreadyChecked(QDialog):
    def __init__(self, parent=None):
        super(alreadyChecked, self).__init__(parent)
        self.setWindowModality(True)
        self.setModal(False)
        self.ui = checkMsg()
        self.ui.setupUi(self)
        self.ui.select_reject.accepted.connect(self.returnTrue)
        self.ui.select_reject.rejected.connect(self.returnFalse)
        self.ui.ConfirmMessage.setText("")

    def returnTrue(self):
        self.accept()

    def open(self):
        self.show()

    def returnFalse(self):
        self.reject()


class passwordWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(passwordWindow, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.handleLogin)
        self.ui.lineEdit.setEchoMode(QLineEdit.Password)

    def handleLogin(self):
        if self.ui.lineEdit.text() == 'foo':
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Bad password')
            self.rejected()


class mainWindow(QWidget):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global server, database
        self.admin = Admin_Interface()
        self.check = alreadyChecked()
        self.show()
        self.eventEntry = []
        self.RemovedItems = []
        self.markedList = []
        self.alreadyCh = []

        # connect button to functions
        self.ui.Done_Button.released.connect(self.done_button_clicked)  # button connected
        self.ui.Employee_ID_Enter.released.connect(self.Employee_enter)
        self.ui.Employee_ID_Enter.setFocusPolicy(Qt.ClickFocus)
        self.ui.Asset_ID_Enter.released.connect(self.asset_enter_action)
        self.ui.Asset_ID_Enter.setFocusPolicy(Qt.ClickFocus)
        self.ui.Cancel_Button.released.connect(self.cancel_button_clicked)  # button connected
        self.ui.Asset_ID_Input.returnPressed.connect(self.asset_enter_action)
        self.ui.Employee_ID_Input.returnPressed.connect(self.Employee_enter)
        self.ui.Remove_Button.released.connect(self.remove_action)
        self.ui.New_Item_List.setAlternatingRowColors(True)
        self.ui.Existing_Item_list.setAlternatingRowColors(True)
        self.ui.Employee_ID_Input.setFocus()
        self.ui.Mark_Button.released.connect(self.mark_assets)
        self.ui.Mark_Button.setEnabled(False)
        self.ui.Asset_ID_Input.setEnabled(False)
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.timer_timeout)
        self.ui.Admin_Button.setEnabled(False)
        self.ui.Remove_Button.setEnabled(False)
        # validator to only enter integer values into the entry fields
        self.onlyInt = QtGui.QIntValidator()
        self.ui.Asset_ID_Input.setValidator(self.onlyInt)
        self.ui.Employee_ID_Input.setValidator(self.onlyInt)
        self.qm = QtWidgets.QMessageBox()

    def alreadyCheckedOut(self, assetID):
        status_check_query = '''SELECT TOP(1)
                                [Event Log Table].EMPLOYEEID,[Event Log Table].Status
                                FROM
                                [Event Log Table]
                                WHERE
                                [Event Log Table].AssetID = (?)
                                ORDER BY [Event Log Table].Entry DESC'''
        cursor.execute(status_check_query, assetID)
        state = cursor.fetchone()
        flag = ""
        if state == None:
            flag = "gtg"
        elif state[1] == "1":
            flag = "gtg"
        elif state[1] == "2":

            if state[0] != self.ui.Employee_ID_Input.text():
                #add name to this dialog box

                response =  self.qm.question(self,'Input Required', "Asset " +assetID+" is currently assigned to Employee " + state[0] + "\n\nDo you still wish to proceed?", self.qm.Yes | self.qm.No)
                if response == self.qm.Yes:
                    flag = "gtg"
                else:
                    self.RemovedItems.append(assetID)
                    flag ="discard"
            else:
                self.qm.warning(self, 'Notice',"You already have asset "+ assetID+" assigned to you")
                self.RemovedItems.append(assetID)
                flag = "discard"

        elif state[1] == "5":
            flag = "broken"

        return flag

    def adminButtonClicked(self):
        print('clicked admin')
        self.admin.openAdmin(server, database)

    def remove_action(self):
        if len(self.ui.New_Item_List.selectedItems()) != 0:
            # if len(self.eventEntry) != 0: ###this is incorrect
            row = self.ui.New_Item_List.currentRow()
            text = self.ui.New_Item_List.item(row, 0).text()
            if text not in self.RemovedItems:
                self.RemovedItems.append(text)
            y = [x for x in self.eventEntry if text in x]
            if len(y) != 0:
                z = self.eventEntry.index(y[0])
                del self.eventEntry[z]
            self.ui.New_Item_List.removeRow(row)
        else:
            return

    def Employee_enter(self):
        if Permission_Check(self.ui.Employee_ID_Input.text()):
            self.ui.Admin_Button.setEnabled(True)
            self.ui.Admin_Button.clicked.connect(self.adminButtonClicked)
        if Employee_ID_Check(self.ui.Employee_ID_Input.text()):
            self.current_items(self.ui.Employee_ID_Input.text())
            self.ui.Asset_ID_Input.setEnabled(True)
            self.ui.Asset_ID_Input.setFocus()
            self.ui.Employee_ID_Input.setReadOnly(True)
            employeeName = getEmployeeName(self.ui.Employee_ID_Input.text())
            self.ui.Name_Label.setText(str(employeeName))
        else:
            self.qm.information(self,'Input Required', "Enter a valid Employee ID before continuing")
            self.ui.Employee_ID_Input.clear()
            return

    def mark_assets(self):
        if len(self.ui.New_Item_List.selectedItems()) != 0:
            row = self.ui.New_Item_List.currentRow()
            text = self.ui.New_Item_List.item(row, 0).text()
            if text not in self.markedList:
                self.markedList.append(text)
            y = [x for x in self.eventEntry if text in x]
            z = self.eventEntry.index(y[0])
            del self.eventEntry[z]
            self.ui.New_Item_List.item(row, 0).setBackground(QtGui.QColor(125, 125, 125))
            self.ui.New_Item_List.clearSelection()
        else:
            return

    def clear_lists(self):
        self.ui.New_Item_List.setRowCount(0)
        self.ui.Existing_Item_list.setRowCount(0)
        self.eventEntry.clear()
        self.ui.Employee_ID_Input.setReadOnly(False)
        self.ui.Employee_ID_Input.clear()
        self.RemovedItems.clear()
        self.ui.Check_Out_Box.setEnabled(True)
        self.ui.Check_In_Box.setEnabled(True)
        self.ui.Check_In_Box.setAutoExclusive(False)
        self.ui.Check_Out_Box.setAutoExclusive(False)
        self.ui.Check_Out_Box.setChecked(False)
        self.ui.Check_In_Box.setChecked(False)
        self.ui.Check_In_Box.setAutoExclusive(True)
        self.ui.Check_Out_Box.setAutoExclusive(True)
        self.ui.Mark_Button.setEnabled(False)
        self.ui.Admin_Button.setEnabled(False)
        self.markedList.clear()

        self.ui.Name_Label.clear()
        self.alreadyCh.clear()
        self.ui.Remove_Button.setEnabled(False)
        return

    def done_button_clicked(self):
        if self.ui.Check_In_Box.isChecked():
            print('Check IN action')
            self.check_in_action()
        elif self.ui.Check_Out_Box.isChecked():
            print('Check OUT action')
            self.check_out_action()
        else:
            self.confirmation_msg([])
        self.clear_lists()

    def cancel_button_clicked(self):
        self.ui.Employee_ID_Input.setReadOnly(False)
        self.ui.Employee_ID_Input.clear()
        self.ui.Asset_ID_Input.clear()
        self.ui.Asset_ID_Input.setEnabled(False)
        self.clear_lists()

    def timer_timeout(self):
        print("timer running")
        self.ui.Asset_ID_Input.clear()

    def insert_into_table(self, mode, item):
        self.ui.Remove_Button.setEnabled(True)
        if mode == 1:
            lastrow_new = self.ui.New_Item_List.rowCount()
            self.ui.New_Item_List.insertRow(lastrow_new)
            self.ui.New_Item_List.setItem(lastrow_new, 0, QTableWidgetItem(item))
            if self.ui.Check_In_Box.isChecked():
                self.ui.Mark_Button.setEnabled(True)
        elif mode == 2:
            lastrow_existing = self.ui.Existing_Item_list.rowCount()
            self.ui.Existing_Item_list.insertRow(lastrow_existing)
            self.ui.Existing_Item_list.setItem(lastrow_existing, 0, QTableWidgetItem(item))

    def asset_enter_action(self):
        Asset = self.ui.Asset_ID_Input.text()
        if self.ui.Check_In_Box.isChecked() or self.ui.Check_Out_Box.isChecked():
            if Asset_Check(Asset):
                self.ui.Check_Out_Box.setEnabled(False)
                self.ui.Check_In_Box.setEnabled(False)
                flag = self.alreadyCheckedOut(Asset)
                if flag == "gtg":
                    if not any(Asset in sublist for sublist in self.eventEntry):  # any(Asset in sublist for sublist in self.ItemEntry) == False:
                        self.insert_into_table(1, Asset)
                        # apend the entries into a list
                        self.eventEntry.append([self.ui.Employee_ID_Input.text(), Asset])
                        # self.StateEntry.append(self.ui.Employee_ID_Input.text())
                        # self.ui.New_Item_List.insertRow()
                        self.ui.Asset_ID_Input.clear()
                ##decided to not check out an already checked out item
                elif flag == "discard":
                    self.ui.Asset_ID_Input.clear()
                ##broken or something
                elif flag == "broken":
                    self.qm.critical(self, 'Critical Issue',"Asset " +Asset + " is broken. Do NOT use.")
                    self.ui.Asset_ID_Input.clear()
            else:
                self.qm.warning(self, 'Check Asset', "Asset "  +Asset +  " is not configured for use or does not exist \n\n Please Check your Asset ID and try again or Enter a valid Asset ID")
                self.ui.Asset_ID_Input.clear()
        else:
            self.qm.information(self, 'Input Required', "Please select an action to perform (Check-In or Check-Out")
        return

    def rfid_insert(self, asset):

        if self.ui.Asset_ID_Input.isEnabled() and (not any(asset in sublist for sublist in self.eventEntry)) and (
                asset not in self.RemovedItems) and (self.ui.Check_Out_Box.isChecked() or self.ui.Check_In_Box.isChecked()):
            flag = self.alreadyCheckedOut(asset)
            if flag == "gtg":
                self.eventEntry.append([self.ui.Employee_ID_Input.text(), asset])
                self.insert_into_table(1, asset)
            elif flag == "broken":
                self.qm.critical(self, 'Critical Issue',"Asset " +asset + " is broken. Do NOT use.")
                self.ui.Asset_ID_Input.clear()
        elif not (self.ui.Check_Out_Box.isChecked() or self.ui.Check_In_Box.isChecked()):
            self.qm.information(self, 'Input Required',"Please select an action to perform (Check-In or Check-Out")

    def check_in_action(self):
        timestamp = datetime.datetime.now(tz=pytz.utc)
        timestamp = timestamp.astimezone(timezone('US/Pacific'))
        self.sql_call("1", timestamp)


    def check_out_action(self):
        timestamp = datetime.datetime.now(tz=pytz.utc)
        timestamp = timestamp.astimezone(timezone('US/Pacific'))
        self.sql_call("2", timestamp)


    def confirmation_msg(self, entries):
        preString = ''
        brkSring = "You have broken"
        message = QtWidgets.QMessageBox()
        if self.ui.Check_In_Box.isChecked():
            preString = "You Have Checked-In"
        elif self.ui.Check_Out_Box.isChecked():
            preString = "You Have Checked-Out"
        # initialize an empty string seperator
        str1 = "\n"

        if len(self.markedList) != 0:
            message.setText(preString + " " + str(len(entries)) + " Items: \n" + str1.join(entries) + "\n" + brkSring
                            + " " + str(len(self.markedList)) + " Items: " + "\n" + str1.join(self.markedList))
        else:
            message.setText(preString + " " + str(len(entries)) + " Items: \n" + str1.join(entries))

        message.setWindowTitle("Confirmation")
        message.exec_()
        return

    def sql_call(self, status, timestamp):
        confirmation_list = []

        if len(self.markedList) != 0:
            for item in self.markedList:
                Event_Log_Entry.append(
                    [timestamp.strftime('%Y-%m-%d %H:%M:%S'), self.ui.Employee_ID_Input.text(), item, '5'])
        for item in self.eventEntry:
            Event_Log_Entry.append([timestamp.strftime('%Y-%m-%d %H:%M:%S'), item[0], item[1], status])

        insert_event_query = ''' INSERT INTO [Event Log Table] (TIMESTAMP,EMPLOYEEID,ASSETID, STATUS) VALUES(?,?,?,?);'''
        for entry in Event_Log_Entry:
            # define the values to insert
            eventValues = (entry[0], entry[1], entry[2], entry[3])
            confirmation_list.append(entry[2])
            # insert the data into the database
            cursor.execute(insert_event_query, eventValues)
        # commit the inserts

        cnxn.commit()
        self.confirmation_msg(confirmation_list)
        Event_Log_Entry.clear()

        # cursor.close
        # cnxn.close
        return

    def current_items(self, emID):
        current_asset_query = '''
                            SELECT AssetID
                            FROM
                            (
                            SELECT *
                            FROM
                            (
                            SELECT TOP(999999999999)
                            [Event Log Table].Entry,[Event Log Table].AssetID,[Event Log Table].Status
                            FROM
                            [Event Log Table]
                            WHERE
                            [Event Log Table].EmployeeID = (?)
                            ORDER BY [Event Log Table].Entry DESC
                            )AS subquery
                            WHERE
                            Entry in (Select max(Entry) FROM  (
                            SELECT TOP(999999999999)
                            [Event Log Table].Entry,[Event Log Table].AssetID,[Event Log Table].Status
                            FROM
                            [Event Log Table]
                            WHERE
                            [Event Log Table].EmployeeID = (?)
                            ORDER BY [Event Log Table].Entry DESC
                            )AS subquery group by AssetID)
                            )AS final_result
                            WHERE
                            Status = '2'; '''
        status_check_query = '''SELECT TOP(1)
                                [Event Log Table].EMPLOYEEID
                                FROM
                                [Event Log Table]
                                WHERE
                                [Event Log Table].AssetID = (?)
                                ORDER BY [Event Log Table].Entry DESC'''

        cursor.execute(current_asset_query, str(emID), str(emID))
        for assets in cursor.fetchall():
            print(assets[0])
            cursor.execute(status_check_query, assets[0])
            state = cursor.fetchone()
            print (state)
            if state[0] == self.ui.Employee_ID_Input.text():
                self.insert_into_table(2, assets[0])
        return



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = passwordWindow()
    # RFID init
    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = mainWindow()
        work = WorkerThread()
        window.show()
        logging.getLogger().setLevel(logging.INFO)
        factory = llrp.LLRPClientFactory(antennas=[1], start_inventory=True, session=0, duration=0.8)
        factory.addTagReportCallback(work.cb)
        reactor.connectTCP('169.254.10.1', llrp.LLRP_PORT, factory)

        # define the server name and the database name
        config = ConfigParser()
        config.read('config.ini')
        global server, database
        server = config.get('database_info', 'server')
        database = config.get('database_info','database')
        print(server)
        print(database)

        # define a connection string
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                                SERVER=' + server + ';\
                                  DATABASE=' + database + ';\
                                Trusted_Connection=yes;')

        # create the connection cursor
        cursor = cnxn.cursor()
        reading = "on"
        r = Thread(target=reactor.run, args=(False,))
        r.daemon = True
        r.start()

        Thread(target=sys.exit(app.exec()), args=(False,)).start()
        # sys.exit(app.exec())
