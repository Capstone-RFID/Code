from sllurp import llrp
from twisted.internet import reactor
import pyodbc
from datetime import datetime
from datetime import date
from threading import Thread
import subprocess
import keyboard
import logging
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from Etek_main_window_v2 import Ui_MainWindow
import time
Event_Log_Entry = []

assetID = 0
errorFlag = 0
taglist = []

def cb(tagReport):
    #print("running")
    global readFlag, assetID

    if keyboard.is_pressed('q'):
        reactor.stop()
        mode = 'q'
    tags = tagReport.msgdict['RO_ACCESS_REPORT']['TagReportData']
    result = [sub['EPC-96'] for sub in tags]
    if len(tags) != 0:
        # taglist.append(tags[0]['EPC-96'])
        # if tags[0]['EPC-96'] not in taglist:
            #RFID(tags[0]['EPC-96'])
            RFID(result)
    result.clear()

def RFID(result):
    if Employee_ID_Check(window.ui.Employee_ID_Input.text()):
        for tag in result:
            rfid_check_query = '''SELECT TOP 1 * FROM RFID_Table WHERE TagID = (?);'''  # '?' is a placeholder
            cursor.execute(rfid_check_query, str(tag))
            if cursor.fetchone():
                get_asset_query = '''SELECT AssetID FROM RFID_Table WHERE TagID = (?);'''  # '?' is a placeholder
                cursor.execute(get_asset_query, str(tag))
                assetID = cursor.fetchone()
                window.rfid_insert(assetID[0])



def shutdown(factory):
    return factory.politeShutdown()

def assets_from_RFID_Tag(tag):
    return

##work in progress
# def update():
#     update_query = '''
#                     UPDATE TestDB.dbo.Person
#                     SET Age = 29,City = 'Montreal'
#                     WHERE Name = 'Jon'
#                     '''
#     # loop thru each row in the matrix
#     for row in equipmentID:
#         # define the values to insert
#         values = (row[0], row[1],row[2],row[3])
#         print(values)
#         # insert the data into the database
#         cursor.execute(update_query, values)

def snapshot():
    subprocess.run(
        ["C:\\Program Files\\Microsoft SQL Server\\150\\COM\\snapshot.exe",
         "-Publisher", "[BALKARAN09]", "-PublisherDB", "[TEST]",
         "-Distributor", "[BALKARAN09]", "-Publication", "[please_merge]",
         "-ReplicationType", "2", "-DistributorSecurityMode", "1"],
        # probably add this
        check=True)

def stop():
    reactor.stop()

def Employee_ID_Check(input):
    check_query = '''SELECT TOP 1 * FROM Employee_Table WHERE EmployeeID = (?);'''# '?' is a placeholder
    cursor.execute(check_query, str(input))
    if cursor.fetchone():
        return True
    else:
        return False

def Asset_Check(input):
    check_query = '''SELECT TOP 1 * FROM Asset_Table WHERE AssetID = (?);'''  # '?' is a placeholder
    cursor.execute(check_query, str(input))
    if cursor.fetchone():
        return True
    else:
        return False



class mainWindow(QWidget):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.existingList = []
        self.eventEntry = []
        self.RemovedItems = []
        self.markedList = []

        #connect button to functions
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

        #validator to only enter integer values into the entry fields
        self.onlyInt = QtGui.QIntValidator()
        self.ui.Asset_ID_Input.setValidator(self.onlyInt)
        self.ui.Employee_ID_Input.setValidator(self.onlyInt)

    def remove_action(self):
        if(len(self.eventEntry)!=0):
            row = self.ui.New_Item_List.currentRow()
            text = self.ui.New_Item_List.item(row, 0).text()
            if text not in self.RemovedItems:
                self.RemovedItems.append(text)
            y = [x for x in self.eventEntry if text in x]
            z = self.eventEntry.index(y[0])
            del self.eventEntry[z]
            self.ui.New_Item_List.removeRow(row)


    def Employee_enter(self):
        if Employee_ID_Check(self.ui.Employee_ID_Input.text()):
            self.current_items(self.ui.Employee_ID_Input.text())
            self.ui.Asset_ID_Input.setEnabled(True)
            self.ui.Asset_ID_Input.setFocus()
            self.ui.Employee_ID_Input.setReadOnly(True)
        else:
            self.error_message("Enter a valid Employee ID")
            self.ui.Employee_ID_Input.clear()
            return
    
    def done_button_clicked(self):
        if self.ui.Check_In_Box.isChecked():
            print('Check IN action')
            self.check_in_action()
            self.clear_lists()
        elif self.ui.Check_Out_Box.isChecked():
            print('Check OUT action')
            self.check_out_action()
            self.clear_lists()

    def mark_assets(self):
        row = self.ui.New_Item_List.currentRow()
        text = self.ui.New_Item_List.item(row, 0).text()
        if text not in self.markedList:
            self.markedList.append(text)
        y = [x for x in self.eventEntry if text in x]
        z = self.eventEntry.index(y[0])
        del self.eventEntry[z]
        self.ui.New_Item_List.item(row, 0).setBackground(QtGui.QColor(125,125,125))
        self.ui.New_Item_List.clearSelection()


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
        self.markedList.clear()
        self.existingList.clear()
        return

    def cancel_button_clicked(self):
        self.ui.Employee_ID_Input.setReadOnly(False)
        self.ui.Employee_ID_Input.clear()
        self.ui.Asset_ID_Input.clear()
        self.ui.Asset_ID_Input.setEnabled(False)
        self.clear_lists()

    def error_message(self, text):
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(text)
        error_dialog.setWindowTitle("Error")
        error_dialog.exec_()
        return
    
    def timer_timeout(self):
        print("timer running")
        self.ui.Asset_ID_Input.clear()

    def insert_into_new_table(self, mode, item):
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
            #self.ItemEntry.append(Asset)
            print('Asset Number:' + Asset)
            if self.ui.Check_In_Box.isChecked() or self.ui.Check_Out_Box.isChecked():
                if Asset_Check(Asset):
                    self.ui.Check_Out_Box.setEnabled(False)
                    self.ui.Check_In_Box.setEnabled(False)
                    if not any(Asset in sublist for sublist in self.eventEntry) and self.eliminate_duplicates(Asset): #any(Asset in sublist for sublist in self.ItemEntry) == False:
                        self.insert_into_new_table(1, Asset)
                        #apend the entries into a list
                        self.eventEntry.append([self.ui.Employee_ID_Input.text(),Asset])
                        #self.StateEntry.append(self.ui.Employee_ID_Input.text())
                        #self.ui.New_Item_List.insertRow()
                        self.ui.Asset_ID_Input.clear()

                    else:
                         self.ui.Asset_ID_Input.clear()
                         self.timer.start(1000)
                         self.ui.Asset_ID_Input.setText("DUPLICATE!!!")

                else:
                    self.error_message("Enter a valid Asset ID")
                    self.ui.Asset_ID_Input.clear()
            else:
                self.error_message("Please select Check-In or Check-out action")
            return

    def rfid_insert(self, asset):
        if self.ui.Asset_ID_Input.isEnabled() and (not any(asset in sublist for sublist in self.eventEntry)) and (asset not in self.RemovedItems) and self.eliminate_duplicates(asset) and (self.ui.Check_Out_Box.isChecked() or self.ui.Check_In_Box.isChecked()) :
            self.eventEntry.append([self.ui.Employee_ID_Input.text(),asset])
            self.insert_into_new_table(1, asset)
        # else:
        #     self.ui.Asset_ID_Input.setText('DUPLICATE!!!!')


    def check_in_action(self):
        time = datetime.now()
        datevar = date.today()
        self.sql_call("1", time, datevar)
        self.sql_call("5", time, datevar)


    def eliminate_duplicates(self, asset):
        if asset in self.existingList and self.ui.Check_Out_Box.isChecked():
            return False
        else:
            return True

    def check_out_action(self):
        time = datetime.now()
        datevar = date.today()
        self.sql_call("2", time, datevar)


    def sql_call(self,status, time, datevar):

        if status == '5':
            for item in self.markedList:
                Event_Log_Entry.append([self.ui.Employee_ID_Input.text(), datevar.strftime("%d/%m/%Y") + "," + time.strftime("%H:%M:%S"), item, status])
        else:
            for item in self.eventEntry:
                Event_Log_Entry.append(
                    [item[0], datevar.strftime("%d/%m/%Y") + "," + time.strftime("%H:%M:%S"), item[1], status])
        insert_event_query = ''' INSERT INTO Event_Log_Table (EMPLOYEEID,TIMESTAMP, ASSETID, STATUS) VALUES(?,?,?,?);'''
        for entry in Event_Log_Entry:
            # define the values to insert
            eventValues = (entry[0], entry[1], entry[2],entry[3])
            print(eventValues)
            # insert the data into the database
            cursor.execute(insert_event_query, eventValues)
        # commit the inserts
        cnxn.commit()
        Event_Log_Entry.clear()

        # self.StateEntry.clear()
        # self.ItemEntry.clear()
        # State_Log_Entry.clear()
        # Item_Log_Entry.clear()
        # cursor.close
        # cnxn.close
        return

    def current_items(self,emID):
      current_asset_query =  '''
                            SELECT AssetID
                            FROM
                            (
                            SELECT *
                            FROM
                            (
                            SELECT TOP(999999999999)
                            Event_Log_Table.Entry,Event_Log_Table.AssetID,Event_Log_Table.Status
                            FROM
                            Event_Log_Table
                            WHERE
                            Event_Log_Table.EmployeeID = (?)
                            ORDER BY Event_Log_Table.Entry DESC
                            )AS subquery
                            WHERE
                            Entry in (Select max(Entry) FROM  (
                            SELECT TOP(999999999999)
                            Event_Log_Table.Entry,Event_Log_Table.AssetID,Event_Log_Table.Status
                            FROM
                            Event_Log_Table
                            WHERE
                            Event_Log_Table.EmployeeID = (?)
                            ORDER BY Event_Log_Table.Entry DESC
                            )AS subquery group by AssetID)
                            )AS final_result
                            WHERE
                            Status = '2'; '''
      cursor.execute(current_asset_query,str(emID),str(emID))
      for assets in cursor.fetchall():
          print(assets[0])
          self.existingList.append(assets[0])
          self.insert_into_new_table(2, assets[0])
      return

    def testfunction(self):
        print('hello')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = mainWindow()
    #RFID init

    logging.getLogger().setLevel(logging.INFO)
    factory = llrp.LLRPClientFactory(antennas=[1], start_inventory=True, session=0, duration=0.8)
    factory.addTagReportCallback(cb)
    reactor.connectTCP('169.254.10.1', llrp.LLRP_PORT, factory)

    # define the server name and the database name
    server = "BALKARAN09"
    database = 'TEST'

    # define the server name and the database name
    # server = "Raymond-P1"
    # database = 'RCMP_RFID'

    # define a connection string
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                            SERVER=' + server + ';\
                              DATABASE=' + database + ';\
                            Trusted_Connection=yes;')

    # create the connection cursor
    cursor = cnxn.cursor()
    #it works now
    # if readFlag == True:
    #sys.exit(app.exec_())
    Thread(target=reactor.run, args=(False,)).start()
    Thread(target=sys.exit(app.exec_()), args=(False,)).start()