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
from Admin_Level2_Access import Ui_Admin_Interface

readFlag = False #used to check if employeeID is in the database
eqcheck = "undermined"
employeeID = '0'
equipmentID = []

tagIdentity = 0  #lets get rid of a lot of globals




class Admin_Interface(QWidget):
    def __init__(self):
        super(Admin_Interface, self).__init__()
        self.reactor = reactor
        self.ui = Ui_Admin_Interface()
        self.ui.setupUi(self)
        #self.show()
        #initialize classes:
        #self.checkIn = CheckInWindow()
        #connect button to functions
        self.ui.Home_Force_Sync_Button.clicked.connect(self.syncClicked)  # button connected
        #self.ui.Check_In_button.clicked.connect(self.checkinClicked)  # button connected


    def syncClicked(self):

        print("Sync Clicked")
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



    def testfunction(self):
        self.show()
        print('hello')





# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     window = mainWindow()
#     #RFID init
#     logging.getLogger().setLevel(logging.INFO)
#     factory = llrp.LLRPClientFactory(antennas=[1], start_inventory=True, session=0, duration=0.8)
#     factory.addTagReportCallback(cb)
#     reactor.connectTCP('169.254.10.1', llrp.LLRP_PORT, factory)
#
#     # define the server name and the database name
#     server = "BALKARAN09"
#     database = 'TEST'
#
#     # define a connection string
#     cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
#                             SERVER=' + server + ';\
#                               DATABASE=' + database + ';\
#                             Trusted_Connection=yes;')
#
#     # create the connection cursor
#     cursor = cnxn.cursor()
#     #it works now
#     # if readFlag == True:
#     Thread(target=reactor.run, args=(False,)).start()
#     Thread(target=sys.exit(app.exec_()), args=(False,)).start()