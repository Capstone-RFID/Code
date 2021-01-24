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
from PyQt5.QtWidgets import *
import sys
from Etek_main_window_All_In_One import Ui_MainWindow
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
    if len(tags) != 0:
        # taglist.append(tags[0]['EPC-96'])
        # if tags[0]['EPC-96'] not in taglist:
            RFID(tags[0]['EPC-96'])
        # else:
        #     window.error_message("haha")

        # if Employee_ID_Check(window.ui.Employee_ID_input.text()):
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


def RFID(tag):
    if Employee_ID_Check(window.ui.Employee_ID_input.text()):
        print(tag)
        rfid_check_query = '''SELECT TOP 1 * FROM RFID_Table WHERE TagID = (?);'''  # '?' is a placeholder
        cursor.execute(rfid_check_query, str(tag))
        if cursor.fetchone():
            get_asset_query = '''SELECT AssetID FROM RFID_Table WHERE TagID = (?);'''  # '?' is a placeholder
            cursor.execute(get_asset_query, str(tag))
            assetID = cursor.fetchone()
            window.rfid_insert(assetID[0])

def shutdown(factory):
    return factory.politeShutdown()

def checkOut():
    print(State_Log_Entry)
    print(Item_Log_Entry)

    # check = any(str(tagID) in sublist for sublist in equipmentID) #check if the same equipment is already in database
    # if check == False:
    #     assetNum = "Radio"
    #     global employeeID
    #     description = "tag"
    #     equipmentID.append([assetNum,str(tagID),employeeID,date.today().strftime("%d/%m/%Y"),datetime.now().strftime("%H:%M:%S"),eqcheck,description])
    #     print(str(tagID[20:26]))
    #     insert()
        # print("Do you want to SYNC: ")
        # sync = str(input())
        # if sync =='T':
        #     snapshot()


def insert():

    # define our insert and update query
    insert_query = '''INSERT INTO Item_Log_Table (Timestamp,AssetID)
                        VALUES (?,?);'''  # '?' is a placeholder

    # loop thru each row in the matrix
    for row in equipmentID:
        # define the values to insert
        values = (row[0], row[1],row[2],row[3],row[4],row[5],row[6])
        print(values)
        # insert the data into the database

    cursor.execute(insert_query, values)

    # commit the inserts
    cnxn.commit()

    # grab all the rows in our database table
    #cursor.execute('SELECT ID FROM Employees')

   # loop through the results
   # for row in cursor:
      #  print(row)

    # close the connection and remove the cursor
    cursor.close
    cnxn.close

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
        #connect button to functions
        self.ui.Check_Out_Button.released.connect(self.check_out_button_clicked)  # button connected
        self.ui.Finish_Button.released.connect(self.check_in_button_clicked)  # button connected
        self.ui.Asset_Ok_Button.released.connect(self.asset_ok_button_clicked)
        self.ui.Cancel_Button.released.connect(self.cancel_button_clicked)  # button connected
        self.ui.Asset_input.returnPressed.connect(self.asset_ok_button_clicked)
        self.ui.Employee_ID_input.returnPressed.connect(self.Employee_enter)
        self.ui.Employee_ID_input.setFocus()

    def Employee_enter(self):
        if Employee_ID_Check(self.ui.Employee_ID_input.text()):
            self.ui.Asset_input.setFocus()


    def cancel_button_clicked(self):
        self.ui.Employee_ID_input.setReadOnly(False)
        self.ui.Employee_ID_input.clear()
        self.ui.Asset_input.clear()
        self.ItemEntry.clear()
        self.StateEntry.clear()

    def error_message(self, text):
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(text)
        error_dialog.setWindowTitle("Error")
        error_dialog.exec_()
        return

    def asset_ok_button_clicked(self):
        if Employee_ID_Check(self.ui.Employee_ID_input.text()):
            self.ui.Employee_ID_input.setReadOnly(True)
            Asset = self.ui.Asset_input.text()
            #self.ItemEntry.append(Asset)
            print('Asset Number:' + Asset)
            if Asset_Check(Asset):
                if Asset not in self.ItemEntry: #any(Asset in sublist for sublist in self.ItemEntry) == False:
                    lastrow = self.ui.Equipment_List.rowCount()
                    self.ui.Equipment_List.insertRow(lastrow)
                    item = QTableWidgetItem(Asset)

                    self.ui.Equipment_List.setItem(lastrow, 0, item)
                    #apend the entrieds into a list
                    self.StateEntry.append(self.ui.Employee_ID_input.text())
                    self.ItemEntry.append(Asset)
                else:
                     print('already in list')
                    # text = str('already in list')
                     #self.error_message(text)
                     # error_dialog = QtWidgets.QErrorMessage()
                     # error_dialog.showMessage('Enter an Valid Asset Number')
                     # error_dialog.setWindowTitle("Error")
                     # error_dialog.exec_()
                     # duplicate = QMessageBox()
                     # duplicate.setText('duplicate')

                self.ui.Asset_input.clear()
            else:

                print('invalid Asset')
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('Enter an Valid Asset Number')
                error_dialog.setWindowTitle("Error")
                error_dialog.exec_()
            return
        else:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Invalid Employee ID')
            error_dialog.setWindowTitle("Error")
            error_dialog.exec_()
            return

    def rfid_insert(self, asset):
        self.ui.Asset_input.clear()
        self.ui.Asset_input.insert(asset)
        self.asset_ok_button_clicked()



    def check_in_button_clicked(self):
        print("'ha")

        # filterInfo(self.EmployeeID)
        # global readFlag
        # readFlag = True

    def check_out_button_clicked(self):
        global State_Log_Entry
        global Item_Log_Entry
        # self.ui.Employee_ID_input.clear()
        if Employee_ID_Check(self.ui.Employee_ID_input.text()):
            print('Valid Employee ID. ')
            time = datetime.now()
            datevar = date.today()
            for employee in self.StateEntry:
                State_Log_Entry.append([employee, datevar.strftime("%d/%m/%Y") + "," + time.strftime("%H:%M:%S"), "2"])
            for asset in self.ItemEntry:
                Item_Log_Entry.append([datevar.strftime("%d/%m/%Y") + "," + time.strftime("%H:%M:%S"), asset])

            insert_item_query = '''INSERT INTO Item_Log_Table (TIMESTAMP,ASSETID)
                                    VALUES (?,?); '''  # '?' is a placeholder
            insert_state_query = '''INSERT INTO State_Log_Table (EMPLOYEEID,TIMESTAMP,STATUS)
                                                VALUES (?,?,?);'''  # '?' is a placeholder

            # loop thru each row in the matrix
            for entry in Item_Log_Entry:
                # define the values to insert
                itemValues = (entry[0], entry[1])
                print(itemValues)
                # insert the data into the database
                cursor.execute(insert_item_query, itemValues)


            for entry in State_Log_Entry:
                # define the values to insert
                stateValues = (entry[0], entry[1],entry[2])
                print(stateValues)
                # insert the data into the database
                cursor.execute(insert_state_query, stateValues)

            # commit the inserts
            cnxn.commit()
        else:
            print('invalid employee ID. Please try again. ')

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