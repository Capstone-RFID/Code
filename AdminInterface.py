from sllurp import llrp
from twisted.internet import reactor
import pyodbc
from datetime import datetime
from datetime import date

from threading import Thread
import subprocess
import keyboard


#for reading excel files
import numpy as np
import pandas as pd
from pathlib import Path
import os
#Regular expressions
import re
#import xlrd
#from openpyxl import load_workbook

from pandas import ExcelWriter
from pandas import ExcelFile

from PyQt5 import QtCore, QtGui, QtWidgets,  QtPrintSupport
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from Admin_Level2_Access import Ui_Admin_Interface
from password_change_prompt import Ui_PasswordChangeDialog
import sys

import hashlib


#For reading passwords
from configparser import ConfigParser
import openpyxl
#for generating log text file for exception handling and timestamp of all user actions
import logging
#format log file to save as 'ETEK.log' and store date time and message of actions or errors
#logging.basicConfig(filename='ETEK.log', filemode='w', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
from logging.handlers import TimedRotatingFileHandler
FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s", datefmt='%d-%b-%y %H:%M:%S')
LOG_FILE = "ETEK.log"
IMPORT_LOG_FILE = "IMPORT.log"
def get_console_handler():
   console_handler = logging.StreamHandler(sys.stdout)
   console_handler.setFormatter(FORMATTER)
   return console_handler
def get_file_handler():
   file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
   file_handler.setFormatter(FORMATTER)
   return file_handler
def get_file_handler2():
   file_handler = TimedRotatingFileHandler(IMPORT_LOG_FILE, when='midnight')
   file_handler.setFormatter(FORMATTER)
   return file_handler
def get_logger(logger_name):
   logger = logging.getLogger(logger_name)
   logger.setLevel(logging.DEBUG) # better to have too much log than not enough
   logger.addHandler(get_console_handler())
   logger.addHandler(get_file_handler())
   # with this pattern, it's rarely necessary to propagate the error up to parent
   logger.propagate = False
   return logger
def get_logger2(logger_name):
   logger = logging.getLogger(logger_name)
   logger.setLevel(logging.DEBUG) # better to have too much log than not enough
   logger.addHandler(get_console_handler())
   logger.addHandler(get_file_handler2())
   # with this pattern, it's rarely necessary to propagate the error up to parent
   logger.propagate = False
   return logger
# define global logger variable using the global current user ID
CurrentUser = ''
ETEK_log = get_logger('Admin Action' + CurrentUser)
Import_log = get_logger2('Import')
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
# As of writing (Jan 30, 2021), the rest of this class should be fairly self contained and not need anything else in main file

#*********************END NOTES ON HOW TO USE THIS CLASS*************************



class Admin_Interface(QWidget):
    def __init__(self):
        super(Admin_Interface, self).__init__()
        self.reactor = reactor
        self.ui = Ui_Admin_Interface()
        self.ui.setupUi(self)

        self.ChangePasswordWindow = changePassword()

        #Stop user from editing tables
        self.ui.Search_Display_Results_Table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # ****************************************Private Var(s)*********************************
        self.userLoggedIn = ""

        self.StateEntry = []
        self.ItemEntry = []

        #For storing the data on the search results table in the edit tab
        self.edit_AssetsInGUITable = []
        self.edit_EmployeesInGUITable = []
        self.edit_StatusInGUITable = []

        self.filePath = str(r'C:\Users\cbker\Documents\GitHub\E-TekCode') #change this to wherever your excel import docs are stashed
        self.import_EmployeeIDList = []
        self.import_EmployeeNameList = []
        self.import_AssetList = []
        self.import_EmployeeIDList_AlreadyExisting = []

        #Initialize this with nothing to start
        self.edit_AssetSearchedInDatabase = None
        # ****************************************Asset Validators*********************************
        # validator to only enter valid asset ID's into asset ID entry fields

        rExpSearch = QRegExp("(([Ee][0-9]{7}|[4][0-9]{6})(,{1}))*")
        MultiAssetValid = QtGui.QRegExpValidator(rExpSearch, self.ui.Search_Asset_Numbers_Field)
        self.ui.Search_Asset_Numbers_Field.setValidator(MultiAssetValid)

        rExpEditCreateAssigntag = QRegExp("([Ee][0-9]{7}|[4][0-9]{6})")
        SingleAssetValid = QtGui.QRegExpValidator(rExpEditCreateAssigntag, self.ui.Edit_Asset_Field)
        self.ui.Edit_Asset_Field.setValidator(SingleAssetValid)


        CreateTabValid = QtGui.QRegExpValidator(rExpEditCreateAssigntag, self.ui.Create_Asset_Num_Field)
        self.ui.Create_Asset_Num_Field.setValidator(CreateTabValid)

        Edit_EmployeeFieldsValid = QtGui.QIntValidator()
        self.ui.Edit_AssignTo_Field.setValidator(Edit_EmployeeFieldsValid)

        Edit_AssignTo_Valid = QtGui.QIntValidator()
        self.ui.Search_Employee_ID_Entry_Field.setValidator(Edit_AssignTo_Valid)

        #Regex for a 24 digit hex number (either ABCDEF OR Numerical 0-9)
        rExpRFID = QRegExp("([ABCDEF]|[0-9]){24}")
        RFIDValid = QtGui.QRegExpValidator(rExpRFID, self.ui.AssignTag_RFID_Tag_Field)
        self.ui.AssignTag_RFID_Tag_Field.setValidator(RFIDValid)

        self.ui.AssignTag_Asset_Num_Field.setValidator(SingleAssetValid)
        # ****************************************End of Validators*********************************

        # ****************************************Home Tab Button(s)*********************************
        self.ui.Home_ChangePassword_Button.clicked.connect(self.home_changePasswordButtonClicked)  # sync button connected

        #****************************************Search Tab Button(s)*********************************
        #self.ui.Search_SearchID_Query_Button.clicked.connect(self.search_searchIDButtonClicked)
        self.ui.Search_SearchAsset_Query_Button.clicked.connect(self.search_checkFieldInputs)
        self.ui.Search_Employee_ID_Entry_Field.returnPressed.connect(self.search_checkFieldInputs)
        self.ui.Search_Asset_Numbers_Field.returnPressed.connect(self.search_checkFieldInputs)
        self.ui.Search_Print_PDF_Button.clicked.connect(self.search_printPDFButtonClicked)
        self.ui.Search_Reset_Fields_Button.clicked.connect(self.search_searchResetFieldsButtonClicked)
        self.ui.Search_Display_Help_Button.clicked.connect(self.search_helpButton)
        # ****************************************Edit Tab Button(s)*********************************
        self.ui.Edit_Clear_Button.clicked.connect(self.edit_clearButtonClicked)
        self.ui.Edit_Commit_Edits_Button.clicked.connect(self.edit_commitButtonClicked)
        self.ui.Edit_Display_Help_Button.clicked.connect(self.edit_helpButton)

        # ****************************************Create Tab Button(s)*********************************
        self.ui.Create_Clear_Fields_Button.clicked.connect(self.create_clearButtonClicked)
        self.ui.Create_Confirm_Entry_Button.clicked.connect(self.create_confirmEntryButtonClicked)
        self.ui.Import_ImportAssets_Button.clicked.connect(self.Import_ImportAssets_ButtonClicked)
        self.ui.Import_ImportEmployees_Button.clicked.connect(self.Import_ImportEmployees_ButtonClicked)
        self.ui.Create_Display_Help_Button.clicked.connect(self.create_helpButton)
        # ****************************************Assign Tag Tab Button(s)*********************************
        self.ui.AssignTag_Confirm_Entry_Button.clicked.connect(self.AssignTag_confirmButtonClicked)
        self.ui.AssignTag_Remove_Tag_Button.clicked.connect(self.AssignTag_removeButtonClicked)
        self.ui.AssignTag_Clear_Fields_Button.clicked.connect(self.AssignTag_clearButtonClicked)
        self.ui.AssignTag_Display_Help_Button.clicked.connect(self.AssignTag_helpButton)
        # ****************************************Resolve Tab Button(s)*********************************
        #Nothing here yet, define button connections here when we put something in the GUI

        # ****************************************QMessageBox (Used across tabs)*********************************
        self.qm = QtWidgets.QMessageBox()

    def search_helpButton(self):

        self.qm.setFixedSize(3000, 5000)
        self.qm.information(self, 'Help',
                            'The search tab allows you to list records from the event log table in the local database\n\nUse/combine filters to find records that meet the criteria specified\n\nUsing the Date/Time filters allows you to set two dates and retrieve records from between those dates\n\nMonth by Month returns records from that month across all years in the database\n\nThe Employee and Asset ID(s) allow you to look for only the employees and assets specified\n\nTo search multiple assets at once, type in each asset ID seperated by a comma')
    def edit_helpButton(self):

        self.qm.setFixedSize(3000, 5000)
        self.qm.information(self, 'Help',
                            'The edit tab allows you to update the status of an asset\n\nYou can update an asset as assigned to an employee ID as either checked-in or checked-out\n\nPlease note that you can not assign something to an employee as any other status than specified above ')
    def create_helpButton(self):

        self.qm.setFixedSize(3000, 5000)
        self.qm.information(self, 'Help',
                            'The create tab is where you can enter new asset ID(s) into the local database by:\n\n1. Entering in the new Asset\n\n2. Making a .xlsx file in excel as in the user manual section "Import File Formats"\n\nYou can also add in new employee IDs into the database by making a .xlsx file in excel as in the user manual "Import File Formats"\n\nIf you need to assign an RFID tag to an individual asset, please use the "Assign Tag" tab')
    def AssignTag_helpButton(self):

        self.qm.setFixedSize(3000, 5000)
        self.qm.information(self, 'Help',
                            'To assign an RFID Tag to an asset:\n\n1. Enter the asset number into the asset field\n\n2. Enter in the 24-digit hexidecimal value of the RFID tag you want to assign to that asset ID\n\nTo remove an RFID tag from an asset, enter the asset number and click the "remove tag" button')
    def RFIDINSERT(self, tag):
        if self.ui.Create_Tab.isVisible() and self.ui.Create_RFID_Tag_Field_3.text()=="":
            self.ui.Create_RFID_Tag_Field_3.insert(tag)
    # open up the admin window from the button on main window
    def openAdmin(self, s, d, userLoggedIn):
        self.userLoggedIn = userLoggedIn
        global CurrentUser
        CurrentUser = userLoggedIn
        print("The admin who just logged in has the ID: " + self.userLoggedIn)
        self.show()
        #set default tab on window opening to home tab
        self.ui.Admin_Select.setCurrentIndex(0)
        server = s
        database = d
        #Set default datetime values to show admin users required format for input
        d = QDate(2021, 1, 1)
        self.ui.Search_Datetime_From.setDate(d)
        self.ui.Search_Datetime_To.setDate(d)
         # define a connection string
        try:
            self.cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                                            SERVER=' + server + ';\
                                              DATABASE=' + database + ';\
                                            Trusted_Connection=yes;')
            # create the connection cursor as a private variable
            self.cursor = self.cnxn.cursor()

            ETEK_log.info('Connected to Server ' + server + ' and ' + database)


        except:
            ETEK_log.error('Unable to connect to Server ' + server + ' and ' + database + ' please check configuration file.')
    #****************************************Class Methods for Tab Button(s)*********************************
    def home_changePasswordButtonClicked(self):

        print("Change Password Button Clicked")
        self.ChangePasswordWindow.open(self.userLoggedIn)





    def search_searchResetFieldsButtonClicked(self):

        try:
            # Reset Filters to default values
            self.ui.Search_Employee_ID_Entry_Field.setText("")
            self.ui.Search_Asset_Numbers_Field.setText("")
            self.ui.Search_UI_Message_Prompt.setText("")
            d = QDate(2021, 1, 1)
            self.ui.Search_Datetime_From.setDate(d)
            self.ui.Search_Datetime_To.setDate(d)
            self.ui.Search_Month_By_Month_Search_Dropdown.setCurrentIndex(0)

            #clear search results in table
            self.search_clearTableResults()
            ETEK_log.info('Search Filters reset')
        except:
            ETEK_log.error('Error while resetting Search Filters')



    #Generates list of assets in event log based on Employee ID search Filter
    def search_searchIDButtonClicked(self):
        try:
            print('Search Tab Search ID Button Clicked')
            #if self.Employee_ID_Check(self.ui.Search_Employee_ID_Entry_Field.text()):
            EmployeeNum = self.ui.Search_Employee_ID_Entry_Field.text()

            if self.Employee_ID_Check(EmployeeNum):
                EmployeeAssetList = self.Employee_ID_FindAssets(EmployeeNum)
                if EmployeeAssetList != False:
                    self.search_PopulateTable(EmployeeAssetList)
                    ETEK_log.info('Search for Employee ID (' + EmployeeNum + ') - events found')
                else:
                    self.qm.warning(self, 'No events found for Employee ID')
                    ETEK_log.info('Search for Employee ID (' + EmployeeNum + ') - no events found')
            else:
                #self.ui.Search_UI_Message_Prompt.setText('No matching employee ID found')
                self.qm.warning(self, 'Notice', 'No matching employee ID found')
                ETEK_log.info('Search for Employee ID (' + EmployeeNum + ') - no matching employee found')

                #self.ui.Search_UI_Message_Prompt.setText('Found Employee ID')
        # Generates list of EmployeeID in event log based on Assets in search Filter

        except:
            ETEK_log.error('Error while searching for Employee ID. In function - search_searchIDButtonClicked')

    #Checks to see if entered asset# exists in asset table, populates table w/ query results if it is
    def search_searchAssetButtonClicked(self, AssetInputs):
        try:
            print('Search Tab Search Asset Button Clicked')
            #AssetNum = self.ui.Search_Asset_Numbers_Field.text()
            EmployeeNum = self.ui.Search_Employee_ID_Entry_Field.text()
            for AssetNum in AssetInputs:
                #
                if self.Asset_Check(AssetNum):
                    AssetList = self.Asset_List_Fetch(AssetNum)
                    self.search_PopulateTable(AssetList)
                    ETEK_log.info('Search for Asset Number (' + AssetNum + ') - events found')
                elif not self.Asset_Check(AssetNum) and (len(AssetInputs) > 1):
                    self.qm.critical(self, 'Notice', 'Asset number ' + AssetNum + ' does not exist in local database')
                    self.qm.warning(self, 'Notice', 'At least one asset not found')
                    ETEK_log.info('Search for Asset Number (' + AssetNum + ') - does not exist in local database')
                elif not self.Asset_Check(AssetNum):
                    self.qm.critical(self, 'Notice', 'Asset number ' + AssetNum + ' does not exist in local database')
                    ETEK_log.info('Search for Asset Number (' + AssetNum + ') - does not exist in local database')
        except:
            ETEK_log.error('Error while searching for Assets. In function - search_searchAssetButtonClicked')

    def search_searchAssetandIDButtonClicked(self,AssetString):

        try:
            atLeastOneAssetNotFound_Flag = 0
            print('Search Tab Search Asset and ID Button Clicked')
            #AssetNum = self.ui.Search_Asset_Numbers_Field.text()
            EmployeeNum = self.ui.Search_Employee_ID_Entry_Field.text()
            if(not self.Employee_ID_Check(EmployeeNum)):
                self.qm.critical(self, 'Notice', 'Unknown employee ID')
                ETEK_log.info('Employee ID (' + EmployeeNum + ') does not exist in local database')

            for AssetNum in AssetString:

                #Both the asset and employee ID exist, search and populate table display
                if self.Asset_Check(AssetNum) and self.Employee_ID_Check(EmployeeNum):
                   EmployeeAndAssetList = self.search_fetchAssetAndID(AssetNum, EmployeeNum)
                   if EmployeeAndAssetList:
                       self.search_PopulateTable(EmployeeAndAssetList)
                       ETEK_log.info('Search for Asset (' + AssetNum + ') used by Employee ID (' + EmployeeNum + ') - events found')
                   else:
                       print('No ID found with that Asset')
                       atLeastOneAssetNotFound_Flag = 1
                       #self.qm.information(self, 'Notice', 'No employee ID found with the asset number '+ AssetNum)
                       ETEK_log.info('Search for Asset (' + AssetNum + ') used by Employee ID (' + EmployeeNum + ') - events not found')



               #If the asset doesn't exist, we're searching a list and the employee does exist, then display these prompts
                elif not self.Asset_Check(AssetNum) and (len(AssetString) > 1) and self.Employee_ID_Check(EmployeeNum):
                    self.qm.critical(self, 'Notice', 'Asset number ' + AssetNum + ' does not exist in local database')
                    atLeastOneAssetNotFound_Flag = 1
                    ETEK_log.info('Search for Asset (' + AssetNum + ') used by Employee ID (' + EmployeeNum + ') - Asset not in database')


                #If the asset doesn't exist, the employee does exist, then display this prompt
                elif(not self.Asset_Check(AssetNum) and self.Employee_ID_Check(EmployeeNum)):
                    #self.ui.Search_UI_Message_Prompt.setText('At least one asset not found')
                    self.qm.critical(self, 'Notice','Asset number ' + AssetNum + ' does not exist in local database')
                    ETEK_log.info('Search for Asset (' + AssetNum + ') used by Employee ID (' + EmployeeNum + ') - Asset not in database')

                # If the employee ID does not exist, notify the user, then display this prompt
                elif (not self.Employee_ID_Check(EmployeeNum)):
                    # self.ui.Search_UI_Message_Prompt.setText('Unknown employee ID')
                    print('Unknown employee ID')
                    self.qm.critical(self, 'Notice', 'Employee ID ' + EmployeeNum + ' does not exist in local database')
                    ETEK_log.info('Search for Asset (' + AssetNum + ') used by Employee ID (' + EmployeeNum + ') - Employee ID not in database')

                # If the employee ID does not exist, notify the user, don't search anything then display this prompt
                elif (not self.Asset_Check(AssetNum)):
                    # self.ui.Search_UI_Message_Prompt.setText('Unknown employee ID')
                    print('Unknown employee ID')
                    self.qm.critical(self, 'Notice', 'Asset ID ' + AssetNum + ' does not exist in local database')
                    ETEK_log.info('Search for Asset (' + AssetNum + ') used by Employee ID (' + EmployeeNum + ') - Employee ID and Asset both not in database')


            if(atLeastOneAssetNotFound_Flag == 1):
                self.qm.warning(self, 'Notice', 'At least one asset not found')
        except:
            ETEK_log.error('Error while searching for Assets used by Employee. In function - search_searchAssetandIDButtonClicked')


    def search_searchDateButtonClicked(self):
        try:
            print('Search Tab Search Date Button Clicked')

            dateTimeLowerBound = self.ui.Search_Datetime_From.text()
            dateTimeUpperBound = self.ui.Search_Datetime_To.text()
            EmployeeID = self.ui.Search_Employee_ID_Entry_Field.text()

            #If asset field is not blank, retrieve all asset inputs
            if(self.ui.Search_Asset_Numbers_Field.text() != ''):
                AssetList = self.checkInputAssetFormat(self.checkMultiItemsCommas(self.ui.Search_Asset_Numbers_Field.text()))
            else:
                AssetList = []

            #If the date range is valid, go search for the range,
            #else tell user no events b/w dates and display additional prompts for invalid Employee and asset input
            if self.search_checkDateTimeBounds(dateTimeLowerBound, dateTimeUpperBound):
                DateList = self.search_fetchDateTime(dateTimeLowerBound, dateTimeUpperBound)
                if DateList:
                    self.search_PopulateTable(DateList)
                    ETEK_log.info('Search for Dates between (' + dateTimeLowerBound + ') and (' + dateTimeUpperBound + ') - events found for date range')
            else:
                #self.ui.Search_UI_Message_Prompt.setText('No events found between these dates')
                self.qm.information(self, 'Notice', 'No events found between these dates')
                ETEK_log.info('Search for Dates between (' + dateTimeLowerBound + ') and (' + dateTimeUpperBound + ') - no events found for date range')

                if not self.Employee_ID_Check(EmployeeID) and (EmployeeID != ''):
                    self.qm.critical(self, 'Critical Issue','Employee ID ' + EmployeeID + ' does not exist in the local database')
                    ETEK_log.info('Search for Dates between (' + dateTimeLowerBound + ') and (' + dateTimeUpperBound + ') - Employee  ' + EmployeeID + ' does not exist in database.')

                if len(AssetList) != 0:
                    for Asset in AssetList:
                        if not self.Asset_Check(Asset):
                            self.qm.critical(self, 'Critical Issue','Asset ID ' + Asset + ' does not exist in the local database')
                            ETEK_log.info('Search for Dates between (' + dateTimeLowerBound + ') and (' + dateTimeUpperBound + ') - Asset ' + Asset + ' does not exist in database.')

        except:
            ETEK_log.error('Error while searching for Date range. In function - search_searchDateButtonClicked')





    def search_printPDFButtonClicked(self):
        try:
            print('Search Tab Print Button Clicked')
            #self.ui.Search_UI_Message_Prompt.setText('Printing to PDF...')

            #calling the qt object constantly was long and unwieldy, just call it w and move on
            #w = self.ui.Search_Display_Results_Table

            #Append date & time into filename (admin may do multiple searches + prints over several minutes)
            filepath = self.save_PDF_Filepath()
            if filepath != '':
                today = str(datetime.now().strftime("%B %d, %Y %H %M %S"))
                filename = filepath + "/E-TEK Search Results " + today + ".pdf"
                model = self.ui.Search_Display_Results_Table.model()

                #Below just prints a generic crappy table - modify to make formatting better if we have time later
                printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.PrinterResolution)
                printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
                printer.setPaperSize(QtPrintSupport.QPrinter.Letter)
                printer.setOrientation(QtPrintSupport.QPrinter.Portrait)
                printer.setOutputFileName(filename)

                doc = QtGui.QTextDocument()

                html = """<html>
                <head>
                <style>
                table, th, td {
                  border: 1px solid black;
                  border-collapse: collapse;
                }
                </style>
                </head>"""
                html += "<table><thead>"
                html += "<tr>"
                for c in range(model.columnCount()):
                    html += "<th>{}</th>".format(model.headerData(c, QtCore.Qt.Horizontal))

                html += "</tr></thead>"
                html += "<tbody>"
                for r in range(model.rowCount()):
                    html += "<tr>"
                    for c in range(model.columnCount()):
                        html += "<td>{}</td>".format(model.index(r, c).data() or "")
                    html += "</tr>"
                html += "</tbody></table>"
                doc.setHtml(html)
                doc.setPageSize(QtCore.QSizeF(printer.pageRect().size()))
                doc.print_(printer)

                self.ui.Search_UI_Message_Prompt.setText('')
                self.qm.information(self, 'PDF File Created', 'Successful PDF print!')
            else:
                self.qm.information(self, 'Canceled Print Action', 'PDF print was cancelled')
            ETEK_log.info('Print to PDF Search Results Completed')

        except:
            ETEK_log.error('Error while printing to PDF. In function - search_printPDFButtonClicked')


    def edit_clearButtonClicked(self):
        try:
            print('Edit Tab Clear Button Clicked')
            self.ui.Edit_UI_Message_Prompt.setText('')
            self.ui.Edit_AssignTo_Field.setText('')
            self.ui.Edit_Asset_Field.setText('')
            self.ui.Edit_Update_Status_Dropdown.setCurrentIndex(0)
            self.ui.Edit_UI_Message_Name_From_ID.setText('')
        except:
            ETEK_log.error('Error In function - edit_clearButtonClicked')

    # Searches Asset Table to see if asset even exists, then searches
    # for most recent event regarding that asset and who it's assigned to/what is it's status
    # def edit_searchButtonClicked(self):
    #     try:
    #         print('Edit Tab Search Button Clicked')
    #
    #         #self.ui.Edit_UI_Message_Prompt.setText('Searching...')
    #
    #         #self.edit_clearTableResults()
    #         if self.Asset_Check(self.ui.Edit_Asset_Field.text()):
    #             print('Edit search found the asset!')
    #             #self.ui.Edit_UI_Message_Prompt.setText('Asset Found')
    #             #self.qm.information(self, 'Notice', 'Asset Found!')
    #             #EntryList = self.edit_Asset_Info_Fetch(self.ui.Edit_Asset_Num_Field.text())
    #             #self.edit_AssetSearchedInDatabase = self.ui.Edit_Asset_Field.text()
    #             #self.edit_PopulateTable(EntryList)
    #             AssetState = self.edit_Asset_List_Fetch(self.ui.Edit_Asset_Field.text())
    #             # This updates the edit tab GUI fields w/ relevant info from the Event Log
    #             #Current_Status = AssetState[0][4]
    #             self.ui.Edit_AssignTo_Field.setText(AssetState[0][2])
    #
    #             #Query the name of employee using the asset from the employee table
    #             EmployeeName = self.edit_FetchNameViaID(AssetState[0][2])
    #             if EmployeeName != "":
    #                 self.ui.Edit_UI_Message_Name_From_ID.setText(EmployeeName[0])
    #             else:
    #                 self.ui.Edit_UI_Message_Name_From_ID.setText(EmployeeName)
    #
    #
    #
    #             AssetStatus = AssetState[0][4]
    #             if AssetStatus == '1':
    #                 AssetStatus_Dropdown = 'Checked In'
    #             elif AssetStatus == '2':
    #                 AssetStatus_Dropdown = 'Checked Out'
    #             if AssetStatus == '3':
    #                 AssetStatus_Dropdown = 'In Repair'
    #             elif AssetStatus == '4':
    #                  AssetStatus_Dropdown = 'Retired'
    #             if AssetStatus == '5':
    #                 AssetStatus_Dropdown = 'Broken'
    #             elif AssetStatus == '6':
    #                  AssetStatus_Dropdown = 'New Item'
    #             elif AssetStatus == '7':
    #                 AssetStatus_Dropdown = 'New Employee'
    #             self.ui.Edit_Update_Status_Dropdown.setCurrentText(AssetStatus_Dropdown)
    #         else:
    #             print('Edit search did not find the asset!')
    #             #self.ui.Edit_UI_Message_Prompt.setText('Asset not found')
    #             self.qm.critical(self, 'Invalid Entry', 'Asset ' + self.ui.Edit_Asset_Field.text() + ' does not exist in local database!')
    #     except:
    #         ETEK_log.error('Error In function - edit_searchButtonClicked')


    def edit_FetchNameViaID(self, EmployeeID):
            #This should only ever return one result because the EmployeeID is the primary key of this table
        try:
            check_query = '''SELECT Name FROM [Employee Table] WHERE (EmployeeID =  (?));'''  # '?' is a placeholder
            self.cursor.execute(check_query, str(EmployeeID))
            if self.cursor.fetchone():
                self.cursor.execute(check_query, str(EmployeeID))
                return self.cursor.fetchone()
            else:
                #self.ui.Edit_UI_Message_Prompt.setText('Unknown Employee ID')
                #self.qm.information(self, 'Notice', 'Unknown Employee ID')
                return str("")
        except:
            ETEK_log.error('Error In function - edit_FetchNameViaID')

    def edit_AssignTo_commitSQL(self,edit_Employee,Edit_Asset,AssetStatus_Dropdown):

        insert_event_query = ''' INSERT INTO [Event Log Table] (EmployeeID, AssetID, Status) VALUES(?,?,?);'''
        # Next two lines commit the edits present in the table
        self.cursor.execute(insert_event_query, str(edit_Employee), str(Edit_Asset),
                            str(AssetStatus_Dropdown))
        self.cnxn.commit()

    def edit_UpdateStatus_commitSQL(self, Edit_Asset, AssetStatus_Dropdown):
        insert_event_query = ''' INSERT INTO [Event Log Table] (AssetID, Status) VALUES(?,?);'''
        # Next two lines commit the edits present in the table
        self.cursor.execute(insert_event_query, str(Edit_Asset),
                            str(AssetStatus_Dropdown))
        self.cnxn.commit()

    def edit_commitButtonClicked(self):

        try:
            print('Edit Tab Commit Button Clicked')


            Edit_Asset = self.ui.Edit_Asset_Field.text()
            #If the assign to field is blank, then record the event as the admin logged in
            if self.ui.Edit_AssignTo_Field.text() == '':
               Edit_Employee = self.userLoggedIn
            else:
                Edit_Employee = self.ui.Edit_AssignTo_Field.text()



            #AssetState = self.Asset_Return(self.edit_AssetSearchedInDatabase)
            if (self.ui.Edit_Update_Status_Dropdown.currentText() != '') and self.Employee_ID_Check(Edit_Employee):
                if self.ui.Edit_Update_Status_Dropdown.currentText() == 'Checked In':
                    AssetStatus_Dropdown = '1'
                elif self.ui.Edit_Update_Status_Dropdown.currentText() == 'Checked Out':
                    AssetStatus_Dropdown = '2'
                elif self.ui.Edit_Update_Status_Dropdown.currentText() == 'In Repair':
                    AssetStatus_Dropdown = '3'
                elif self.ui.Edit_Update_Status_Dropdown.currentText() == 'Retired':
                    AssetStatus_Dropdown = '4'
                elif self.ui.Edit_Update_Status_Dropdown.currentText() == 'Broken':
                    AssetStatus_Dropdown = '5'


            #This is a big logical or statement so that we don't get events w/ employee numbers that are associated
            #with assets that are in repair, retire, broken, a new item the introduction of a new employee from the
            # edit tab.
            # Made this into a flag for ease of reference
            invalidEmployeeStatusFlag = (self.ui.Edit_Update_Status_Dropdown.currentText() == '') or (self.ui.Edit_Update_Status_Dropdown.currentText() == 'New Employee') or (self.ui.Edit_Update_Status_Dropdown.currentText() == 'New Item') or (self.ui.Edit_Update_Status_Dropdown.currentText() == 'Broken') or (self.ui.Edit_Update_Status_Dropdown.currentText() == 'Retired') or (self.ui.Edit_Update_Status_Dropdown.currentText() == 'In Repair')

            if (Edit_Asset != ''):
                #This should not commit w/ any employee ID if the status is set to Retired, Broken, In Repair, New Item or New Employee
                #If it's not any of those listed and the Assign To field isn't blank, then commit all three into the database
                if not invalidEmployeeStatusFlag:
                    # Employee field is empty and admin wants to sign this asset out
                    if self.ui.Edit_AssignTo_Field.text() == '':
                        response = self.qm.question(self, 'Input Required',
                                                    'Do you want to check out or check in this asset as your logged in admin employee ID?',
                                                    self.qm.Yes | self.qm.No)
                        if response == self.qm.Yes:
                            Edit_Employee = self.userLoggedIn
                            self.edit_AssignTo_commitSQL(str(Edit_Employee), str(Edit_Asset),str(AssetStatus_Dropdown))

                            self.ui.Edit_UI_Message_Prompt.setText('')
                            EmployeeName = (self.edit_FetchNameViaID(Edit_Employee))
                            self.qm.information(self, 'Edit Confirmation', 'Asset ' + Edit_Asset +' was assigned to '+ EmployeeName[0] + ' (Employee ID: ' + Edit_Employee +') with the status: "' + self.ui.Edit_Update_Status_Dropdown.currentText() +'" (status code ' + AssetStatus_Dropdown +')')
                            ETEK_log.info('Asset Edits Committed to Database')

                            # clear fields after commit
                            self.ui.Edit_AssignTo_Field.setText('')
                            self.ui.Edit_Asset_Field.setText('')
                            self.ui.Edit_Update_Status_Dropdown.setCurrentIndex(0)
                            self.ui.Edit_UI_Message_Name_From_ID.setText('')
                    # Employee field is empty and admin does not want to sign this asset out
                        elif response == self.qm.No:
                            self.qm.warning(self, 'Invalid commit','Please fill in the "Assign To" field if you are not checking an asset in/out')

                    # Employee field is not empty and admin does not want to sign this asset out
                    elif self.ui.Edit_AssignTo_Field.text() != '':
                        Edit_Employee = self.ui.Edit_AssignTo_Field.text()
                        self.edit_AssignTo_commitSQL(str(Edit_Employee), str(Edit_Asset),str(AssetStatus_Dropdown))
                        self.ui.Edit_UI_Message_Prompt.setText('')
                        EmployeeName = (self.edit_FetchNameViaID(Edit_Employee))
                        self.qm.information(self, 'Edit Confirmation',
                                            'Asset ' + Edit_Asset + ' was assigned to ' + EmployeeName[
                                                0] + ' (Employee ID: ' + Edit_Employee + ') with the status: "' + self.ui.Edit_Update_Status_Dropdown.currentText() + '" (status code ' + AssetStatus_Dropdown + ')')
                        ETEK_log.info('Asset Edits Committed to Database')

                # If it's not any of those listed and the Assign To field isn't blank, then commit all three into the
                else:
                    response = self.qm.question(self, 'Input Required', 'Do you want to check out or check in this asset as your logged in admin employee ID?', self.qm.Yes | self.qm.No)
                    if response == self.qm.Yes:
                        if invalidEmployeeStatusFlag:
                            self.qm.warning(self, 'Invalid Status for Assignment', 'Can not assign an asset to an employee with the status ' + self.ui.Edit_Update_Status_Dropdown.currentText() + '\n\nPlease pick either "Checked In" or ""Checked out" if assigning to an employee or yourself')
                        else:
                            self.edit_AssignTo_commitSQL(str(Edit_Employee), str(Edit_Asset), str(AssetStatus_Dropdown))
                            self.ui.Edit_UI_Message_Prompt.setText('')
                            EmployeeName = (self.edit_FetchNameViaID(Edit_Employee))
                            self.qm.information(self, 'Edit Confirmation',
                                                'Asset ' + Edit_Asset + ' was assigned to ' + EmployeeName[
                                                    0] + ' (Employee ID: ' + Edit_Employee + ') with the status: "' + self.ui.Edit_Update_Status_Dropdown.currentText() + '" (status code ' + AssetStatus_Dropdown + ')')
                            ETEK_log.info('Asset Edits Committed to Database w/ admin employee ID')

                            # clear fields after commit
                            self.ui.Edit_AssignTo_Field.setText('')
                            self.ui.Edit_Asset_Field.setText('')
                            self.ui.Edit_Update_Status_Dropdown.setCurrentIndex(0)
                            self.ui.Edit_UI_Message_Name_From_ID.setText('')

                    else:

                        self.edit_UpdateStatus_commitSQL(str(Edit_Asset),str(AssetStatus_Dropdown))
                        self.ui.Edit_UI_Message_Prompt.setText('')
                        self.qm.information(self, 'Edit Confirmation',
                                            'Asset ' + Edit_Asset + ' was updated to being "' + self.ui.Edit_Update_Status_Dropdown.currentText() + '" (status code ' + AssetStatus_Dropdown + ')')
                        ETEK_log.info('Asset Edits Committed to Database as status update')

                        # clear fields after commit
                        self.ui.Edit_AssignTo_Field.setText('')
                        self.ui.Edit_Asset_Field.setText('')
                        self.ui.Edit_Update_Status_Dropdown.setCurrentIndex(0)
                        self.ui.Edit_UI_Message_Name_From_ID.setText('')




            else:

                if(Edit_Asset == ''):
                    self.qm.warning(self, 'Blank asset field',
                                    'Please enter an asset number before pressing the commit edits button')
                elif not self.Employee_ID_Check(Edit_Employee) and self.ui.Edit_Update_Status_Dropdown.currentText() != '':
                    self.qm.critical(self, 'Invalid Commit', 'Employee ID: ' + Edit_Employee +' does not exist in the local database')
                elif (self.ui.Edit_Update_Status_Dropdown.currentText() == '' and self.Employee_ID_Check(Edit_Employee)):
                    print("Please fill status field before committing")
                    #self.ui.Edit_UI_Message_Prompt.setText('Please fill status field')
                    self.qm.critical(self, 'Invalid Commit', 'Please fill status field!')
                elif (self.ui.Edit_Update_Status_Dropdown.currentText() == '' and Edit_Employee == ''):

                    self.qm.critical(self, 'Invalid Commit', 'Please search for asset, make desired changes to employee and status, then press commit!')
        except:
            ETEK_log.error('Error In function - edit_commitButtonClicked')
            print('Threw an exception in edit_commitButtonClicked function')



    def create_clearButtonClicked(self):
        try:
            print('Create Tab Clear Button Clicked')

            # Reset Asset and RFID Filters to empty values
            self.ui.Create_Asset_Num_Field.setText("")
            self.ui.Create_Asset_Description_Field.setText("")
            self.ui.Create_RFID_Tag_Field_3.setText("")
            self.ui.Create_UI_Message_Prompt.setText('')
        except:
            ETEK_log.error('Error In function - create_clearButtonClicked')


    #Edit from RFID text field to RFID scan for entering the tag (maybe change lineEdit field to text display)
    def create_confirmEntryButtonClicked(self):
        try:
            ETEK_log.info('Admin logged in as Employee ID ' + self.userLoggedIn + 'pressed enter button on create tab')
            assetID = self.ui.Create_Asset_Num_Field.text()
            if assetID != '':
                if re.findall(r"\A[E,e][0-9]{7}$|\A[4][0-9]{6}$",assetID):
                    if not self.Asset_Check(assetID):
                        self.create_commitAssetOnly(assetID)
                        self.qm.information(self, 'Asset ID added to local database','The asset ID "' + assetID + '" was commited to the asset table')
                        ETEK_log.info('Admin logged in as Employee ID ' + self.userLoggedIn + 'added the asset ID ' + assetID + ' to the asset table in the local database')
                    else:
                        self.qm.warning(self, 'Asset already exists',
                                        'The asset number entered is already in the Asset Table of the local database')
                        ETEK_log.info('Admin logged in as Employee ID ' + self.userLoggedIn + ' attempted to add an asset that already exists in the asset table')
                else:
                    ETEK_log.info(
                        'Admin logged in as Employee ID ' + self.userLoggedIn + 'entered an incomplete asset number - not in "Exxxxxxx" or "4xxxxxx"')
                    self.qm.warning(self, 'Incomplete asset number',
                                    'Please enter a valid asset # into the field before pressing enter\n\n Two accepted formats are: "Exxxxxxx" and "4xxxxxx"\n\nWhere x is a numerical digit')
            else:
                ETEK_log.info(
                    'Admin logged in as Employee ID ' + self.userLoggedIn + 'pressed enter button with nothing in asset field')
                self.qm.warning(self,'Empty asset field','Please enter text into the asset # field before pressing enter')
            self.ui.Create_Asset_Num_Field.setText('')
        except:
            ETEK_log.error('Error In function - create_confirmEntryButtonClicked')
            self.qm.warning(self, 'Error: exception thrown','An exception was thrown in the create_confirmEntryButtonClicked function, see ETEK.log file for more details')
            self.ui.Create_Asset_Num_Field.setText('')


    def create_commitAssetOnly(self,assetID):
        insert_event_query = ''' INSERT INTO [Event Log Table] (AssetID, Status) VALUES(?,?);'''
        self.cursor.execute(insert_event_query, str(assetID),str('6'))
        self.cnxn.commit()

        insert_event_query = ''' INSERT INTO [Asset Table] (AssetID) VALUES(?);'''
        self.cursor.execute(insert_event_query, str(assetID))
        self.cnxn.commit()

    def save_PDF_Filepath(self):
        try:

            file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

            return file
        except:
            ETEK_log.error('Error In function - save_PDF_Filepath')

    def find_files(self):
        try:

            #self.scrollqm.buttonClicked()
            f = QFileDialog.getOpenFileName(self, "Open .xlsx File","/home",".xlsx files (*.xlsx)")

            return f[0]
        except:
            ETEK_log.error('Error In function - find_files')


    def Import_ImportAssets_ButtonClicked(self):
        try:
            Import_log.info('User:(' + self.userLoggedIn + ') - Clicked Import Assets Button')
            print('Import Tab ImportAssets Button Clicked')
            self.ui.Create_UI_Message_Prompt.setText('')
            name = "AssetList.xlsx"
            assetFile = self.find_files()


            if(assetFile != ''):
                dataAsset = pd.read_excel(assetFile, engine='openpyxl', dtype = str)

                df = pd.DataFrame(dataAsset, columns=['Asset ID', 'RFID Tag'])

                if dataAsset.columns[0] == 'Asset ID' and dataAsset.columns[1] == 'RFID Tag':
                    if not all (np.where(pd.isnull(df))):
                        count = 0
                        for index in df["Asset ID"]:
                                # Regex for getting asset numbers that start w/ 4,E or e and have 7 digits (numerical) after
                                # If the number is the correct format, then start processing it
                            if re.findall(r"\A[E,e][0-9]{7}$|\A[4][0-9]{6}$",index):
                                # If the string begins w/ lower case e, then replace it with an E
                                if re.findall(r"\be", index):
                                        index = str.capitalize(index)
                                print(index)

                            else:
                                df.drop([count], inplace = True)
                                print("Wrong format in Asset field")
                                Import_log.info('Asset: (' + index + ") in wrong format, Asset not imported")
                            count = count +1

                        df = df.reset_index(drop=True)
                        self.import_checkAssetsOrEmployeesToSQL(df)
                       # self.ui.Create_UI_Message_Prompt.setText('Import Successful!')
                        self.qm.information(self, 'Notice', 'New asset(s) imported successfully!')
                        ETEK_log.info('New Assets imported successfully through .xlsx file. Check Import Log for details.')

                    else:
                        print('Please reformat excel into 2 columns "AssetID" and "RFID Tag" with no blank cells')
                        #self.ui.Create_UI_Message_Prompt.setText('Import failed: blank cells in file')
                        self.qm.critical(self, 'Critical Issue', 'Import failed: please reformat .xlsx file into 2 columns "AssetID" and "RFID Tag" with no blank cells')
                else:
                    print('Please reformat excel into 2 columns "AssetID" and "Type"')
                    #self.ui.Create_UI_Message_Prompt.setText('Import failed: check column headers')
                    self.qm.critical(self, 'Critical Issue','Import failed: please reformat .xlsx file into 2 columns "AssetID" and "RFID Tag" with no blank cells')
            else:
                ETEK_log.info('Admin logged in as Employee ID ' + self.userLoggedIn + ' clicked import assets button but did not select a .xlsx file from file browser prompt')
        except:
            ETEK_log.error('Error In function - Import_ImportAssets_ButtonClicked')
            self.qm.critical(self, 'Critical Issue', 'Asset import failed: An exception was thrown')

    def Import_ImportEmployees_ButtonClicked(self):
        try:
            Import_log.info('User:(' + self.userLoggedIn + ') - Clicked Import Employees Button')
            print('Import Tab ImportEmployees Button Clicked')
            self.ui.Create_UI_Message_Prompt.setText('')
            employeeFile = self.find_files()

            if (employeeFile != False):


                dataEmployee = pd.read_excel(employeeFile, engine = 'openpyxl', dtype = str)
                df = pd.DataFrame(dataEmployee, columns=['Name', 'Employee ID'])

                if dataEmployee.columns[0] == 'Name' and dataEmployee.columns[1] == 'Employee ID':
                    if not all (np.where(pd.isnull(df))):
                        self.import_checkAssetsOrEmployeesToSQL(df)
                        #self.ui.Create_UI_Message_Prompt.setText('Import Successful!')

                        ETEK_log.info('New Employees imported successfully through .xlsx file. Check Import log for details')
                        self.qm.information(self, 'Notice', 'New employee(s) imported successfully!')
                    else:
                        print('Please reformat excel into 2 columns "Name" and "Employee ID" with no empty cells')
                        #self.ui.Create_UI_Message_Prompt.setText('Import failed: blank cells in file')
                        self.qm.critical(self, 'Critical Issue','Import failed: please reformat .xlsx file into 2 columns "Name" and "Employee ID" with no blank cells')
                else:
                    print('Please reformat excel into 2 columns "Name" and "EmployeeID"')
                    #self.ui.Create_UI_Message_Prompt.setText('Import failed: bad column header(s)')
                    self.qm.critical(self, 'Critical Issue','Import failed: please reformat .xlsx file into 2 columns "Name" and "Employee ID" with no blank cells')
        except:
            ETEK_log.error('Error In function - Import_ImportEmployees_ButtonClicked')
            self.qm.critical(self, 'Critical Issue', 'Employee import failed: An exception was thrown')

    # ****************************************End Class Methods for Tab Button(s)*****************************
    # ****************************************Class Methods for Running Queries*******************************
    #Searches for Asset ID in RFID Table, returns true if it exists else returns false
    def AssetRFID_Check(self, AssetNum):
        check_query = '''SELECT TOP 1 * FROM [RFID Table] WHERE (AssetID =  (?));'''  # '?' is a placeholder
        self.cursor.execute(check_query, str(AssetNum))
        if self.cursor.fetchone():
            #self.cursor.execute(check_query, str(AssetNum))
            return True
        else:
            return False

    def RFID_Check(self, RFIDTag):
        check_query = '''SELECT TOP 1 * FROM [RFID Table] WHERE (TagID =  (?));'''  # '?' is a placeholder
        self.cursor.execute(check_query, str(RFIDTag))
        if self.cursor.fetchone():
            # self.cursor.execute(check_query, str(RFIDTag))
            return True
        else:
            return False

    def Employee_ID_Check(self, input):
        check_query = '''SELECT TOP 1 * FROM [Employee Table] WHERE EmployeeID = (?);'''  # '?' is a placeholder
        self.cursor.execute(check_query, str(input))
        if self.cursor.fetchone():
            print('This ID exists!')
            return True
        else:
            return False

    def Employee_ID_FindAssets(self, input):
        check_query = '''SELECT * FROM [Event Log Table] WHERE (EmployeeID =  (?));'''  # '?' is a placeholder
        self.cursor.execute(check_query, str(input))
        if self.cursor.fetchone():
            print('This ID has used assets!')
            self.cursor.execute(check_query, str(input))
            return self.cursor.fetchall()
        else:
            print('This ID has not used assets!')
            return False
    def search_clearTableResults(self):
        self.ui.Search_Display_Results_Table.setRowCount(0)

    def edit_clearTableResults(self):
        self.ui.Edit_Display_Results_Table.setRowCount(0)


    def search_checkFieldInputs(self):
        try:
            #Clear table and UI prompt everytime you run a search
            self.ui.Search_UI_Message_Prompt.setText('')
            self.search_clearTableResults()

            #For ease of development, we're writing all the fields and boolean checks into local method variables
            #Hopefully this is less of a headache to look at
            YesDateRangeFlag = (self.ui.Search_Datetime_From.text() != "Jan 1 2021") or (self.ui.Search_Datetime_To.text() != "Jan 1 2021")
            NoDateRangeFlag = (self.ui.Search_Datetime_From.text() == "Jan 1 2021") and (self.ui.Search_Datetime_To.text() == "Jan 1 2021")
            SearchMonthFlag = (self.ui.Search_Month_By_Month_Search_Dropdown.currentText() !=  "")
            EmployeeIdField = self.ui.Search_Employee_ID_Entry_Field.text()
            AssetField = self.ui.Search_Asset_Numbers_Field.text()

            #Seperate the field entry into a list
            AssetList = self.checkMultiItemsCommas(AssetField)


            #First captialize each entry that starts with an 'e' in AssetList before doing a comparison




            #Check if the list of asset #'s entered is the same as the list of valid asset #'s that went thru regex
            #If it is the same, then nothing happens, else the user is notified of bad input and search looks
            #for valid inputs only
            if AssetList != self.checkInputAssetFormat(AssetList):
                #If it's not valid, then notify user and go ahead with search for the valid asset #'s
                self.qm.warning(self, 'Notice', 'At least one invalid asset number was entered, please check field input')

                AssetList = self.checkInputAssetFormat(self.checkMultiItemsCommas(AssetField))


            #Prevents redundancy in search
            if(YesDateRangeFlag and SearchMonthFlag):

                #self.ui.Search_UI_Message_Prompt.setText('Enter month OR date range, not both!')
                self.qm.critical(self, 'Critical Issue', 'Enter month OR date range, not both!')

            #This also checks for whether we're searching employeeID's or Asset ID's in the SQL query
            elif(SearchMonthFlag):

                self.search_Find_Months()

            # This also checks for whether we're searching employeeID's or Asset ID's in the SQL query
            elif(YesDateRangeFlag):
                self.search_searchDateButtonClicked()


            #If no date or month specified then we're just searching for combinations of assets and employees
            else:
                if EmployeeIdField and not AssetField:
                    self.search_searchIDButtonClicked()
                elif AssetField and not EmployeeIdField:
                    self.search_searchAssetButtonClicked(AssetList)
                elif AssetField and EmployeeIdField:
                    self.search_searchAssetandIDButtonClicked(AssetList)


        except:
            ETEK_log.error('Error while searching. In function - search_checkFieldInputs')

    #This method uses Regex to separate a string of #'s separated by commas into a list that we can put into
    #our search and populate table methods.  This also ignores whitespace to allow more robust valid inputs
    #If you're feeding this an asset or list of assets, then give it a second argument = 1
    def checkMultiItemsCommas(self, StringWithCommas):

        CapitalCheckList = []
        RawAssetList = (re.findall(r'[^,\s]+', StringWithCommas))

        for index in RawAssetList:
            # If the string begins w/ lower case e, then replace it with an E
            if index == '':
                print("Entered a double comma")
            elif re.findall(r"\be", index):
                CapitalCheckList.append(str.capitalize(index))
            else:
                CapitalCheckList.append(str(index))
        return CapitalCheckList



    #Checks the assets specified to see if it's a valid format
    #No UI messages done here because we want to use this function for every part of admin
    def checkInputAssetFormat(self,RawAssetList):

        #Initialize empty list to append valid entries into
        ProcessedAssetList = []

        #If the list is empty, do nothing, else start processing for valid entries
        #Below formats known as of March 1, 2021
        #Two asset# formats existing:  (1) start with 4 for 7 digit asset –  (2)  starts with E and then 7 digits
        if not RawAssetList:
            print('Nothing in the list')
        else:
            for index in RawAssetList:
                #Regex for getting asset numbers that start w/ 4,E or e and have 7 digits (numerical) after
                #If the number is the correct format, then start processing it
                if re.findall(r"\A[E,e][0-9]{7}$|\A[4][0-9]{6}$",index):
                    #If the string begins w/ lower case e, then replace it with an E
                    if re.findall(r"\be",index):
                        index = str.capitalize(index)
                    print(index)
                    ProcessedAssetList.append(index)
                else:
                    print("Wrong format in Asset field")
                    #self.ui.Search_UI_Message_Prompt.setText('At least one invalid asset#')
                    #self.qm.warning(self, 'Notice', 'At least one invalid asset number was entered, please check field input')

        #return all assets that have the correct format
        return ProcessedAssetList





                #\print("Begins w/ 4 w/ 7 digits afterwards")


    def search_Find_Months(self):
        try:
            MonthList = self.search_FindMonthsSQLQuery()
            if MonthList:
                self.search_PopulateTable(MonthList)
                ETEK_log.info('Search by Specific Month - events found')
            else:
                #self.ui.Search_UI_Message_Prompt.setText('No events found for that month')
                #self.qm.information(self, 'Notice', 'No events found for that month')
                ETEK_log.info('Search by Specific Month - no events found')
        except:
            ETEK_log.error('Error while searching by Month. In function - search_Find_Months ')

    def search_FindMonthsSQLQuery(self):
        Month = self.ui.Search_Month_By_Month_Search_Dropdown.currentText()

        EmployeeID = self.ui.Search_Employee_ID_Entry_Field.text()

        AssetList = self.checkMultiItemsCommas(self.ui.Search_Asset_Numbers_Field.text())

        QueryList = [] #empty list for appending queries

        #Translation Table
        if Month == 'Jan':
            MonthSearch = '01'
        elif Month == 'Feb':
            MonthSearch = '02'
        elif Month == 'Mar':
            MonthSearch = '03'
        elif Month == 'Apr':
            MonthSearch = '04'
        elif Month == 'May':
            MonthSearch = '05'
        elif Month == 'Jun':
            MonthSearch = '06'
        elif Month == 'Jul':
            MonthSearch = '07'
        elif Month == 'Aug':
            MonthSearch = '08'
        elif Month == 'Sep':
            MonthSearch = '09'
        elif Month == 'Oct':
            MonthSearch = '10'
        elif Month == 'Nov':
            MonthSearch = '11'
        elif Month == 'Dec':
            MonthSearch = '12'


        #if AssetList is empty (not searching for assets)
        if not AssetList:
            # Searching for month only
            if(Month and not EmployeeID):
                check_query = '''SELECT * FROM [Event Log Table] WHERE (MONTH(Timestamp) =  (?));'''  # '?' is a placeholder
                self.cursor.execute(check_query, str(MonthSearch))
                if self.cursor.fetchone():
                    self.cursor.execute(check_query, str(MonthSearch))
                    print("Found items for the specified month!")
                    return self.cursor.fetchall()
                else:
                    print("No items found for the specified month")
                    #self.ui.Search_UI_Message_Prompt.setText('No items found for this month')
                    self.qm.information(self, 'Notice', 'No events found for this month')
                    return False
            # Searching for month and EmployeeID
            elif (Month and EmployeeID):
                check_query = '''SELECT * FROM [Event Log Table] WHERE (MONTH(Timestamp) =  (?) AND EmployeeID = (?));'''  # '?' is a placeholder
                self.cursor.execute(check_query, str(MonthSearch), str(EmployeeID))
                if self.cursor.fetchone():
                    self.cursor.execute(check_query, str(MonthSearch), str(EmployeeID))
                    print("Found items for the specified month!")
                    return self.cursor.fetchall()
                else:
                    print("No items found for the specified month")
                    #self.ui.Search_UI_Message_Prompt.setText('No items found for this month')
                    if(self.Employee_ID_Check(EmployeeID)):
                        self.qm.information(self, 'Notice', 'No events with this employee ID found for this month')
                    else:
                        self.qm.critical(self, 'Notice', 'Employee ID ' + EmployeeID + ' does not exist in the local database')

                    return False

        for Asset in AssetList:
            #Searching for month and Asset
            if(Month and Asset and not EmployeeID):
                check_query = '''SELECT * FROM [Event Log Table] WHERE (MONTH(Timestamp) =  (?) AND AssetID = (?));'''  # '?' is a placeholder
                self.cursor.execute(check_query, str(MonthSearch),str(Asset))
                if self.cursor.fetchone():
                    self.cursor.execute(check_query, str(MonthSearch),str(Asset))
                    print("Found items for the specified month!")

                    for Event in self.cursor.fetchall():
                        QueryList.append(Event)
                   # return self.cursor.fetchall()
                else:
                    print("No items found for the specified month")
                    #self.ui.Search_UI_Message_Prompt.setText('At least one asset not found')

                    if(not self.Asset_Check(Asset)):
                        self.qm.critical(self, 'Critical Issue','Asset number ' + Asset + ' does not exist in the local database')



                    #return False



            # Searching for month and EmployeeID and Asset
            elif (Month and Asset and EmployeeID):
                check_query = '''SELECT * FROM [Event Log Table] WHERE (MONTH(Timestamp) =  (?) AND EmployeeID = (?) AND AssetID = (?));'''  # '?' is a placeholder
                self.cursor.execute(check_query, str(MonthSearch),str(EmployeeID),str(Asset))
                if self.cursor.fetchone():
                    self.cursor.execute(check_query, str(MonthSearch),str(EmployeeID),str(Asset))
                    print("Found items for the specified month!")

                    for Event in self.cursor.fetchall():
                        QueryList.append(Event)

                else:
                    print("No items found for the specified month")
                    #self.ui.Search_UI_Message_Prompt.setText('At least one asset not found')

                    if (not self.Asset_Check(Asset)):
                        self.qm.critical(self, 'Critical Issue','Asset number ' + Asset + ' does not exist in the local database')

                    if ( not self.Employee_ID_Check(EmployeeID)):
                        self.qm.critical(self, 'Notice','Employee ID ' + EmployeeID + ' does not exist in the local database')

                    #return False
        # If the list is empty (queries returned no results whatsoever) then return false
        if not (QueryList):
            self.qm.information(self, 'Notice', 'No events found for this search criteria')
            return False
        else:
            return QueryList


    def search_checkDateTimeBounds(self,LowerBound,UpperBound):
        check_query = '''SELECT * FROM [Event Log Table] WHERE (Timestamp >=  (?)) AND (Timestamp <=  (?));'''  # '?' is a placeholder
        self.cursor.execute(check_query, str(LowerBound), str(UpperBound))
        if self.cursor.fetchone():
            #self.cursor.execute(check_query, str(LowerBound), str(UpperBound))
            print("Found items between these times")
            return True
        else:
            print("No items found between these times")
            return False

    def search_fetchDateTime(self,LowerBound,UpperBound):
        #Asset = self.ui.Search_Asset_Numbers_Field.text()
        EmployeeID = self.ui.Search_Employee_ID_Entry_Field.text()
        AssetList = self.checkMultiItemsCommas(self.ui.Search_Asset_Numbers_Field.text())


        QueryList = [] #Initialize empty list to store all query results

        #Just doing a date range search
        if(not AssetList):
            if(not EmployeeID):

                check_query = '''SELECT * FROM [Event Log Table] WHERE (Timestamp >=  (?)) AND (Timestamp <=  (?));'''  # '?' is a placeholder
                self.cursor.execute(check_query, str(LowerBound), str(UpperBound))
                if self.cursor.fetchone():
                    self.cursor.execute(check_query, str(LowerBound), str(UpperBound))

                    #not searching for multiple assets, just return this list
                    return self.cursor.fetchall()
                    #QueryList.append(self.cursor.fetchall())
                else:
                    self.qm.warning(self, 'Notice','No events found between the specified dates')
                    return False

            # Searching for Employee ID's within a date range
            elif(EmployeeID):
                check_query = '''SELECT * FROM [Event Log Table] WHERE (Timestamp >=  (?) AND Timestamp <=  (?) AND EmployeeID = (?));'''  # '?' is a placeholder
                self.cursor.execute(check_query, str(LowerBound), str(UpperBound), str(EmployeeID))
                if self.cursor.fetchone():
                    self.cursor.execute(check_query, str(LowerBound), str(UpperBound), str(EmployeeID))

                    # not searching for multiple assets, just return this list
                    return self.cursor.fetchall()
                    # QueryList.append(self.cursor.fetchall())
                else:
                    if(self.Employee_ID_Check(EmployeeID)):
                        self.qm.warning(self, 'Notice', 'Employee ID ' + EmployeeID + ' has no associated events found between the specified dates')
                    else:
                        self.qm.critical(self, 'Critical Issue','Employee ID ' + EmployeeID + ' does not exist in local database')
                    return False
        else:

            for Asset in AssetList:
                #Searching for assets within a date range
                if(Asset and not EmployeeID):
                    check_query = '''SELECT * FROM [Event Log Table] WHERE (Timestamp >=  (?) AND Timestamp <=  (?) AND AssetID = (?));'''  # '?' is a placeholder
                    self.cursor.execute(check_query, str(LowerBound), str(UpperBound),str(Asset))
                    if self.cursor.fetchone():
                        self.cursor.execute(check_query, str(LowerBound), str(UpperBound),str(Asset))
                        tmp = self.cursor.fetchall()
                        #return self.cursor.fetchall()
                        for Event in tmp:
                            QueryList.append(Event)


                    else:
                        #self.ui.Search_UI_Message_Prompt.setText('At least one asset not found')
                        if self.Asset_Check(Asset):
                            self.qm.warning(self, 'Notice', 'Asset number ' + Asset + ' has no associated events found between the specified dates')
                        else:
                            self.qm.critical(self, 'Critical Issue','Asset number ' + Asset + ' does not exist in the local database')
                        #return False



                # Searching for assets and employeeID within a date range
                elif (Asset and EmployeeID):
                    check_query = '''SELECT * FROM [Event Log Table] WHERE (Timestamp >=  (?) AND Timestamp <=  (?) AND EmployeeID = (?) AND AssetID = (?));'''  # '?' is a placeholder
                    self.cursor.execute(check_query, str(LowerBound), str(UpperBound),str(EmployeeID),str(Asset))
                    if self.cursor.fetchone():
                        self.cursor.execute(check_query, str(LowerBound), str(UpperBound),str(EmployeeID),str(Asset))

                        #return self.cursor.fetchall()
                        for Event in self.cursor.fetchall():
                            QueryList.append(Event)
                    else:
                        #self.ui.Search_UI_Message_Prompt.setText('At least one asset not found')

                        #if the asset exists, notify that employee ID has not used it, else say that it doesn't exist
                        if (not self.Employee_ID_Check(EmployeeID)):
                            self.qm.critical(self, 'Critical Issue','Employee ID ' + EmployeeID + ' does not exist in local database')

                        if(self.Asset_Check(Asset)):
                            self.qm.information(self, 'Notice', 'Employee ID ' + EmployeeID + ' has not used asset number ' + Asset + ' between the specified dates')
                        else:
                            self.qm.critical(self, 'Critical Issue','Asset number ' + Asset + ' does not exist in the local database')

                        if (self.Employee_ID_Check(EmployeeID) and self.Asset_Check(Asset)):
                            self.qm.warning(self, 'Notice','Employee ID ' + EmployeeID + ' has no associated events found between the specified dates')

                        #return False
            #If the list is empty (queries returned no results whatsoever) then return false
            if not(QueryList):
                return False
                self.qm.information(self, 'Notice','No events found between the specified dates for these Asset(s) and Employee ID')
            else:

                return QueryList






    def edit_PopulateTable(self, EntryList):
        #EmployeeAssetList = self.Employee_ID_FindAssets(EmployeeNum)

        print(EntryList)

        for i in range(len(EntryList)):
            # Create a row
            lastrow = self.ui.Edit_Display_Results_Table.rowCount()
            self.ui.Edit_Display_Results_Table.insertRow(lastrow)

            # Show items on row in interface
            self.ui.Edit_Display_Results_Table.setItem(lastrow, 0, QTableWidgetItem(EntryList[i][2]))
            self.ui.Edit_Display_Results_Table.setItem(lastrow, 1, QTableWidgetItem(EntryList[i][1]))
            self.ui.Edit_Display_Results_Table.setItem(lastrow, 2, QTableWidgetItem(str(EntryList[i][0])))
            self.ui.Edit_Display_Results_Table.setItem(lastrow, 4, QTableWidgetItem(str(EntryList[i][3])))

    def search_PopulateTable(self, EntryList):
        try:
            #EmployeeAssetList = self.Employee_ID_FindAssets(EmployeeNum)
            print(EntryList)



            for i in range(len(EntryList)):
                # Create a row
                lastrow = self.ui.Search_Display_Results_Table.rowCount()
                self.ui.Search_Display_Results_Table.insertRow(lastrow)

                AssetStatus = EntryList[i][3]
                if AssetStatus == '1':
                    AssetStatus_Words = 'Checked In'
                elif AssetStatus == '2':
                    AssetStatus_Words = 'Checked Out'
                if AssetStatus == '3':
                    AssetStatus_Words = 'In Repair'
                elif AssetStatus == '4':
                    AssetStatus_Words = 'Retired'
                if AssetStatus == '5':
                    AssetStatus_Words = 'Broken'


                # Show items on row in interface
                self.ui.Search_Display_Results_Table.setItem(lastrow, 0, QTableWidgetItem(EntryList[i][2]))
                self.ui.Search_Display_Results_Table.setItem(lastrow, 1, QTableWidgetItem(EntryList[i][1]))
                self.ui.Search_Display_Results_Table.setItem(lastrow, 3, QTableWidgetItem(str(EntryList[i][0])))
                self.ui.Search_Display_Results_Table.setItem(lastrow, 2, QTableWidgetItem(str(AssetStatus_Words)))
        except:
            self.qm.critical(self, 'Notice', 'An exception was thrown while populating the search tab table')

    #Searchs for a list of assets specified by lower and upper bound of asset #'s
    #returns list within and including bounds

    #If it can fetch a query from the Asset Table, then it will return true, else it returns false
    #For checking if the asset number already exists in the database
    def Asset_Check(self, AssetNum):
        check_query = '''SELECT TOP 1 * FROM [Asset Table] WHERE (AssetID =  (?));'''  # '?' is a placeholder
        self.cursor.execute(check_query, str(AssetNum))

        if self.cursor.fetchone():
            self.cursor.execute(check_query, str(AssetNum))
            return True
        else:

            return False



    def edit_Asset_Info_Fetch(self, AssetNum):
        check_query = '''SELECT * FROM [Event Log Table] WHERE (AssetID =  (?));'''  # '?' is a placeholder
        self.cursor.execute(check_query, str(AssetNum))
        if self.cursor.fetchone():
            self.cursor.execute(check_query, str(AssetNum))
            return self.cursor.fetchall()
        else:
            return False

    def Asset_List_Fetch(self, AssetNum):
        check_query = '''SELECT * FROM [Event Log Table] WHERE (AssetID =  (?));'''  # '?' is a placeholder
        self.cursor.execute(check_query, str(AssetNum))
        if self.cursor.fetchone():
            self.cursor.execute(check_query, str(AssetNum))
            return self.cursor.fetchall()
        else:
            return False

    def edit_Asset_List_Fetch(self, AssetNum):
        check_query = '''SELECT top 1 * FROM [Event Log Table] WHERE (AssetID =  (?)) ORDER BY Timestamp DESC;'''  # '?' is a placeholder
        self.cursor.execute(check_query, str(AssetNum))
        if self.cursor.fetchone():
            self.cursor.execute(check_query, str(AssetNum))
            return self.cursor.fetchall()
        else:
            return False

    def search_fetchAssetAndID(self,Asset,ID):
        if self.Employee_ID_Check(ID) and self.Asset_Check(Asset):
            print('Both the asset and employee ID are valid!')
            #QUESTION: Do we want to return all entries w/ the asset ID OR the Employee ID or should it be an AND statement?
            check_query = '''SELECT * FROM [Event Log Table] WHERE (AssetID = (?) AND EmployeeID = (?));'''  # '?' is a placeholder
            self.cursor.execute(check_query, str(Asset),str(ID))
            if self.cursor.fetchone():
                print('This employee has used the specified asset')
                self.cursor.execute(check_query, str(Asset),str(ID))
                return self.cursor.fetchall()
            else:
                print('This employee has not used the specified asset')
                #self.ui.Search_UI_Message_Prompt.setText('This asset not used by employee')
                self.qm.information(self, 'Notice', 'This asset: ' + Asset + ' was not used by employee ID ' + ID)
                return False

    #Check what dataset we're dealing with and whether it already exists or not
    #
    def import_checkAssetsOrEmployeesToSQL(self,df):
        importType = None

        #Clear these lists for initial and subsequent runs
        self.import_EmployeeIDList.clear()
        self.import_EmployeeNameList.clear()
        self.import_AssetList.clear()
        self.import_EmployeeIDList_AlreadyExisting.clear()


        #Look at first column in Excel table to determine what data we're working with here
        for col in df.columns:
            if col == "Name":
                importType = "Employees"
                break
            elif col == "Asset ID":
                importType = "Assets"
                break


        #if we're importing employees, populate lists for SQL queries and importing into SQL
        if importType == "Employees":
            for row in range(len(df.index)):
                #if the employee ID already exists, it won't be imported to the lists
                if not self.Employee_ID_Check(str(df.at[row, 'Employee ID'])):
                    self.import_EmployeeIDList.append(str(df.at[row, 'Employee ID']))
                    self.import_EmployeeNameList.append(str(df.at[row, 'Name']))

                    #Commit employee ID to Event log as a new addition (code 104) "10-4 good buddy"
                    self.import_commitEmployeesToSQL(str(df.at[row, 'Employee ID']),str(df.at[row, 'Name']))
                    # NOTE: We should have a GUI notification that shows the import was sucessful
                    #self.ui.Create_UI_Message_Prompt.setText('Employee(s) imported')



                #NOTE: We should have a case where it notifies you on the GUI if you're trying to enter data that already exists and what entries would be duplicates
                else:
                    # self.import_EmployeeIDList_AlreadyExisting.append(str(df.at[row, 'Employee ID']))
                    print("The employee ID: "+ str(df.at[row, 'Employee ID']) +" already exists in the database")
                    Import_log.info('Employee: ' + str(df.at[row, 'Employee ID']) + " already exists in the database, Employee not imported")
            # if(len(self.import_EmployeeIDList_AlreadyExisting) > 0):
            #     # initialize an empty string
            #     str1 = ""
            #
            #     # traverse in the string
            #     for ele in self.import_EmployeeIDList_AlreadyExisting:
            #         str1 += (ele + ', ')
            # self.qm.warning(self, 'Employee numbers already existing not imported ' + str(str1))
        # if we're importing assets, populate lists for SQL queries and importing into SQL
        if importType == "Assets":
            for row in range(len(df.index)):

                # if the asset ID already exists, it won't be imported to the lists or commited to SQL
                if not self.Asset_Check(str(df.at[row, 'Asset ID'])):
                    self.import_AssetList.append(df.at[row, 'Asset ID'])
                    self.import_AssetList.append(str(df.at[row, 'RFID Tag']))

                    #Commit employee ID to Event log as a new addition (code 42) "The answer to everything"
                    self.import_commitAssetsToSQL(str(df.at[row, 'Asset ID']),str(df.at[row, 'RFID Tag']))
                    #self.ui.Create_UI_Message_Prompt.setText('Asset(s) imported')
                    #self.qm.information(self, 'Notice', 'New asset(s) imported successfully!')
                # NOTE: We should have a case where it notifies you on the GUI if you're trying to enter data that already exists and what entries would be duplicates
                else:
                    print("The Asset Number: "+ str(df.at[row, 'Asset ID']) +" already exists in the database")
                    Import_log.info('Asset: ' + str(df.at[row, 'Asset ID']) +" already exists in the database, asset not imported")


        # print(self.import_EmployeeIDList)
        # print(self.import_EmployeeNameList)
        # print(self.import_AssetList)


    #New employee imported appends
    def import_commitEmployeesToSQL(self, EmployeeID, EmployeeName):
        insert_event_query = ''' INSERT INTO [Employee Table] (EmployeeID, Name) VALUES(?,?);'''
        # Next two lines commit the edits present in the table
        self.cursor.execute(insert_event_query, str(EmployeeID), str(EmployeeName))
        self.cnxn.commit()


    # New asset imported appends with status #6
    def import_commitAssetsToSQL(self, AssetID, RFID_Tag):
        insert_event_query = ''' INSERT INTO [Event Log Table] (AssetID, Status) VALUES(?,?);'''
        # Next two lines commit the edits present in the table
        self.cursor.execute(insert_event_query, str(AssetID), '1')

        insert_event_query = ''' INSERT INTO [Asset Table] (AssetID) VALUES(?);'''
        # Next two lines commit the edits present in the table
        self.cursor.execute(insert_event_query, str(AssetID))

        insert_event_query = ''' INSERT INTO [RFID Table] (TagID, AssetID) VALUES(?,?);'''
        # Next two lines commit the edits present in the table
        self.cursor.execute(insert_event_query, str(RFID_Tag),str(AssetID))



        self.cnxn.commit()

    def AssignTag_clearButtonClicked(self):
        try:
            self.ui.AssignTag_Asset_Num_Field.setText('')
            self.ui.AssignTag_RFID_Tag_Field.setText('')
        except:
            self.qm.critical(self, 'Error', 'An exception was thrown in AssignTag_clearButtonClicked function')

    def AssignTag_removeButtonClicked(self):
        try:
            AssetID = self.ui.AssignTag_Asset_Num_Field.text()

            if not (AssetID == ''):
                # Asset does not exist
                if self.Asset_Check(AssetID):
                    #The asset exists in the RFID table already (it has a tag assigned already)
                    if self.RFIDTable_AssetCheck(AssetID)[0]:
                        RFID_Tag = self.RFIDTable_AssetCheck(AssetID)[1][0]
                        response = self.qm.question(self, 'Input Required',
                                                    'The asset ID " ' + AssetID + '"has the RFID tag "' +
                                                    self.RFIDTable_AssetCheck(AssetID)[1][0] + '" associated with it\n\n Please confirm that you want to remove this RFID tag association from this asset ID,',
                                                    self.qm.Yes | self.qm.No)
                        if response == self.qm.Yes:
                            self.RFIDTable_RemoveRow(AssetID)
                            self.qm.information(self, 'RFID Tag Removal Successful',
                                                'The removal of RFID tag "' + RFID_Tag + ' from asset ID "' + AssetID + '" was sucessful!')
                            ETEK_log.info('Admin logged in as Employee ID ' + self.userLoggedIn + 'removed RFID Tag "' + RFID_Tag + '" from the asset "' + AssetID +'"')

                        else:
                            self.qm.information(self, 'RFID Tag Removal Cancelled',
                                            'The removal of an RFID tag from an asset ID was cancelled')
                            ETEK_log.info('Admin logged in as Employee ID ' + self.userLoggedIn + ' selected "No" on confirmation prompt to remove RFID tag')
                    else:
                        self.qm.warning(self, 'No RFID tag found for asset',
                                            'There is no RFID tag associated with this asset ID\n\nRemoval of RFID tag from asset ID cancelled')
                        ETEK_log.info(
                            'Admin logged in as Employee ID ' + self.userLoggedIn + ' attempted to remove RFID tag from asset with no associated RFID tag')
                else:
                    self.qm.critical(self, 'Asset does not exist','This asset does not exist in the asset table of the local database')
                    ETEK_log.info(
                        'Admin logged in as Employee ID ' + self.userLoggedIn + ' attempted to remove RFID tag from asset that does not exist in database')
            else:
                self.qm.critical(self, 'Blank Field',
                                 'Asset ID field is blank, please fill in the field to remove association with an RFID tag')
                ETEK_log.info(
                    'Admin logged in as Employee ID ' + self.userLoggedIn + ' attempted to remove RFID tag from asset when asset ID field was blank')
        except:
            ETEK_log.error(self, 'An exception was thrown in AssignTag_removeButtonClicked function')
            self.qm.critical(self, 'Error', 'An exception was thrown in AssignTag_removeButtonClicked function')

    def AssignTag_confirmButtonClicked(self):
        try:
            AssetID = self.ui.AssignTag_Asset_Num_Field.text()
            RFID_Tag = self.ui.AssignTag_RFID_Tag_Field.text()


            if not (AssetID == '') or not (RFID_Tag == ''):
                # Asset does not exist
                if not self.Asset_Check(AssetID):
                    self.qm.critical(self,'Asset ID not found','Asset ID '+ AssetID +' not found in the database' + '\n\nCan not associate RFID tag unless asset is either created or imported into local database')
                #User entered in whitespace into RFID field
                if not re.findall("([ABCDEF]|[0-9]){24}",RFID_Tag):
                    self.qm.critical(self, 'Invalid RFID Tag','The RFID tag "' + RFID_Tag + '" must be a 24-digit hexidecimal value ' + '\n\nPlease try scanning RFID tag again')
                else:
                    #The asset exists in the RFID table already (it has a tag assigned already)
                    if self.RFIDTable_AssetCheck(AssetID)[0]:
                        response = self.qm.question(self, 'Input Required',
                                                    'The asset ID " ' + AssetID + '" already has the RFID tag "'+ self.RFIDTable_AssetCheck(AssetID)[1][0] + '" associated with it\n\n Do you want to assign the current RFID tag "' + RFID_Tag + '" to this asset ID?',
                                                    self.qm.Yes | self.qm.No)
                        if response == self.qm.Yes:
                            response = self.qm.question(self, 'Input Required',
                                                        'Please confirm that you want to assign the RFID tag: "' + RFID_Tag + '" to the asset ID "' + AssetID + '"',
                                                        self.qm.Yes | self.qm.No)
                            if response == self.qm.Yes:
                                self.RFIDTable_UpdateRow(AssetID,RFID_Tag)
                                self.qm.information(self, 'RFID Tag Assignment Successful',
                                                    'The assignment of RFID tag"' + RFID_Tag + 'to asset ID "' + AssetID + '" was sucessful!')

                            else:
                                self.qm.information(self, 'RFID Assignment Cancelled',
                                                    'The assignment of an RFID tag to an asset ID was cancelled')
                        else:
                            self.qm.information(self, 'RFID Assignment Cancelled', 'The assignment of an RFID tag to an asset ID was cancelled')
                    else:
                        response = self.qm.question(self, 'Input Required',
                                                    'Please confirm that you want to assign the RFID tag: "' + RFID_Tag + '" to the asset ID "' + AssetID + '"',
                                                    self.qm.Yes | self.qm.No)
                        if response == self.qm.Yes:
                            self.RFIDTable_InsertRow(AssetID,RFID_Tag)
                        else:
                            self.qm.information(self, 'RFID Assignment Cancelled', 'The assignment of an RFID tag to an asset ID was cancelled')


            else:
                self.qm.critical(self, 'Blank Fields','One or more fields are blank, please fill both to assign a tag to an asset ID')


        except:
            self.qm.critical(self,'Error','An exception was thrown in AssignTag_confirmButtonClicked function')
            ETEK_log.error(self, 'An exception was thrown in AssignTag_confirmButtonClicked function')

    #Returns true if asset exists in table, returns true if it does, false if it doesn't
    def RFIDTable_AssetCheck(self,AssetID):
        check_query = '''SELECT TOP 1 * FROM [RFID Table] WHERE (AssetID =  (?));'''  # '?' is a placeholder
        self.cursor.execute(check_query, str(AssetID))
        if self.cursor.fetchone():
            self.cursor.execute(check_query, str(AssetID))
            record = self.cursor.fetchone()
            return [True,record]
        else:
            return [False]

    def RFIDTable_RemoveRow(self, AssetID):
        delete_query = ''' DELETE FROM [RFID Table] WHERE (AssetID = (?));'''
        self.cursor.execute(delete_query, str(AssetID))
        self.cnxn.commit()

    def RFIDTable_InsertRow(self, AssetID, RFID_Tag):
        insert_query = ''' INSERT INTO [RFID Table] (AssetID, TagID) VALUES(?,?);'''
        self.cursor.execute(insert_query, str(AssetID),str(RFID_Tag))
        self.cnxn.commit()

    def RFIDTable_UpdateRow(self,AssetID, RFID_Tag):
        update_query = '''UPDATE [RFID Table] SET AssetID = (?), TagID = (?) WHERE AssetID = (?);'''
        self.cursor.execute(update_query, str(AssetID), str(RFID_Tag),str(AssetID))
        self.cnxn.commit()


class changePassword(QWidget):
    def __init__(self, parent=None):
        super(changePassword, self).__init__(parent)
        self.ui = Ui_PasswordChangeDialog()
        self.ui.setupUi(self)

        # self.ui.CurrentPassword_Field.returnPressed.connect(self.okButtonClicked())
        # self.ui.NewPassword_Field.returnPressed.connect(self.okButtonClicked())
        # self.ui.ConfirmPassword_Field.returnPressed.connect(self.okButtonClicked())
        self.ui.ok.clicked.connect(self.okButtonClicked)
        self.ui.cancel.clicked.connect(self.cancelButtonClicked)

        self.ui.CurrentPassword_Field.setEchoMode(QLineEdit.Password)
        self.ui.NewPassword_Field.setEchoMode(QLineEdit.Password)
        self.ui.ConfirmPassword_Field.setEchoMode(QLineEdit.Password)
        self.qm = QtWidgets.QMessageBox()
        self.userLoggedIn = ''

        #Validators
        rPWFields = QRegExp("\S*") #Reject whitespace

        CurrentPasswordValid = QtGui.QRegExpValidator(rPWFields, self.ui.CurrentPassword_Field)
        self.ui.CurrentPassword_Field.setValidator(CurrentPasswordValid)

        NewPasswordValid = QtGui.QRegExpValidator(rPWFields, self.ui.NewPassword_Field)
        self.ui.NewPassword_Field.setValidator(NewPasswordValid)

        NewPasswordValid = QtGui.QRegExpValidator(rPWFields, self.ui.ConfirmPassword_Field)
        self.ui.ConfirmPassword_Field.setValidator(NewPasswordValid)
    # setup the password and and the conditions of correct and wrong password in this method
    def okButtonClicked(self):
        try:
            BlankFieldCheckBoolFlag = (self.ui.CurrentPassword_Field.text() != '' and self.ui.NewPassword_Field.text() != '' and self.ui.ConfirmPassword_Field.text() != '')
            ETEK_log.info(
                'Admin logged in as employee ID ' + self.userLoggedIn + ' clicked the ok button')

            #if the old password entered is correct, go ahead and write new password to existing config file
            if BlankFieldCheckBoolFlag:
                if self.oldPasswordCheck():
                    if self.confirmNewPassword():
                        self.recordNewPasswordHash()
                else:
                    self.qm.warning(self, 'Invalid Password', "Current password does not match what was entered, please check spelling and try again")
            else:
                self.qm.warning(self, 'Blank Fields',
                                "Please make sure all fields are filled and try again")

        except:
            ETEK_log.error('error occurred inside the "changePassword" class in the "okButtonClicked" method')
            self.qm.critical(self,'Exception thrown',"An exception was thrown in the passwordChangeWindow class, okButtonClicked method")


    def confirmNewPassword(self):
        try:
            if(self.ui.NewPassword_Field.text() == self.ui.ConfirmPassword_Field.text()):
                ETEK_log.info(
                    'Admin logged in as employee ID ' + self.userLoggedIn + ' entered a new password that matched what was in both boxes')
                return True
            else:
                ETEK_log.info(
                    'Admin logged in as employee ID ' + self.userLoggedIn + ' entered a new password that did not match what was in both boxes')
                self.qm.warning(self, 'New password does not match',
                                "The new password does not match what was entered in the confirm field, please check spelling and try again")
                return False
        except:
            ETEK_log.error('error occurred inside the "changePassword" class in the "confirmNewPassword" method')
            self.qm.critical(self, 'Exception thrown',
                             "An exception was thrown in the passwordChangeWindow class, confirmNewPassword method")

    def recordNewPasswordHash(self):
        try:
            NewPW = self.ui.NewPassword_Field.text().encode('utf-8')
            hashpass = hashlib.sha256(NewPW).hexdigest()
            config = ConfigParser()
            config.read('config.ini')
            config['password']['pass'] = hashpass;
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
            ETEK_log.info('Admin logged in as employee ID ' + self.userLoggedIn + ' changed the application launch password')
            self.qm.information(self,'Password Change Successful', 'New password has been sucessfully changed')
            self.ui.NewPassword_Field.setText('')
            self.ui.CurrentPassword_Field.setText('')
            self.ui.ConfirmPassword_Field.setText('')


        except:
            ETEK_log.error('error occurred inside the "changePassword" class in the "recordNewPasswordHash" method')
            self.qm.critical(self, 'Exception thrown',
                             "An exception was thrown in the passwordChangeWindow class, recordNewPasswordHash method")

    def oldPasswordCheck(self):
        try:
            OldPW = self.ui.CurrentPassword_Field.text().encode('utf-8')
            hashpass = hashlib.sha256(OldPW).hexdigest()
            config = ConfigParser()
            config.read('config.ini')
            storedPass = config.get('password', 'pass')
            if hashpass == storedPass:  # password
                ETEK_log.info(
                    'Admin logged in as employee ID ' + self.userLoggedIn + ' entered current password into change password dialog')
                return True

            else:
                ETEK_log.info(
                    'Admin logged in as employee ID ' + self.userLoggedIn + ' entered wrong password into change password dialog')
                return False

        except:
            ETEK_log.error('error occurred inside the "changePassword" class in the "oldPasswordCheck" method')
            self.qm.critical(self,'Exception thrown',"An exception was thrown in the passwordChangeWindow class, oldPasswordCheck method")
    def open(self,userLoggedIn):
        try:
            self.userLoggedIn = userLoggedIn
            self.show()
            self.ui.CurrentPassword_Field.setText('')
            self.ui.NewPassword_Field.setText('')
            self.ui.ConfirmPassword_Field.setText('')

            ETEK_log.info(
                'Admin logged in as employee ID ' + self.userLoggedIn + ' opened the change password window from the home tab')
        except:
            ETEK_log.error('error occurred inside the "changePassword" class in the "open" method')
            self.qm.critical(self,'Exception thrown',"An exception was thrown in the passwordChangeWindow class, open method")

    def cancelButtonClicked(self):
        try:
            self.ui.CurrentPassword_Field.setText('')
            self.ui.NewPassword_Field.setText('')
            self.ui.ConfirmPassword_Field.setText('')
            self.close()
            ETEK_log.info(
                'Admin logged in as employee ID ' + self.userLoggedIn + ' closed the change password window from the home tab')
        except:
            ETEK_log.error('error occurred inside the "changePassword" class in the "close" method')
            self.qm.critical(self, 'Exception thrown',
                             "An exception was thrown in the passwordChangeWindow class, close method")
