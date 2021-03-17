from sllurp import llrp
from twisted.internet import reactor
import pyodbc
from datetime import datetime
from datetime import date

from threading import Thread
import subprocess
import keyboard
import logging
#format log file to save as 'ETEK.log' and store date time and message of actions or errors
logging.basicConfig(filename='ETEK.log', filemode='w', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


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

#For reading passwords
from configparser import ConfigParser


import openpyxl



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
        # ****************************************Private Var(s)*********************************

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

        #Initialize this with nothing to start
        self.edit_AssetSearchedInDatabase = None
        # ****************************************Asset Validators*********************************
        #Validator for each QLineEdit in
        # validator to only enter valid asset ID's into asset ID entry fields
        self.onlyInt = QtGui.QIntValidator()

        rExpSearch = QRegExp("(([E,e][0-9]{7}|[4][0-9]{6})(,{1}))*") #"(,?[E,e][0-9]{7}|[4][0-9]{6})* + (,)*"
                                                                    #"(([E,e][0-9]{7}|[4][0-9]{6})(,))*"
        SearchTabValid = QtGui.QRegExpValidator(rExpSearch, self.ui.Search_Asset_Numbers_Field)
        self.ui.Search_Asset_Numbers_Field.setValidator(SearchTabValid)

        rExpEditAndCreate = QRegExp("([E,e][0-9]{7}|[4][0-9]{6})")
        EditTabValid = QtGui.QRegExpValidator(rExpEditAndCreate, self.ui.Edit_Asset_Field)
        self.ui.Edit_Asset_Field.setValidator(EditTabValid)

        CreateTabValid = QtGui.QRegExpValidator(rExpEditAndCreate, self.ui.Create_Asset_Num_Field)
        self.ui.Create_Asset_Num_Field.setValidator(CreateTabValid)
        # ****************************************End of Asset Validators*********************************

        # ****************************************Home Tab Button(s)*********************************
        self.ui.Home_Force_Sync_Button.clicked.connect(self.home_syncButtonClicked)  # sync button connected

        #****************************************Search Tab Button(s)*********************************
        #self.ui.Search_SearchID_Query_Button.clicked.connect(self.search_searchIDButtonClicked)
        self.ui.Search_SearchAsset_Query_Button.clicked.connect(self.search_checkFieldInputs)
        self.ui.Search_Employee_ID_Entry_Field.returnPressed.connect(self.search_checkFieldInputs)
        self.ui.Search_Asset_Numbers_Field.returnPressed.connect(self.search_checkFieldInputs)
        #self.ui.Search_SearchDate_Query_Button.clicked.connect(self.search_searchDateButtonClicked)
        self.ui.Search_Print_PDF_Button.clicked.connect(self.search_printPDFButtonClicked)
        self.ui.Search_Reset_Fields_Button.clicked.connect(self.search_searchResetFieldsButtonClicked)

        # ****************************************Edit Tab Button(s)*********************************
        self.ui.Edit_Clear_Button.clicked.connect(self.edit_clearButtonClicked)
        self.ui.Edit_Search_Button.clicked.connect(self.edit_searchButtonClicked)
        self.ui.Edit_Asset_Field.returnPressed.connect(self.edit_searchButtonClicked)
        #self.ui.Edit_Delete_Entry_Button.clicked.connect(self.edit_deleteButtonClicked)
        self.ui.Edit_Commit_Edits_Button.clicked.connect(self.edit_commitButtonClicked)


        # ****************************************Create Tab Button(s)*********************************
        self.ui.Create_Clear_Fields_Button.clicked.connect(self.create_clearButtonClicked)
        self.ui.Create_Confirm_Entry_Button.clicked.connect(self.create_confirmEntryButtonClicked)
        self.ui.Import_ImportAssets_Button.clicked.connect(self.Import_ImportAssets_ButtonClicked)
        self.ui.Import_ImportEmployees_Button.clicked.connect(self.Import_ImportEmployees_ButtonClicked)
        #

        # ****************************************Resolve Tab Button(s)*********************************
        #Nothing here yet, define button connections here when we put something in the GUI

        # ****************************************QMessageBox (Used across tabs)*********************************
        self.qm = QtWidgets.QMessageBox()

    # open up the admin window from the button on main window
    def openAdmin(self, s, d):
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

            logging.info('Connected to Server ' + server + ' and ' + database)


        except:
            logging.error('Unable to connect to Server ' + server + ' and ' + database + ' please check configuration file.')



    #****************************************Class Methods for Tab Button(s)*********************************
    def home_syncButtonClicked(self):
        print("Home Sync Button Clicked")


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
            logging.info('Search Filters reset')
        except:
            logging.error('Error while resetting Search Filters')



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
                    logging.info('Search for Employee ID (' + EmployeeNum + ') - events found')
                else:
                    self.qm.warning(self, 'No events found for Employee ID')
                    logging.info('Search for Employee ID (' + EmployeeNum + ') - no events found')
            else:
                #self.ui.Search_UI_Message_Prompt.setText('No matching employee ID found')
                self.qm.warning(self, 'Notice', 'No matching employee ID found')
                logging.info('Search for Employee ID (' + EmployeeNum + ') - no matching employee found')

                #self.ui.Search_UI_Message_Prompt.setText('Found Employee ID')
        # Generates list of EmployeeID in event log based on Assets in search Filter

        except:
            logging.error('Error while searching for Employee ID. In function - search_searchIDButtonClicked')

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
                    logging.info('Search for Asset Number (' + AssetNum + ') - events found')
                elif not self.Asset_Check(AssetNum) and (len(AssetInputs) > 1):
                    self.qm.critical(self, 'Notice', 'Asset number ' + AssetNum + ' does not exist in local database')
                    self.qm.warning(self, 'Notice', 'At least one asset not found')
                    logging.info('Search for Asset Number (' + AssetNum + ') - does not exist in local database')
                elif not self.Asset_Check(AssetNum):
                    self.qm.critical(self, 'Notice', 'Asset number ' + AssetNum + ' does not exist in local database')
                    logging.info('Search for Asset Number (' + AssetNum + ') - does not exist in local database')
        except:
            logging.error('Error while searching for Assets. In function - search_searchAssetButtonClicked')

    def search_searchAssetandIDButtonClicked(self,AssetString):

        try:
            atLeastOneAssetNotFound_Flag = 0
            print('Search Tab Search Asset and ID Button Clicked')
            #AssetNum = self.ui.Search_Asset_Numbers_Field.text()
            EmployeeNum = self.ui.Search_Employee_ID_Entry_Field.text()
            if(not self.Employee_ID_Check(EmployeeNum)):
                self.qm.critical(self, 'Notice', 'Unknown employee ID')
                logging.info('Employee ID (' + EmployeeNum + ') does not exist in local database')

            for AssetNum in AssetString:

                #Both the asset and employee ID exist, search and populate table display
                if self.Asset_Check(AssetNum) and self.Employee_ID_Check(EmployeeNum):
                   EmployeeAndAssetList = self.search_fetchAssetAndID(AssetNum, EmployeeNum)
                   if EmployeeAndAssetList:
                       self.search_PopulateTable(EmployeeAndAssetList)
                       logging.info('Search for Asset (' + AssetNum + ') used by Employee ID (' + EmployeeNum + ') - events found')
                   else:
                       print('No ID found with that Asset')
                       atLeastOneAssetNotFound_Flag = 1
                       #self.qm.information(self, 'Notice', 'No employee ID found with the asset number '+ AssetNum)
                       logging.info('Search for Asset (' + AssetNum + ') used by Employee ID (' + EmployeeNum + ') - events not found')



               #If the asset doesn't exist, we're searching a list and the employee does exist, then display these prompts
                elif not self.Asset_Check(AssetNum) and (len(AssetString) > 1) and self.Employee_ID_Check(EmployeeNum):
                    self.qm.critical(self, 'Notice', 'Asset number ' + AssetNum + ' does not exist in local database')
                    atLeastOneAssetNotFound_Flag = 1
                    logging.info('Search for Asset (' + AssetNum + ') used by Employee ID (' + EmployeeNum + ') - Asset not in database')


                #If the asset doesn't exist, the employee does exist, then display this prompt
                elif(not self.Asset_Check(AssetNum) and self.Employee_ID_Check(EmployeeNum)):
                    #self.ui.Search_UI_Message_Prompt.setText('At least one asset not found')
                    self.qm.critical(self, 'Notice','Asset number ' + AssetNum + ' does not exist in local database')
                    logging.info('Search for Asset (' + AssetNum + ') used by Employee ID (' + EmployeeNum + ') - Asset not in database')

                # If the employee ID does not exist, notify the user, then display this prompt
                elif (not self.Employee_ID_Check(EmployeeNum)):
                    # self.ui.Search_UI_Message_Prompt.setText('Unknown employee ID')
                    print('Unknown employee ID')
                    self.qm.critical(self, 'Notice', 'Employee ID ' + EmployeeNum + ' does not exist in local database')
                    logging.info('Search for Asset (' + AssetNum + ') used by Employee ID (' + EmployeeNum + ') - Employee ID not in database')

                # If the employee ID does not exist, notify the user, don't search anything then display this prompt
                elif (not self.Asset_Check(AssetNum)):
                    # self.ui.Search_UI_Message_Prompt.setText('Unknown employee ID')
                    print('Unknown employee ID')
                    self.qm.critical(self, 'Notice', 'Asset ID ' + AssetNum + ' does not exist in local database')
                    logging.info('Search for Asset (' + AssetNum + ') used by Employee ID (' + EmployeeNum + ') - Employee ID and Asset both not in database')


            if(atLeastOneAssetNotFound_Flag == 1):
                self.qm.warning(self, 'Notice', 'At least one asset not found')
        except:
            logging.error('Error while searching for Assets used by Employee. In function - search_searchAssetandIDButtonClicked')


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
                    logging.info('Search for Dates between (' + dateTimeLowerBound + ') and (' + dateTimeUpperBound + ') - events found for date range')
            else:
                #self.ui.Search_UI_Message_Prompt.setText('No events found between these dates')
                self.qm.information(self, 'Notice', 'No events found between these dates')
                logging.info('Search for Dates between (' + dateTimeLowerBound + ') and (' + dateTimeUpperBound + ') - no events found for date range')

                if not self.Employee_ID_Check(EmployeeID) and (EmployeeID != ''):
                    self.qm.critical(self, 'Critical Issue','Employee ID ' + EmployeeID + ' does not exist in the local database')
                    logging.info('Search for Dates between (' + dateTimeLowerBound + ') and (' + dateTimeUpperBound + ') - Employee  ' + EmployeeID + ' does not exist in database.')

                if len(AssetList) != 0:
                    for Asset in AssetList:
                        if not self.Asset_Check(Asset):
                            self.qm.critical(self, 'Critical Issue','Asset ID ' + Asset + ' does not exist in the local database')
                            logging.info('Search for Dates between (' + dateTimeLowerBound + ') and (' + dateTimeUpperBound + ') - Asset ' + Asset + ' does not exist in database.')

        except:
            logging.error('Error while searching for Date range. In function - search_searchDateButtonClicked')





    def search_printPDFButtonClicked(self):
        try:
            print('Search Tab Print Button Clicked')
            self.ui.Search_UI_Message_Prompt.setText('Printing to PDF...')

            #calling the qt object constantly was long and unwieldy, just call it w and move on
            #w = self.ui.Search_Display_Results_Table

            #Append date & time into filename (admin may do multiple searches + prints over several minutes)
            today = str(datetime.now().strftime("%B %d, %Y %H %M %S"))
            filename = "Search Results " + today + ".pdf"
            model = self.ui.Search_Display_Results_Table.model()

            #Below just prints a generic crappy table - modify to make formatting better if we have time later
            printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.PrinterResolution)
            printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
            printer.setPaperSize(QtPrintSupport.QPrinter.A4)
            printer.setOrientation(QtPrintSupport.QPrinter.Landscape)
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
            self.qm.information(self, 'Notice', 'Successful PDF Print!')
            logging.info('Print to PDF Search Results Completed')

        except:
            logging.error('Error while printing to PDF. In function - search_printPDFButtonClicked')


    def edit_clearButtonClicked(self):
        try:
            print('Edit Tab Clear Button Clicked')
            self.ui.Edit_UI_Message_Prompt.setText('')
            self.ui.Edit_AssignTo_Field.setText('')
            self.ui.Edit_Asset_Field.setText('')
            self.ui.Edit_Update_Status_Dropdown.setCurrentIndex(0)
            self.ui.Edit_UI_Message_Name_From_ID.setText('')
        except:
            logging.error('Error In function - edit_clearButtonClicked')

    # Searches Asset Table to see if asset even exists, then searches
    # for most recent event regarding that asset and who it's assigned to/what is it's status
    def edit_searchButtonClicked(self):
        try:
            print('Edit Tab Search Button Clicked')

            #self.ui.Edit_UI_Message_Prompt.setText('Searching...')

            #self.edit_clearTableResults()
            if self.Asset_Check(self.ui.Edit_Asset_Field.text()):
                print('Edit search found the asset!')
                #self.ui.Edit_UI_Message_Prompt.setText('Asset Found')
                #self.qm.information(self, 'Notice', 'Asset Found!')
                #EntryList = self.edit_Asset_Info_Fetch(self.ui.Edit_Asset_Num_Field.text())
                #self.edit_AssetSearchedInDatabase = self.ui.Edit_Asset_Field.text()
                #self.edit_PopulateTable(EntryList)
                AssetState = self.edit_Asset_List_Fetch(self.ui.Edit_Asset_Field.text())
                # This updates the edit tab GUI fields w/ relevant info from the Event Log
                #Current_Status = AssetState[0][4]
                self.ui.Edit_AssignTo_Field.setText(AssetState[0][2])

                #Query the name of employee using the asset from the employee table
                EmployeeName = self.edit_FetchNameViaID(AssetState[0][2])
                if EmployeeName != "":
                    self.ui.Edit_UI_Message_Name_From_ID.setText(EmployeeName[0])
                else:
                    self.ui.Edit_UI_Message_Name_From_ID.setText(EmployeeName)



                AssetStatus = AssetState[0][4]
                if AssetStatus == '1':
                    AssetStatus_Dropdown = 'Checked In'
                elif AssetStatus == '2':
                    AssetStatus_Dropdown = 'Checked Out'
                if AssetStatus == '3':
                    AssetStatus_Dropdown = 'In Repair'
                elif AssetStatus == '4':
                     AssetStatus_Dropdown = 'Retired'
                if AssetStatus == '5':
                    AssetStatus_Dropdown = 'Broken'
                elif AssetStatus == '6':
                     AssetStatus_Dropdown = 'New Item'
                elif AssetStatus == '7':
                    AssetStatus_Dropdown = 'New Employee'
                self.ui.Edit_Update_Status_Dropdown.setCurrentText(AssetStatus_Dropdown)
            else:
                print('Edit search did not find the asset!')
                #self.ui.Edit_UI_Message_Prompt.setText('Asset not found')
                self.qm.Critical(self, 'Invalid Entry', 'Asset does not exist in local database!')
        except:
            logging.error('Error In function - edit_searchButtonClicked')


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
            logging.error('Error In function - edit_FetchNameViaID')


    def edit_commitButtonClicked(self):
        try:
            print('Edit Tab Commit Button Clicked')

            #AssetState = self.Asset_Return(self.edit_AssetSearchedInDatabase)
            if self.ui.Edit_Update_Status_Dropdown.currentText() != '':
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
                elif self.ui.Edit_Update_Status_Dropdown.currentText() == 'New Item':
                    AssetStatus_Dropdown = '6'
                elif self.ui.Edit_Update_Status_Dropdown.currentText() == 'New Employee':
                    AssetStatus_Dropdown = '7'
                Edit_Employee = self.ui.Edit_AssignTo_Field.text()
                Edit_Asset = self.ui.Edit_Asset_Field.text()

                insert_event_query = ''' INSERT INTO [Event Log Table] (EmployeeID, AssetID, Status) VALUES(?,?,?);'''
                #Next two lines commit the edits present in the table
                self.cursor.execute(insert_event_query, str(Edit_Employee), str(Edit_Asset),str(AssetStatus_Dropdown))
                self.cnxn.commit()
                self.ui.Edit_UI_Message_Prompt.setText('')
                EmployeeName = (self.edit_FetchNameViaID(Edit_Employee))
                self.qm.information(self, 'Edit Confirmation', 'Asset ' + Edit_Asset +' was assigned to '+ EmployeeName[0] + ' (Employee ID: ' + Edit_Employee +') with the status: "' + self.ui.Edit_Update_Status_Dropdown.currentText() +'" (status code ' + AssetStatus_Dropdown +')')
                logging.info('Asset Edits Committed to Database')

                #clear fields after commit
                self.ui.Edit_AssignTo_Field.setText('')
                self.ui.Edit_Asset_Field.setText('')
                self.ui.Edit_Update_Status_Dropdown.setCurrentIndex(0)
                self.ui.Edit_UI_Message_Name_From_ID.setText('')

            else:
                print("Please fill status field before committing")
                #self.ui.Edit_UI_Message_Prompt.setText('Please fill status field')
                self.qm.critical(self, 'Critical Issue', 'Please fill status field!')
        except:
            logging.error('Error In function - edit_commitButtonClicked')
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
            logging.error('Error In function - create_clearButtonClicked')


    #Edit from RFID text field to RFID scan for entering the tag (maybe change lineEdit field to text display)
    def create_confirmEntryButtonClicked(self):
        try:
            self.ui.Create_UI_Message_Prompt.setText('')

            #Turn text field string into a list of a single string
            AssetFiltered = self.checkMultiItemsCommas(self.ui.Create_Asset_Num_Field.text())

            #If the format is good, then go ahead, else this is replaced with a blank list
            AssetFiltered = self.checkInputAssetFormat(AssetFiltered)


            if (AssetFiltered) and (self.ui.Create_Asset_Description_Field.text() != ''):
                print('Create Tab Confirm Entry Button Clicked')

                if (self.AssetRFID_Check(self.ui.Create_Asset_Num_Field.text()) or self.Asset_Check(AssetFiltered[0])):
                    print('This asset ID already exists! ')
                    #self.ui.Create_UI_Message_Prompt.setText('ID already exists')
                    self.qm.warning(self, 'Notice', 'ID already exists')

                    # If the RFID number does not exist yet (and field is not blank) , then write it to the RFID table with existing asset
                    if ((not self.RFID_Check(self.ui.Create_RFID_Tag_Field_3.text()) and (self.ui.Create_RFID_Tag_Field_3.text() != ''))):
                        print('Linking existing asset to new RFID tag ')

                        insert_event_query = ''' INSERT INTO [RFID Table] (TagID, AssetID) VALUES(?,?);'''
                        # Next two lines commit the edits present in the table
                        self.cursor.execute(insert_event_query, str(self.ui.Create_RFID_Tag_Field_3.text()),
                                            str(self.ui.Create_Asset_Num_Field.text()))
                        #self.cnxn.commit()

                        # Create an event in the Event Log Table to show linking
                        # Append status # 420 (An RFID tag was linked to an existing asset in the system)
                        insert_event_query = ''' INSERT INTO [Event Log Table] (EmployeeID, AssetID, Status) VALUES(?,?,?);'''
                        # Next two lines commit the edits present in the table
                        self.cursor.execute(insert_event_query, str(''), str(self.ui.Create_Asset_Num_Field.text()), str(420))
                        self.cnxn.commit()
                        #self.ui.Create_UI_Message_Prompt.setText('New tag applied to asset')
                        self.qm.information(self,'Notice', 'New tag applied to asset!')
                        logging.info('New RFID tag added to existing Asset in Database')


                    #Edit this so it prints info somewhere so user can edit association
                    elif(self.RFID_Check(self.ui.Create_RFID_Tag_Field_3.text()) and (self.ui.Create_RFID_Tag_Field_3.text() != '')):

                        print('This tag already associated with another asset!')
                        #self.ui.Create_UI_Message_Prompt.setText('Tag associated w/ another asset')
                        self.qm.warning(self, 'Notice', 'This tag already associated with another asset!')

                else:
                    # If the RFID number does not exist yet (and field is not blank) and the asset does not already exist, then write it to the RFID table
                    if ((not self.RFID_Check(self.ui.Create_RFID_Tag_Field_3.text()) and (self.ui.Create_RFID_Tag_Field_3.text() != ''))):
                        insert_event_query = ''' INSERT INTO [RFID Table] (TagID, AssetID) VALUES(?,?);'''
                        # Next two lines commit the edits present in the table
                        self.cursor.execute(insert_event_query, str(self.ui.Create_RFID_Tag_Field_3.text()),
                                            str(self.ui.Create_Asset_Num_Field.text()))
                    #self.cnxn.commit()
                    #Create an event in the Event Log Table
                    #Append status # 3 (A new asset was added to the system)
                    insert_event_query = ''' INSERT INTO [Event Log Table] (EmployeeID, AssetID, Status) VALUES(?,?,?);'''
                    # Next two lines commit the edits present in the table
                    self.cursor.execute(insert_event_query, str(''), str(self.ui.Create_Asset_Num_Field.text()),str(3))


                    #insert new Asset into Asset Table
                    insert_event_query = ''' INSERT INTO [Asset Table] (AssetID, Type) VALUES(?,?);'''
                    # Next two lines commit the edits present in the table
                    self.cursor.execute(insert_event_query, str(self.ui.Create_Asset_Num_Field.text()), str(self.ui.Create_Asset_Description_Field.text()))

                    self.cnxn.commit()
                    #self.ui.Create_UI_Message_Prompt.setText('Asset Successfully Created!')
                    self.qm.information(self, 'Notice', "Asset Successfully Created!")
                    logging.info('New Asset linked to RFID and created in Database')
            else:
                print("Enter both a valid asset number and description!")
                #self.ui.Create_UI_Message_Prompt.setText('Enter valid asset # and description')
                self.qm.warning(self, 'Notice', 'Enter valid asset number (Exxxxxxx OR 4xxxxxx, x ~ digit) and a description!')

            # clear fields after commit
            self.ui.Create_Asset_Num_Field.setText("")
            self.ui.Create_Asset_Description_Field.setText("")
            self.ui.Create_RFID_Tag_Field_3.setText("")
        except:
            logging.error('Error In function - create_confirmEntryButtonClicked')

    def find_files(self,filename):
        try:
            fileNotFoundFlag = 0 #Used to ask user if they want to search the C:\ drive
            path_list = [Path("D:\\"),Path("E:\\"),Path("F:\\"),Path("G:\\"),Path("H:\\"),Path("I:\\"),Path("J:\\"),Path("K:\\"),Path("L:\\"),Path("M:\\"),Path("N:\\"),Path("O:\\"),Path("P\\"),Path("Q:\\"),Path("R:\\"),Path("S:\\"),Path("T:\\"),Path("U:\\"),Path("V:\\"),Path("W:\\"),Path("X:\\"),Path("Y:\\"),Path("Z:\\")]
            # Walking top-down from the root
            for search_path in path_list:
                for root, dir, files in os.walk(search_path):
                    if filename in files:
                        #print(os.path.join(root, filename))
                        return (os.path.join(root, filename))

            response = self.qm.question(self, 'Input Required', "Could not find " + filename +" on letter drives D: thru Z:" + "\n\nDo you want to search the C: drive for "+ filename + "?" + "\nWARNING: Searching C: drive may take some time", self.qm.Yes | self.qm.No)
            if response == self.qm.Yes:
                for root, dir, files in os.walk(Path("C:\\")):
                    if filename in files:
                        # print(os.path.join(root, filename))
                        return (os.path.join(root, filename))
                    else:
                        fileNotFoundFlag = 1
            elif response == self.qm.No:
                self.qm.warning(self, 'File not found',"Could not find " + filename + " on USB drive, please check that file exists on USB drive")
                return False

            if fileNotFoundFlag == 1:
                self.qm.warning(self, 'File not found', "Could not find " + filename + " on USB or C: drive, please check that file exists")
                return False
        except:
            logging.error('Error In function - find_files')







    def Import_ImportAssets_ButtonClicked(self):
        try:
            print('Import Tab ImportAssets Button Clicked')
            self.ui.Create_UI_Message_Prompt.setText('')
            name = "AssetList.xlsx"
            assetFile = self.find_files(name)

            if(assetFile != False):
                dataAsset = pd.read_excel(assetFile, engine='openpyxl', dtype = str)

                df = pd.DataFrame(dataAsset, columns=['AssetID', 'Type'])

                if dataAsset.columns[0] == 'AssetID' and dataAsset.columns[1] == 'Type':
                    if not all (np.where(pd.isnull(df))):
                        count = 0
                        for index in df["AssetID"]:
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
                            count = count +1

                        df = df.reset_index(drop=True)
                        self.import_checkAssetsOrEmployeesToSQL(df)
                       # self.ui.Create_UI_Message_Prompt.setText('Import Successful!')
                        self.qm.information(self, 'Notice', 'Import successful!')
                        logging.info('New Assets imported successfully through .xlsx file')

                    else:
                        print('Please reformat excel into 2 columns "AssetID" and "Type" with no blank cells')
                        #self.ui.Create_UI_Message_Prompt.setText('Import failed: blank cells in file')
                        self.qm.critical(self, 'Critical Issue', 'Import failed: please reformat .xlsx file into 2 columns "AssetID" and "Type" with no blank cells')
                else:
                    print('Please reformat excel into 2 columns "AssetID" and "Type"')
                    #self.ui.Create_UI_Message_Prompt.setText('Import failed: check column headers')
                    self.qm.critical(self, 'Critical Issue','Import failed: please reformat .xlsx file into 2 columns "AssetID" and "Type" with no blank cells')
        except:
            logging.error('Error In function - Import_ImportAssets_ButtonClicked')

    def Import_ImportEmployees_ButtonClicked(self):
        try:
            print('Import Tab ImportEmployees Button Clicked')
            self.ui.Create_UI_Message_Prompt.setText('')
            name = "EmployeeList.xlsx"
            employeeFile = self.find_files(name)

            if (employeeFile != False):


                dataEmployee = pd.read_excel(employeeFile, engine = 'openpyxl', dtype = str)
                df = pd.DataFrame(dataEmployee, columns=['Name', 'EmployeeID'])

                if dataEmployee.columns[0] == 'Name' and dataEmployee.columns[1] == 'EmployeeID':
                    if not all (np.where(pd.isnull(df))):
                        self.import_checkAssetsOrEmployeesToSQL(df)
                        #self.ui.Create_UI_Message_Prompt.setText('Import Successful!')
                        self.qm.information(self, 'Notice', 'Import successful!')
                        logging.info('New Employees imported successfully through .xlsx file')

                    else:
                        print('Please reformat excel into 2 columns "Name" and "EmployeeID" with no empty cells')
                        #self.ui.Create_UI_Message_Prompt.setText('Import failed: blank cells in file')
                        self.qm.critical(self, 'Critical Issue','Import failed: please reformat .xlsx file into 2 columns "Name" and "EmployeeID" with no blank cells')
                else:
                    print('Please reformat excel into 2 columns "Name" and "EmployeeID"')
                    #self.ui.Create_UI_Message_Prompt.setText('Import failed: bad column header(s)')
                    self.qm.critical(self, 'Critical Issue','Import failed: please reformat .xlsx file into 2 columns "Name" and "EmployeeID" with no blank cells')
        except:
            logging.error('Error In function - Import_ImportEmployees_ButtonClicked')




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


            # if EmployeeIdField and not AssetField and not SearchMonthFlag and NoDateRangeFlag:
            #     self.search_searchIDButtonClicked()
            #
            # elif AssetField and not EmployeeIdField:
            #     self.search_searchAssetButtonClicked()
            #
            # elif AssetField and EmployeeIdField:
            #     self.search_searchAssetandIDButtonClicked()
            #
            # elif (SearchMonthFlag):
            #     self.search_Find_Months()
            #
            # elif YesDateRangeFlag:
            #     self.search_searchDateButtonClicked()
            #
            # elif not EmployeeIdField and not AssetField and NoDateRangeFlag:
            #     print("No Asset or Employee ID or Date Range Entered!")
            #     self.ui.Search_UI_Message_Prompt.setText('Specify Search Filters!')
        except:
            logging.error('Error while searching. In function - search_checkFieldInputs')

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
                logging.info('Search by Specific Month - events found')
            else:
                #self.ui.Search_UI_Message_Prompt.setText('No events found for that month')
                #self.qm.information(self, 'Notice', 'No events found for that month')
                logging.info('Search by Specific Month - no events found')
        except:
            logging.error('Error while searching by Month. In function - search_Find_Months ')

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
            self.ui.Edit_Display_Results_Table.setItem(lastrow, 0, QTableWidgetItem(EntryList[i][3]))
            self.ui.Edit_Display_Results_Table.setItem(lastrow, 1, QTableWidgetItem(EntryList[i][2]))
            self.ui.Edit_Display_Results_Table.setItem(lastrow, 2, QTableWidgetItem(str(EntryList[i][1])))
            self.ui.Edit_Display_Results_Table.setItem(lastrow, 4, QTableWidgetItem(str(EntryList[i][4])))

    def search_PopulateTable(self, EntryList):
        try:
            #EmployeeAssetList = self.Employee_ID_FindAssets(EmployeeNum)
            print(EntryList)



            for i in range(len(EntryList)):
                # Create a row
                lastrow = self.ui.Search_Display_Results_Table.rowCount()
                self.ui.Search_Display_Results_Table.insertRow(lastrow)

                AssetStatus = EntryList[i][4]
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
                elif AssetStatus == '6':
                    AssetStatus_Words = 'New Item'
                elif AssetStatus == '7':
                    AssetStatus_Words = 'New Employee'

                # Show items on row in interface
                self.ui.Search_Display_Results_Table.setItem(lastrow, 0, QTableWidgetItem(EntryList[i][3]))
                self.ui.Search_Display_Results_Table.setItem(lastrow, 1, QTableWidgetItem(EntryList[i][2]))
                self.ui.Search_Display_Results_Table.setItem(lastrow, 2, QTableWidgetItem(str(EntryList[i][1])))
                self.ui.Search_Display_Results_Table.setItem(lastrow, 3, QTableWidgetItem(str(AssetStatus_Words)))
        except:
            self.qm.critical(self, 'Notice', 'An exception was thrown')

    #Searchs for a list of assets specified by lower and upper bound of asset #'s
    #returns list within and including bounds


    def Asset_Check(self, AssetNum):
        check_query = '''SELECT TOP 1 * FROM [Asset Table] WHERE (AssetID =  (?));'''  # '?' is a placeholder
        self.cursor.execute(check_query, str(AssetNum))
        if self.cursor.fetchone():
            self.cursor.execute(check_query, str(AssetNum))
            return True
        else:

            return False

    # def Asset_Return(self, AssetNum):
    #     check_query = '''SELECT TOP 1 * FROM [Event Log Table] WHERE (AssetID =  (?));'''  # '?' is a placeholder
    #     self.cursor.execute(check_query, str(AssetNum))
    #     if self.cursor.fetchone():
    #         self.cursor.execute(check_query, str(AssetNum))
    #         return self.cursor.fetchall()
    #     else:
    #         return False

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

        #Look at first column in Excel table to determine what data we're working with here
        for col in df.columns:
            if col == "Name":
                importType = "Employees"
                break
            elif col == "AssetID":
                importType = "Assets"
                break


        #if we're importing employees, populate lists for SQL queries and importing into SQL
        if importType == "Employees":
            for row in range(len(df.index)):
                #if the employee ID already exists, it won't be imported to the lists
                if not self.Employee_ID_Check(str(df.at[row, 'EmployeeID'])):
                    self.import_EmployeeIDList.append(str(df.at[row, 'EmployeeID']))
                    self.import_EmployeeNameList.append(str(df.at[row, 'Name']))

                    #Commit employee ID to Event log as a new addition (code 104) "10-4 good buddy"
                    self.import_commitEmployeesToSQL(str(df.at[row, 'EmployeeID']),str(df.at[row, 'Name']))
                    # NOTE: We should have a GUI notification that shows the import was sucessful
                    #self.ui.Create_UI_Message_Prompt.setText('Employee(s) imported')
                    self.qm.information(self, 'Notice', 'New employee(s) imported successfully!')


                #NOTE: We should have a case where it notifies you on the GUI if you're trying to enter data that already exists and what entries would be duplicates
                else:
                    print("The employee ID: "+ str(df.at[row, 'EmployeeID']) +" already exists in the database")

        # if we're importing assets, populate lists for SQL queries and importing into SQL
        if importType == "Assets":
            for row in range(len(df.index)):

                # if the asset ID already exists, it won't be imported to the lists or commited to SQL
                if not self.Asset_Check(str(df.at[row, 'AssetID'])):
                    self.import_AssetList.append(df.at[row, 'AssetID'])
                    self.import_AssetList.append(str(df.at[row, 'Type']))

                    #Commit employee ID to Event log as a new addition (code 42) "The answer to everything"
                    self.import_commitAssetsToSQL(str(df.at[row, 'AssetID']),str(df.at[row, 'Type']))
                    #self.ui.Create_UI_Message_Prompt.setText('Asset(s) imported')
                    self.qm.information(self, 'Notice', 'New asset(s) imported successfully!')
                # NOTE: We should have a case where it notifies you on the GUI if you're trying to enter data that already exists and what entries would be duplicates
                else:
                    print("The Asset Number: "+ str(df.at[row, 'AssetID']) +" already exists in the database")


        print(self.import_EmployeeIDList)
        print(self.import_EmployeeNameList)
        print(self.import_AssetList)


    #New employee imported appends
    def import_commitEmployeesToSQL(self, EmployeeID, EmployeeName):
        insert_event_query = ''' INSERT INTO [Employee Table] (EmployeeID, Name) VALUES(?,?);'''
        # Next two lines commit the edits present in the table
        self.cursor.execute(insert_event_query, str(EmployeeID), str(EmployeeName))
        self.cnxn.commit()

    # New asset imported appends with status #6
    def import_commitAssetsToSQL(self, AssetID, Description):
        insert_event_query = ''' INSERT INTO [Event Log Table] (AssetID, Status) VALUES(?,?);'''
        # Next two lines commit the edits present in the table
        self.cursor.execute(insert_event_query, str(AssetID), '6')

        insert_event_query = ''' INSERT INTO [Asset Table] (AssetID, Type) VALUES(?,?);'''
        # Next two lines commit the edits present in the table
        self.cursor.execute(insert_event_query, str(AssetID), str(Description))

        self.cnxn.commit()