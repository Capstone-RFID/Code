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
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import *
import sys

#Need this to use Admin class
#Jon Addition
from AdminInterface import Admin_Interface

from Etek_main_window_All_In_One import Ui_Form

# readFlag = False #used to check if employeeID is in the database
# eqcheck = "undermined"
# employeeID = '0'
# equipmentID = []
#
# tagIdentity = 0  #lets get rid of a lot of globals
#
#
#
#
# def cb(tagReport):
#     # print("running")
#     global readFlag
#     if keyboard.is_pressed('q'):
#         reactor.stop()
#         mode = 'q'
#     tags = tagReport.msgdict['RO_ACCESS_REPORT']['TagReportData']
#     if len(tags) != 0:
#         if readFlag == True :
#             filterInfo(tags[0]['EPC-96'])
#
#
#
#
# def shutdown(factory):
#     return factory.politeShutdown()
#
#
# def filterInfo(tagID):
#     check = any(str(tagID) in sublist for sublist in equipmentID) #check if the same equipment is already in database
#     if check == False:
#         assetNum = "Radio"
#         global employeeID
#         description = "tag"
#         equipmentID.append([assetNum,str(tagID),employeeID,date.today().strftime("%d/%m/%Y"),datetime.now().strftime("%H:%M:%S"),eqcheck,description])
#         print(str(tagID[20:26]))
#         insert()
#         # print("Do you want to SYNC: ")
#         # sync = str(input())
#         # if sync =='T':
#         #     snapshot()
#
#
# def insert():
#
#     # define our insert and update query
#     insert_query = '''INSERT INTO Equipment(ASSET_NUMBER,RFID_TAG_#,LAST_USED_BY_EMPLOYEE,LAST_SEEN_DATE,LAST_SEEN_TIME,STATUS,DESCRIPTION)
#                         VALUES (?,?,?,?,?,?,?);'''  # '?' is a placeholder
#
#     # loop thru each row in the matrix
#     for row in equipmentID:
#         # define the values to insert
#         values = (row[0], row[1],row[2],row[3],row[4],row[5],row[6])
#         print(values)
#         # insert the data into the database
#         #cursor.execute(insert_query, values)
#
#     # commit the inserts
#    # cnxn.commit()
#
#     # grab all the rows in our database table
#     #cursor.execute('SELECT ID FROM Employees')
#
#    # loop through the results
#    # for row in cursor:
#       #  print(row)
#
#     # close the connection and remove the cursor
#     #cursor.close
#    # cnxn.close
#
# ##work in progress
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
#        # cursor.execute(update_query, values)
#
#
# def snapshot():
#     subprocess.run(
#         ["C:\\Program Files\\Microsoft SQL Server\\150\\COM\\snapshot.exe",
#          "-Publisher", "[BALKARAN09]", "-PublisherDB", "[TEST]",
#          "-Distributor", "[BALKARAN09]", "-Publication", "[please_merge]",
#          "-ReplicationType", "2", "-DistributorSecurityMode", "1"],
#         # probably add this
#         check=True)
#
#
# def stop():
#     reactor.stop()
# #
# # def Employee_ID_Check(input):
# #     check_query = '''SELECT TOP 1 * FROM EmployeeTable WHERE ID = (?);''' # '?' is a placeholder
# #     cursor.execute(check_query, str(input))
# #     global readFlag, eqcheck
# #     if cursor.fetchone():
# #         readFlag = True
# #         eqcheck = "Check-In"
# #         return True
# #     else:
# #         readFlag = False
# #         return False

class mainWindow(QWidget):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.reactor = reactor
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show()
        #initialize classes:
        self.admin = Admin_Interface()
        #self.checkIn = CheckInWindow()
        #connect button to functions
        self.ui.Check_Out_Button.clicked.connect(self.checkoutClicked)  # button connected
        self.ui.Finish_Button.clicked.connect(self.checkinClicked)  # button connected

        #Also need this to define admin button connection
        self.ui.Admin_Button.clicked.connect(self.adminButtonClicked)  # button connected

    #When you click Admin on main window, bring up the tabbed admin interface
    #Jon Addition
    def adminButtonClicked(self):
        print('clicked admin')
        #self.ui.hide()
        self.admin.openAdmin()




    def checkinClicked(self):
        print("Check-In clicked")
        # EmployeeID = self.ui.Employee_ID_input.text()
        # print('Your Employee ID Number: ' + EmployeeID)
        # global employeeID, tagIDtoreturn
        # employeeID = EmployeeID
        # self.ui.Employee_ID_input.clear()
        # if Employee_ID_Check(EmployeeID):
        #     self.checkIn.show()
        # else:
        #     return

        # filterInfo(self.EmployeeID)
        # global readFlag
        # readFlag = True

    def checkoutClicked(self):
        print("Check-Out clicked")

        #self.checkIn.show()




# class CheckOutWindow(QWidget):
#     def __init__(self):
#         super(CheckInWindow, self).__init__()
#         #self.ui = Ui_Form()
#         self.ui.setupUi(self)
#         self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
#



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = mainWindow()
    #RFID init
    # logging.getLogger().setLevel(logging.INFO)
    # factory = llrp.LLRPClientFactory(antennas=[1], start_inventory=True, session=0, duration=0.8)
    # factory.addTagReportCallback(cb)
    # reactor.connectTCP('169.254.10.1', llrp.LLRP_PORT, factory)
    #
    # # define the server name and the database name
    # server = "BALKARAN09"
    # database = 'TEST'
    #
    # # define a connection string
    # cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
    #                         SERVER=' + server + ';\
    #                           DATABASE=' + database + ';\
    #                         Trusted_Connection=yes;')
    #
    # # create the connection cursor
    # cursor = cnxn.cursor()
    # #it works now
    # # if readFlag == True:
    Thread(target=reactor.run, args=(False,)).start()
    Thread(target=sys.exit(app.exec_()), args=(False,)).start()