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
State_Log_Entry = []
Item_Log_Entry = []
assetID = 0
errorFlag = 0
taglist = []

def cb(tagReport):
    # print("running")
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


        # else:
        #     window.error_message("haha")

        # if Employee_ID_Check(window.ui.Employee_ID_Input.text()):
        #     print(tags[0]['EPC-96'])
        #     rfid_check_query = '''SELECT TOP 1 * FROM RFID_Table WHERE TagID = (?);'''  # '?' is a placeholder
        #     cursor.execute(rfid_check_query, str(tags[0]['EPC-96']))
        #     if cursor.fetchone():
        #         get_asset_query = '''SELECT AssetID FROM RFID_Table WHERE TagID = (?);'''  # '?' is a placeholder
        #         cursor.execute(get_asset_query, str(tags[0]['EPC-96']))
        #         assetID = cursor.fetchone()
        #         if assetID[0] not in window.ItemEntry:
        #             print(assetID)
        #             window.rfid_insert(assetID[0])
        #         else:
        #             return


def RFID(result):
    if Employee_ID_Check(window.ui.Employee_ID_Input.text()):
        for tag in result:
            rfid_check_query = '''SELECT TOP 1 * FROM RFID_Table WHERE TagID = (?);'''  # '?' is a placeholder
            cursor.execute(rfid_check_query, str(tag))
            if cursor.fetchone():
                get_asset_query = '''SELECT AssetID FROM RFID_Table WHERE TagID = (?);'''  # '?' is a placeholder
                cursor.execute(get_asset_query, str(tag))
                assetID = cursor.fetchone()
                window.ItemEntry.append(assetID[0])
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
    check_query = '''SELECT TOP 1 * FROM Employee_Table WHERE EmployeeID = (?);''' # '?' is a placeholder
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
        self.StateEntry = []
        self.ItemEntry = []
        self.RemovedItems = []

        #connect button to functions
        self.ui.Done_Button.released.connect(self.done_button_clicked)  # button connected
        self.ui.Employee_ID_Enter.released.connect(self.Employee_enter)
        self.ui.Employee_ID_Enter.setFocusPolicy(Qt.ClickFocus)
        self.ui.Asset_ID_Enter.released.connect(self.asset_enter_action)
        self.ui.Asset_ID_Enter.setFocusPolicy(Qt.ClickFocus)
        self.ui.Cancel_Button.released.connect(self.cancel_button_clicked)  # button connected
        self.ui.Asset_ID_Input.returnPressed.connect(self.asset_enter_action)
        self.ui.Employee_ID_Input.returnPressed.connect(self.Employee_enter)
        self.ui.Check_Out_Box.setChecked(True)
        self.ui.Remove_Button.released.connect(self.remove_action)
        self.ui.New_Item_List.setAlternatingRowColors(True)
        self.ui.Existing_Item_list.setAlternatingRowColors(True)
        self.ui.Employee_ID_Input.setFocus()
        self.ui.Asset_ID_Input.setEnabled(False)
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.timer_timeout)

    def remove_action(self):
        row = self.ui.New_Item_List.currentRow()
        if row != 0:
            text = self.ui.New_Item_List.currentItem().text()
            self.RemovedItems.append(text)
            self.ItemEntry.remove(text)
            self.ui.New_Item_List.takeItem(row)

    def Employee_enter(self):

        if Employee_ID_Check(self.ui.Employee_ID_Input.text()):
            self.current_items(self.ui.Employee_ID_Input.text())
            self.ui.Asset_ID_Input.setEnabled(True)
            self.ui.Asset_ID_Input.setFocus()   
            self.ui.Employee_ID_Input.setReadOnly(True)
        else:
            self.error_message("Enter a valid Employee ID")
            return
    
    def done_button_clicked(self):
        self.StateEntry.append(self.ui.Employee_ID_Input.text())
        if self.ui.Check_In_Box.isChecked():
            print('Check IN action')
            self.check_in_action()
        elif self.ui.Check_Out_Box.isChecked():
            print('Check OUT action')
            self.check_out_action()
        else:
            self.error_message("Please select Check-In or Check-out action")
            self.StateEntry.clear()

    def cancel_button_clicked(self):
        self.ui.Employee_ID_Input.setReadOnly(False)
        self.ui.Employee_ID_Input.clear()
        self.ui.Asset_ID_Input.clear()
        self.ui.Asset_ID_Input.setEnabled(False)
        length = len(self.ItemEntry)
        while length > 0:
            self.ui.New_Item_List.takeItem(length)
            length -= 1
        length = len(self.StateEntry)
        while length > 0:
            self.ui.Existing_Item_list.takeItem(length)
            length -= 1
        self.ItemEntry.clear()
        self.StateEntry.clear()
        self.ui.Check_In_Box.setChecked(False)
        self.ui.Check_Out_Box.setChecked(False)

    def error_message(self, text):
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(text)
        error_dialog.setWindowTitle("Error")
        error_dialog.exec_()
        return
    
    def timer_timeout(self):
        print("timer running")
        self.ui.Asset_ID_Input.clear()

    def asset_enter_action(self):
            Asset = self.ui.Asset_ID_Input.text()
            #self.ItemEntry.append(Asset)
            print('Asset Number:' + Asset)
            if Asset_Check(Asset):
                if Asset not in self.ItemEntry: #any(Asset in sublist for sublist in self.ItemEntry) == False:
                    self.ui.New_Item_List.addItem(Asset)
                    #apend the entries into a list
                    self.ItemEntry.append(Asset)
                    self.ui.Asset_ID_Input.clear()
                else:
                     print('already in list')
                     self.ui.Asset_ID_Input.clear()
                     #self.error_message("Asset already selected")
                     self.timer.start(1000)
                     self.ui.Asset_ID_Input.setText("DUPLICATE!!!")
                
            else:
                print('invalid Asset')
                self.error_message("Enter a valid Asset ID")
            return

    def rfid_insert(self, asset):
        if asset not in self.ItemEntry:
            self.ItemEntry.append(asset)
            self.ui.New_Item_List.addItem(asset)
        # else:
        #     self.ui.Asset_ID_Input.setText('DUPLICATE!!!!')


    def check_in_action(self):
        # self.ui.Employee_ID_input.clear()
        if Employee_ID_Check(self.ui.Employee_ID_Input.text()):
            print('Valid Employee ID. ')
            self.sql_call("1")
        else:
            print('invalid employee ID. Please try again. ')
            return

    def check_out_action(self):
        # self.ui.Employee_ID_input.clear()
        if Employee_ID_Check(self.ui.Employee_ID_Input.text()):
            print('Valid Employee ID. ')
            self.sql_call("2")
        else:
            print('invalid employee ID. Please try again. ')
            return

    def sql_call(self,status):
        # global State_Log_Entry
        # global Item_Log_Entry
        # time = datetime.now()
        # datevar = date.today()
        # for employee in self.StateEntry:
        #     State_Log_Entry.append([employee, datevar.strftime("%d/%m/%Y") + "," + time.strftime("%H:%M:%S"), status])
        # for asset in self.ItemEntry:
        #     Item_Log_Entry.append([datevar.strftime("%d/%m/%Y") + "," + time.strftime("%H:%M:%S"), asset])
        #
        # insert_item_query = '''INSERT INTO Item_Log_Table(TIMESTAMP,ASSETID)
        #                                    VALUES (?,?);'''  # '?' is a placeholder
        # insert_state_query = '''INSERT INTO State_Log_Table(EMPLOYEEID,TIMESTAMP,STATUS)
        #                                                VALUES (?,?,?);'''  # '?' is a placeholder
        # for entry in State_Log_Entry:
        #     # define the values to insert
        #     stateValues = (entry[0], entry[1], entry[2])
        #     print(stateValues)
        #     # insert the data into the database
        #     cursor.execute(insert_state_query, stateValues)
        # # commit the inserts
        # cnxn.commit()
        #
        # # loop thru each row in the matrix
        # for entry in Item_Log_Entry:
        #     # define the values to insert
        #     itemValues = (entry[0], entry[1])
        #     print(itemValues)
        #     # insert the data into the database
        #     cursor.execute(insert_item_query,itemValues)
        # cnxn.commit()
        #
        #
        #
        # # insert_event_query = ''' INSERT INTO
        # #                          Event_Log_Table (EMPLOYEEID,TIMESTAMP, ASSETID, STATUS)
        # #                          SELECT
        # #                          State_Log_Table.EMPLOYEEID, State_Log_Table.TIMESTAMP,Item_Log_Table.AssetID, State_Log_Table.STATUS
        # #                          FROM
        # #                          State_Log_Table
        # #                          FULL OUTER JOIN Item_Log_Table
        # #                          ON
        # #                          State_Log_Table.TIMESTAMP = Item_Log_Table.TIMESTAMP;
        # #                         '''
        #
        # # cursor.execute(insert_event_query)
        # # cnxn.commit()
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
        self.ui.Existing_Item_list.addItem(assets[0])
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
    # server = "BALKARAN09"
    # database = 'TEST'

    server = "Raymond-P1"
    database = 'RCMP_RFID'

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