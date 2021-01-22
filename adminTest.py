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

    #When you click Admin on main window, bring up the tabbed admin interface in a new window
    #Jon Addition
    def adminButtonClicked(self):
        print('clicked admin')

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