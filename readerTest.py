from sllurp import llrp
from twisted.internet import reactor
import pyodbc

from threading import Thread
import subprocess

import logging
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys
from Etek_main_window_v2 import Ui_MainWindow
from AdminInterface import Admin_Interface, ETEK_log

import re

from password_prompt import Ui_Dialog
from configparser import ConfigParser
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread
import hashlib

Event_Log_Entry = []
reading = "on"


# ************Using PyQt5 signals and slots to read and process RFID data********
@pyqtSlot(list)
##If valid employee use SQL querries to find out the Asset iD from RFID ID and call rfid_insert function with Asset ID
def update_RFID(result):

    if Employee_ID_Check(window.ui.Employee_ID_Input.text()):
        for tag in result:
            rfid_check_query = '''SELECT TOP 1 * FROM [RFID Table] WHERE TagID = (?);'''  # '?' is a placeholder
            cursor.execute(rfid_check_query, str(tag))
            if cursor.fetchone():
                get_asset_query = '''SELECT AssetID FROM [RFID Table] WHERE TagID = (?);'''  # '?' is a placeholder
                cursor.execute(get_asset_query, str(tag))
                assetID = cursor.fetchone()
                if window.admin.isVisible() and len(tag) != 0:
                    window.admin.RFIDINSERT(str(tag))
                else:
                    window.rfid_insert(assetID[0])






class WorkerThread(QThread):
    signal_update = pyqtSignal(list)

    def __init__(self):
        QThread.__init__(self)
        # self.signals = Communicate()
        self.signal_update.connect(update_RFID)

    ##reads RFID tags
    def cb(self, tagReport):
        global readFlag
        if reading == "on":
            tags = tagReport.msgdict['RO_ACCESS_REPORT']['TagReportData']
            # global result
            result = [sub['EPC-96'] for sub in tags]
            print(result)
            if len(tags) != 0:
                self.signal_update.emit(result)
            result.clear()
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


##Checks whether the employee exists in the database
def Employee_ID_Check(input):
    check_query = '''SELECT TOP 1 * FROM [Employee Table] WHERE EmployeeID = (?);'''  # '?' is a placeholder
    cursor.execute(check_query, str(input))
    if cursor.fetchone():
        return True
    else:
        return False


# Checks whether the asset exists in the database
def Asset_Check(input):
    check_query = '''SELECT TOP 1 * FROM [Asset Table] WHERE AssetID = (?);'''  # '?' is a placeholder
    cursor.execute(check_query, str(input))
    if cursor.fetchone():
        return True
    else:
        return False


# Check whether the employee has the admin interface access
def Permission_Check(employee):
    check_query = '''SELECT EMPLOYEEID FROM [Employee Access Table] WHERE (PERMISSION = '2' OR PERMISSION = '3') AND EMPLOYEEID = (?);'''  # '?' is a placeholder
    cursor.execute(check_query, str(employee))
    if cursor.fetchone():
        return True
    else:
        return False


# Returns the name of the employee from the database based on the employee ID
def getEmployeeName(employeeID):
    get_query = '''SELECT NAME FROM [Employee Table] WHERE EMPLOYEEID = (?);'''  # '?' is a placeholder
    cursor.execute(get_query, str(employeeID))
    name = cursor.fetchone()
    return name[0]


# PasswordWindow creates a password window where a generic password is entered to launch the application
class passwordWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(passwordWindow, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.ok.released.connect(self.handleLogin)
        self.ui.lineEdit.setEchoMode(QLineEdit.Password)

    # setup the password and and the conditions of correct and wrong password in this method
    def handleLogin(self):
        password = self.ui.lineEdit.text().encode('utf-8')
        hashpass = hashlib.sha256(password).hexdigest()
        config = ConfigParser()
        config.read('config.ini')
        storedPass= config.get('password', 'pass')
        if hashpass == storedPass:  # password
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Bad password')
            ETEK_log.info('Incorrect password entered. Application not run.')
            self.rejected()



# ****************************Main program window *********************#
class mainWindow(QWidget):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # define the server name and the database name
        config = ConfigParser()
        config.read('config.ini')
        #server, database
        self.server = config.get('database_info', 'server')
        self.database = config.get('database_info', 'database')

        self.admin = Admin_Interface()
        self.show()
        self.eventEntry = []
        self.RemovedItems = []
        self.markedList = []
        self.alreadyCh = []
        self.qm = QtWidgets.QMessageBox()

        self.error_count = 0
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
        self.ui.move_Button.released.connect(self.move_action)
        self.ui.New_Item_List.setAlternatingRowColors(True)
        self.ui.Existing_Item_list.setAlternatingRowColors(True)
        self.ui.Employee_ID_Input.setFocus()
        self.ui.Mark_Button.released.connect(self.mark_assets)
        self.ui.Mark_Button.setEnabled(False)
        self.ui.Help_Button.released.connect(self.help_button)
        self.ui.Asset_ID_Input.setEnabled(False)
        # self.timer = QtCore.QTimer()
        # self.timer.setSingleShot(True)
        # self.timer.timeout.connect(self.timer_timeout)
        self.ui.Admin_Button.setEnabled(False)
        self.ui.Remove_Button.setEnabled(False)
        # validator to only enter integer values into the entry fields
        self.onlyInt = QtGui.QIntValidator()
        regExp = config.get('assetID', 'regex')
        rExp = QRegExp(regExp)
        valid = QtGui.QRegExpValidator(rExp, self.ui.Asset_ID_Input)
        self.ui.Asset_ID_Input.setValidator(valid)
        self.ui.Employee_ID_Input.setValidator(self.onlyInt)

        ### disable editing of tables
        self.ui.New_Item_List.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.Existing_Item_list.setEditTriggers(QAbstractItemView.NoEditTriggers)

    # Help button text to be displayed:
    def help_button(self):
        try:
            self.qm.setFixedSize(3000, 5000)
            self.qm.information(self, 'Help',
                                '''Welcome to E-TEK! \n\nTo use the application:\n1. Enter Employee ID\n2. Select the action to perform\n3. Confirm items in table\n   (3a) Press 'Mark Broken' to mark item as broken\n   (3b) Press 'Remove Item' to remove item from table\n4. Press 'Done' to complete transaction\n   (4a) Press 'Cancel' to clear the form''')
            ETEK_log.info('Help Button pressed.')
        except:
            self.qm.critical(self,'Unexpected error: Exception thrown','An unexpected error has occured, please try again or contact tech support for help')
            ETEK_log.error('Error occurred in function: help_button')

    def alreadyCheckedOut(self, assetID):
        status_check_query = '''SELECT TOP(1)
                                [Event Log Table].EMPLOYEEID,[Event Log Table].Status
                                FROM
                                [Event Log Table]
                                WHERE
                                [Event Log Table].AssetID = (?)
                                ORDER BY [Event Log Table].TimeStamp DESC'''
        cursor.execute(status_check_query, assetID)
        state = cursor.fetchone()
        flag = ""
        if state == None:
            flag = "gtg"
        elif state[1] == "1":
            flag = "gtg"
        elif state[1] == "2":  ##if asset checked out
            if state[0] != self.ui.Employee_ID_Input.text():  ## if asset assigned to employee is not  the current employee
                # add name to this dialog box
                response = self.qm.question(self, 'Input Required',
                                            "Asset " + assetID + " is currently assigned to Employee " + state[
                                                0] + "\n\nDo you still wish to proceed?", self.qm.Yes | self.qm.No)
                if response == self.qm.Yes:
                    flag = "gtg"
                else:
                    self.RemovedItems.append(assetID)
                    flag = "discard"
            elif self.ui.Check_In_Box.isChecked() and state[0] == self.ui.Employee_ID_Input.text():
                flag = "gtg"
            elif self.ui.Check_Out_Box.isChecked() and state[0] == self.ui.Employee_ID_Input.text():
                self.qm.warning(self, 'Notice', "You already have asset " + assetID + " assigned to you")
                self.RemovedItems.append(assetID)
                flag = "discard"

        elif state[1] == "5" and self.ui.Check_In_Box.isChecked():
            flag = "brokenCheckIn"
        elif state[1] == "5" and self.ui.Check_Out_Box.isChecked():
            flag = "broken"
        elif state[1] == "3" and self.ui.Check_Out_Box.isChecked():
            flag = "InRepair"
        elif state[1] == "3" and self.ui.Check_In_Box.isChecked():
            flag = "RepairCheckIn"
        elif state[1] == "4" and self.ui.Check_Out_Box.isChecked():
            flag = "Retired"
        elif state[1] == "4" and self.ui.Check_In_Box.isChecked():
            flag = "RetiredCheckIn"
        return flag

    def adminButtonClicked(self):
        try:
            print('clicked admin')
            self.admin.openAdmin(server, database,self.ui.Employee_ID_Input.text())
            ETEK_log.info('Clicked admin window button')
        except:
            self.qm.critical(self, 'Unexpected error: Exception thrown',
                             'An unexpected error has occured, please try again or contact tech support for help')
            ETEK_log.error('Error occurred in function: adminButtonClicked')


    ##move asset from one table to another
    def move_action(self):
        try:
            if self.ui.Check_In_Box.isChecked():
                if len(self.ui.Existing_Item_list.selectedItems()) != 0:
                    while len(self.ui.Existing_Item_list.selectedItems()) > 0:
                        targetRow = self.ui.New_Item_List.rowCount()
                        self.ui.New_Item_List.insertRow(targetRow)
                        for column in range(self.ui.Existing_Item_list.columnCount()):
                            row = self.ui.Existing_Item_list.currentRow()
                            item = self.ui.Existing_Item_list.takeItem(row, column)
                            self.eventEntry.append([self.ui.Employee_ID_Input.text(), item.text()])
                            if item:
                                self.ui.New_Item_List.setItem(targetRow, column, item)
                            self.ui.Existing_Item_list.removeRow(row)
                    self.ui.Mark_Button.setEnabled(True)
                    ETEK_log.info('Move items arrow pressed.')
                else:
                    self.qm.information(self, 'Selection Required', "Please select an asset to move first")
                    return
            else:
                self.qm.information(self, 'Selection Required', "This button only works when Check-In action selected")
        except:
            self.qm.critical(self, 'Unexpected error: Exception thrown',
                             'An unexpected error has occured, please try again or contact tech support for help')
            ETEK_log.error('Error occurred in function: move_action')



    def remove_action(self):
        try:
            if len(self.ui.New_Item_List.selectedItems()) != 0:
                # if len(self.eventEntry) != 0: ###this is incorrect
                row = self.ui.New_Item_List.currentRow()
                text = self.ui.New_Item_List.item(row, 0).text()
                if text not in self.RemovedItems:
                    self.RemovedItems.append(text)
                y = [x for x in self.eventEntry if text in x]
                k = [x for x in self.markedList if text in x]
                if len(y) != 0:
                    z = self.eventEntry.index(y[0])
                    del self.eventEntry[z]
                if len(k) != 0:
                    p = self.markedList.index(k[0])
                    del self.markedList[p]

                self.ui.New_Item_List.removeRow(row)
                ETEK_log.info('Remove action pressed.')
            else:
                self.qm.information(self, 'Selection Required', "Please select an asset to remove first")
                return
        except:
            self.qm.critical(self, 'Unexpected error: Exception thrown',
                             'An unexpected error has occured, please try again or contact tech support for help')
            ETEK_log.error('Error occurred in function: remove_action')

    def Employee_enter(self):
        try:
            self.ui.Employee_ID_Enter.setEnabled(False)
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
                self.ui.Employee_ID_Enter.setStyleSheet("color : rgba(0, 0, 0, 50%)")
                ETEK_log.info('User:(' + self.ui.Employee_ID_Input.text() + ') Logged in successfully.')
            else:
                self.qm.information(self, 'Input Required', "Enter a valid Employee ID before continuing")
                self.ui.Employee_ID_Input.clear()
                return
        except:
            self.qm.critical(self, 'Unexpected error: Exception thrown',
                             'An unexpected error has occured, please try again or contact tech support for help')
            ETEK_log.error('Error occurred in function: Employee_enter')

    def mark_assets(self):
        try:
            if len(self.ui.New_Item_List.selectedItems()) != 0:
                row = self.ui.New_Item_List.currentRow()
                text = self.ui.New_Item_List.item(row, 0).text()
                if text not in self.markedList:
                    self.markedList.append(text)
                y = [x for x in self.eventEntry if text in x]
                z = self.eventEntry.index(y[0])
                del self.eventEntry[z]
                self.ui.New_Item_List.item(row, 0).setBackground(QtGui.QColor(255, 0, 0))
                self.ui.New_Item_List.clearSelection()
            else:
                self.qm.information(self, 'Selection Required', "Please select an asset to mark as broken first")
                return
        except:
            self.qm.critical(self, 'Unexpected error: Exception thrown',
                             'An unexpected error has occured, please try again or contact tech support for help')
            ETEK_log.error('Error occurred in function: mark_assets')

    def clear_lists(self):
        self.ui.New_Item_List.setRowCount(0)
        self.ui.Existing_Item_list.setRowCount(0)
        self.eventEntry.clear()
        self.ui.Employee_ID_Input.setReadOnly(False)
        self.ui.Employee_ID_Input.clear()
        self.ui.Asset_ID_Input.clear()
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
        self.ui.Employee_ID_Enter.setEnabled(True)
        self.ui.Name_Label.clear()
        self.alreadyCh.clear()
        self.ui.Remove_Button.setEnabled(False)
        self.error_count = 0
        self.ui.Employee_ID_Enter.setStyleSheet("color : rgba(255, 255, 255,255)")
        ETEK_log.info('Clear lists.')

        self.admin.close()
        return

    def done_button_clicked(self):
        try:
            if self.ui.Check_In_Box.isChecked():
                print('Check IN action')
                self.check_in_action()
                ETEK_log.info('Check IN action pressed')
            elif self.ui.Check_Out_Box.isChecked():
                print('Check OUT action')
                self.check_out_action()
                ETEK_log.info('Check OUT action pressed')
            else:
                self.confirmation_msg([])
            self.clear_lists()
        except:
            self.qm.critical(self, 'Unexpected error: Exception thrown',
                             'An unexpected error has occured, please try again or contact tech support for help')
            ETEK_log.error('Error occurred in function: done_button_clicked')


    def cancel_button_clicked(self):
        try:
            self.ui.Employee_ID_Input.setReadOnly(False)
            self.ui.Employee_ID_Input.clear()
            self.ui.Asset_ID_Input.clear()
            self.ui.Asset_ID_Input.setEnabled(False)
            self.clear_lists()
            ETEK_log.info('Cancel Button Clicked.')
        except:
            self.qm.critical(self,'Unexpected error: Exception thrown','An unexpected error has occured, please try again or contact tech support for help')
            ETEK_log.error('Error occurred in function: cancel_button_clicked')

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
        try:
            Asset = self.ui.Asset_ID_Input.text()
            if re.findall(r"\Ae", Asset):
                Asset = str.capitalize(Asset)
            else:
                Asset = Asset
            if [self.ui.Employee_ID_Input.text(), Asset] in self.eventEntry:
                self.qm.information(self, 'Already Selected', "Asset " + Asset + " is already selected ")
            else:
                if self.ui.Check_In_Box.isChecked() or self.ui.Check_Out_Box.isChecked():
                    if Asset_Check(Asset):
                        self.ui.Check_Out_Box.setEnabled(False)
                        self.ui.Check_In_Box.setEnabled(False)
                        flag = self.alreadyCheckedOut(Asset)
                        if flag == "gtg":
                            if not any(Asset in sublist for sublist in self.eventEntry):
                                self.insert_into_table(1, Asset)
                                # append the entries into a list
                                self.eventEntry.append([self.ui.Employee_ID_Input.text(), Asset])
                                # self.StateEntry.append(self.ui.Employee_ID_Input.text())
                                # self.ui.New_Item_List.insertRow()
                                self.ui.Asset_ID_Input.clear()
                        ##decided to not check out an already checked out item
                        elif flag == "discard":
                            self.ui.Asset_ID_Input.clear()
                        ##broken or something
                        elif flag == "broken":
                            self.qm.critical(self, 'Critical Issue', "Asset " + Asset + " is broken. Do NOT use.")
                            self.ui.Asset_ID_Input.clear()
                        elif flag == "brokenCheckIn":
                            if not any(Asset in sublist for sublist in self.eventEntry):
                                self.insert_into_table(1, Asset)
                                # append the entries into a list
                                self.markedList.append(Asset)
                                row = self.ui.New_Item_List.rowCount() - 1
                                self.ui.New_Item_List.item(row, 0).setBackground(QtGui.QColor(255, 0, 0))
                                self.ui.Asset_ID_Input.clear()
                        elif flag == "InRepair":
                            self.qm.critical(self, 'Critical Issue', "Asset " + Asset + " is in Repair. Do NOT use.")
                            self.ui.Asset_ID_Input.clear()
                        elif flag == "RepairCheckIn":
                            self.qm.critical(self, 'Critical Issue', "Please contact the admin, this Asset " + Asset + " is in Repair. Do NOT use.")
                            self.ui.Asset_ID_Input.clear()
                        elif flag == "RetiredCheckIn":
                            self.qm.critical(self, 'Critical Issue', "Please contact the admin, this Asset " + Asset + " is retired from field. Do NOT use.")
                            self.ui.Asset_ID_Input.clear()

                        elif flag == "Retired":
                            self.qm.critical(self, 'Critical Issue', "Asset " + Asset + " is Retired. Do NOT use.")
                            self.ui.Asset_ID_Input.clear()

                    else:
                        self.qm.warning(self, 'Check Asset',
                                        "Asset " + Asset + " is not configured for use or does not exist \n\n Please Check your Asset ID and try again or Enter a valid Asset ID")
                        self.ui.Asset_ID_Input.clear()
                else:
                    self.qm.information(self, 'Input Required', "Please select an action to perform (Check-In or Check-Out")
                return
        except:
            self.qm.critical(self, 'Unexpected error: Exception thrown',
                             'An unexpected error has occured, please try again or contact tech support for help')
            ETEK_log.error('Error occurred in function: asset_enter_action')

    def rfid_insert(self, asset):
        self.error_count += 1
        if self.ui.Asset_ID_Input.isEnabled() and (not any(asset in sublist for sublist in self.eventEntry)) and (
                asset not in self.RemovedItems) and (
                self.ui.Check_Out_Box.isChecked() or self.ui.Check_In_Box.isChecked()):
            flag = self.alreadyCheckedOut(asset)
            if flag == "gtg":
                self.eventEntry.append([self.ui.Employee_ID_Input.text(), asset])
                self.insert_into_table(1, asset)
            elif flag == "broken":
                self.qm.critical(self, 'Critical Issue', "Asset " + asset + " is broken. Do NOT use.")
                self.ui.Asset_ID_Input.clear()
            elif flag == "brokenCheckIn":
                self.insert_into_table(1, asset)
                # append the entries into a list
                self.markedList.append(asset)
                row = self.ui.New_Item_List.rowCount() - 1
                self.ui.New_Item_List.item(row, 0).setBackground(QtGui.QColor(255, 0, 0))
                self.ui.Asset_ID_Input.clear()

        elif not (self.ui.Check_Out_Box.isChecked() or self.ui.Check_In_Box.isChecked()) and self.error_count == 1:
            self.qm.information(self, 'Input Required', "Please select an action to perform (Check-In or Check-Out")

    def check_in_action(self):
        self.sql_call("1")

    def check_out_action(self):
        self.sql_call("2")

    def confirmation_msg(self, entries):
        preString = ''
        brkSring = "You have broken"
        if self.ui.Check_In_Box.isChecked():
            preString = "You Have Checked-In"
        elif self.ui.Check_Out_Box.isChecked():
            preString = "You Have Checked-Out"
        # initialize an empty string seperator
        str1 = "\n"

        if len(self.markedList) != 0:
            self.qm.information(self, 'Confirmation', preString + " " + str(len(entries)) + " Items: \n" +
                                str1.join(entries) + "\n" + brkSring + " " + str(len(self.markedList)) + " Items: " +
                                "\n" + str1.join(self.markedList))
        else:
            self.qm.information(self, 'Confirmation', preString + " " + str(len(entries)) + " Items: \n" +
                                str1.join(entries))
        return

    def sql_call(self, status):
        confirmation_list = []
        if len(self.markedList) != 0:
            for item in self.markedList:
                Event_Log_Entry.append(
                    [self.ui.Employee_ID_Input.text(), item, '5'])
        for item in self.eventEntry:
            Event_Log_Entry.append([item[0], item[1], status])

        insert_event_query = ''' INSERT INTO [Event Log Table] (EMPLOYEEID,ASSETID, STATUS) VALUES(?,?,?);'''
        for entry in Event_Log_Entry:
            # define the values to insert
            eventValues = (entry[0], entry[1], entry[2])
            confirmation_list.append(entry[1])
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
                            [Event Log Table].TimeStamp,[Event Log Table].AssetID,[Event Log Table].Status
                            FROM
                            [Event Log Table]
                            WHERE
                            [Event Log Table].EmployeeID = (?)
                            ORDER BY [Event Log Table].TimeStamp DESC
                            )AS subquery
                            WHERE
                            TimeStamp in (Select max(TimeStamp) FROM  (
                            SELECT TOP(999999999999)
                            [Event Log Table].TimeStamp,[Event Log Table].AssetID,[Event Log Table].Status
                            FROM
                            [Event Log Table]
                            WHERE
                            [Event Log Table].EmployeeID = (?)
                            ORDER BY [Event Log Table].TimeStamp DESC
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
                                ORDER BY [Event Log Table].TimeStamp DESC'''

        cursor.execute(current_asset_query, str(emID), str(emID))
        for assets in cursor.fetchall():
            print(assets[0])
            cursor.execute(status_check_query, assets[0])
            state = cursor.fetchone()
            print(state)
            if state[0] == self.ui.Employee_ID_Input.text():
                self.insert_into_table(2, assets[0])
        return


if __name__ == "__main__":

    # print(hashlib.sha256(b"foo").hexdigest())
    app = QtWidgets.QApplication(sys.argv)
    login = passwordWindow()
    # RFID init
    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = mainWindow()
        work = WorkerThread()
        window.show()
        ETEK_log.info('Application login successful.')
        logging.getLogger().setLevel(logging.INFO)
        factory = llrp.LLRPClientFactory(antennas=[1], start_inventory=True, session=0, duration=0.8)
        factory.addTagReportCallback(work.cb)
        reactor.connectTCP('169.254.10.1', llrp.LLRP_PORT, factory)

        server = window.server
        database = window.database

        # define a connection string
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                                    SERVER=' + server + ';\
                                      DATABASE=' + database + ';\
                                    Trusted_Connection=yes;')
        ETEK_log.info('Connected to Server ' + server + ' and ' + database)

        # create the connection cursor
        cursor = cnxn.cursor()
        reading = "on"
        r = Thread(target=reactor.run, args=(False,))
        r.daemon = True
        r.start()

        Thread(target=sys.exit(app.exec()), args=(False,)).start()
        # sys.exit(app.exec())
