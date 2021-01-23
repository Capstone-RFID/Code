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

#*********************NOTES ON HOW TO USE THIS CLASS*************************
#Should go without saying that this file needs to be in the same directory as your main
#
#1. Need import statement @ top of main .py file: from AdminInterface import Admin_Interface
#
#2. Need this line to define admin button connection in __init__ of main window class: self.ui.Admin_Button.clicked.connect(self.adminButtonClicked)
#
#
#3. Need this instance to use AdminInterface class
#       self.admin = Admin_Interface()
#
#
#4. Also need the following function defined within the mainWindow class:
# def adminButtonClicked(self):
#     print('clicked admin')
#
#     self.admin.openAdmin()
#
# As of writing (Jan 21, 2021), the rest of this class should be fairly self contained and not need anything else in main file

#*********************END NOTES ON HOW TO USE THIS CLASS*************************

class Admin_Interface(QWidget):
    def __init__(self):
        super(Admin_Interface, self).__init__()
        self.reactor = reactor
        self.ui = Ui_Admin_Interface()
        self.ui.setupUi(self)

        # ****************************************Home Tab Button(s)*********************************
        self.ui.Home_Force_Sync_Button.clicked.connect(self.home_syncButtonClicked)  # sync button connected

        #****************************************Search Tab Button(s)*********************************
        self.ui.Search_SearchID_Query_Button.clicked.connect(self.search_searchIDButtonClicked)
        self.ui.Search_SearchAsset_Query_Button.clicked.connect(self.search_searchAssetButtonClicked)
        self.ui.Search_SearchDate_Query_Button.clicked.connect(self.search_searchDateButtonClicked)
        self.ui.Search_Print_PDF_Button.clicked.connect(self.search_printPDFButtonClicked)

        # ****************************************Edit Tab Button(s)*********************************
        self.ui.Edit_Clear_Button.clicked.connect(self.edit_clearButtonClicked)
        self.ui.Edit_Search_Button.clicked.connect(self.edit_searchButtonClicked)
        self.ui.Edit_Delete_Entry_Button.clicked.connect(self.edit_deleteButtonClicked)
        self.ui.Edit_Commit_Edits_Button.clicked.connect(self.edit_commitButtonClicked)

        # ****************************************Create Tab Button(s)*********************************
        self.ui.Create_Clear_Fields_Button.clicked.connect(self.create_clearButtonClicked)
        self.ui.Create_Confirm_Entry_Button.clicked.connect(self.create_confirmEntryButtonClicked)

        # ****************************************Resolve Tab Button(s)*********************************
        #Nothing here yet, define button connections here when we put something in the GUI

        #
        # define the server name and the database name
        server = 'BIGACER'
        database = 'BALKARAN09'

        # define a connection string
        self.cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                                        SERVER=' + server + ';\
                                          DATABASE=' + database + ';\
                                        Trusted_Connection=yes;')

        # create the connection cursor as a private variable
        self.cursor = self.cnxn.cursor()

    # open up the admin window from the button on main window
    def openAdmin(self):
        self.show()

    #****************************************Class Methods for Tab Button(s)*********************************
    def home_syncButtonClicked(self):

        print("Home Sync Button Clicked")

    def search_searchIDButtonClicked(self):
        print('Search Tab Search ID Button Clicked')
        #if self.Employee_ID_Check(self.ui.Search_Employee_ID_Entry_Field.text()):
        EmployeeNum = self.ui.Search_Employee_ID_Entry_Field.text()

        if self.Employee_ID_Check(EmployeeNum):
            EmployeeAssetList = self.Employee_ID_FindAssets(EmployeeNum)
            print(EmployeeAssetList)




    def search_searchAssetButtonClicked(self):
        print('Search Tab Search Asset Button Clicked')
        AssetLowerBound = self.ui.Search_Asset_Numbers_From_Field.text()

        AssetUpperBound = self.ui.Search_Asset_Numbers_To_Field.text()
        AssetList = self.Asset_Check(AssetLowerBound,AssetUpperBound)
        print(AssetList)
        # Sample select query
        #self.cursor.execute("SELECT Status, [Employee ID] FROM Asset")

    def search_searchDateButtonClicked(self):
        print('Search Tab Search Date Button Clicked')

      #  for entries in self.cursor.fetchall():
      #      print(entries)
      #      test = entries[1]
      #      print(test)

    def search_printPDFButtonClicked(self):
        print('Search Tab Print Button Clicked')

    def edit_clearButtonClicked(self):
        print('Edit Tab Clear Button Clicked')
    def edit_searchButtonClicked(self):
        print('Edit Tab Search Button Clicked')
    def edit_deleteButtonClicked(self):
        print('Edit Tab Delete Button Clicked')
    def edit_commitButtonClicked(self):
        print('Edit Tab Commit Button Clicked')

    def create_clearButtonClicked(self):
        print('Create Tab Clear Button Clicked')
    def create_confirmEntryButtonClicked(self):
        print('Create Tab Confirm Entry Button Clicked')

    # ****************************************End Class Methods for Tab Button(s)*****************************
    # ****************************************Class Methods for Running Queries*******************************
    #Searches for employee_ID in database, returns true if it exists else returns false
    def Employee_ID_Check(self, input):
        check_query = '''SELECT TOP 1 * FROM Employee WHERE [Employee ID] = (?);'''  # '?' is a placeholder
        self.cursor.execute(check_query, str(input))
        if self.cursor.fetchone():
            print('This ID exists!')
            return True
        else:
            return False

    def Employee_ID_FindAssets(self, input):
        check_query = '''SELECT * FROM Asset WHERE ([Employee ID]=  (?));'''  # '?' is a placeholder
        self.cursor.execute(check_query, str(input))
        if self.cursor.fetchone():
            print('This ID has used assets!')
            self.cursor.execute(check_query, str(input))
            return self.cursor.fetchall()
        else:
            print('This ID has not used assets!')
            return False


    #Searchs for a list of assets specified by lower and upper bound of asset #'s
    #returns list within and including bounds
    def Asset_Check(self, LowerBound, UpperBound):
        check_query = '''SELECT * FROM Asset WHERE (Asset# >=  (?)) AND (Asset# <=  (?));'''  # '?' is a placeholder
        self.cursor.execute(check_query, str(LowerBound),str(UpperBound))
        if self.cursor.fetchone():
            self.cursor.execute(check_query, str(LowerBound), str(UpperBound))
            return True
        else:
            return False

    def Asset_List_Fetch(self, LowerBound, UpperBound):
        check_query = '''SELECT * FROM Asset WHERE (Asset# >=  (?)) AND (Asset# <=  (?));'''  # '?' is a placeholder
        self.cursor.execute(check_query, str(LowerBound),str(UpperBound))
        if self.cursor.fetchone():
            self.cursor.execute(check_query, str(LowerBound), str(UpperBound))
            return self.cursor.fetchall()
        else:
            return False


