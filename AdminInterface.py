from sllurp import llrp
from twisted.internet import reactor
import pyodbc
from datetime import datetime
from datetime import date

from threading import Thread
import subprocess
import keyboard
import logging

from PyQt5 import QtCore, QtGui, QtWidgets,  QtPrintSupport
from PyQt5.QtCore import *
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

        self.edit_AssetSearchedInDatabase = None

        # ****************************************Home Tab Button(s)*********************************
        self.ui.Home_Force_Sync_Button.clicked.connect(self.home_syncButtonClicked)  # sync button connected

        #****************************************Search Tab Button(s)*********************************
        #self.ui.Search_SearchID_Query_Button.clicked.connect(self.search_searchIDButtonClicked)
        self.ui.Search_SearchAsset_Query_Button.clicked.connect(self.search_checkFieldInputs)
        #self.ui.Search_SearchDate_Query_Button.clicked.connect(self.search_searchDateButtonClicked)
        self.ui.Search_Print_PDF_Button.clicked.connect(self.search_printPDFButtonClicked)
        self.ui.Search_Reset_Fields_Button.clicked.connect(self.search_searchResetFieldsButtonClicked)

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
        #set defualt tab on window opening to home tab
        self.ui.Admin_Select.setCurrentIndex(0)

        #Set default datetime values to show admin users required format for input
        d = QDate(2021, 1, 1)
        self.ui.Search_Datetime_From.setDate(d)
        self.ui.Search_Datetime_To.setDate(d)


    #****************************************Class Methods for Tab Button(s)*********************************
    def home_syncButtonClicked(self):
        print("Home Sync Button Clicked")


    def search_searchResetFieldsButtonClicked(self):
        # Reset Filters to default values
        self.ui.Search_Employee_ID_Entry_Field.setText("")
        self.ui.Search_Asset_Numbers_Field.setText("")
        d = QDate(2021, 1, 1)
        self.ui.Search_Datetime_From.setDate(d)
        self.ui.Search_Datetime_To.setDate(d)

        #clear search results in table
        self.search_clearTableResults()


    #Generates list of assets in event log based on Employee ID search Filter
    def search_searchIDButtonClicked(self):
        print('Search Tab Search ID Button Clicked')
        #if self.Employee_ID_Check(self.ui.Search_Employee_ID_Entry_Field.text()):
        EmployeeNum = self.ui.Search_Employee_ID_Entry_Field.text()

        if self.Employee_ID_Check(EmployeeNum):
            EmployeeAssetList = self.Employee_ID_FindAssets(EmployeeNum)
            self.search_PopulateTable(EmployeeAssetList)
    # Generates list of EmployeeID in event log based on Assets in search Filter

    #Checks to see if entered asset# exists in asset table, populates table w/ query results if it is
    def search_searchAssetButtonClicked(self):
        print('Search Tab Search Asset Button Clicked')
        AssetNum = self.ui.Search_Asset_Numbers_Field.text()
        EmployeeNum = self.ui.Search_Employee_ID_Entry_Field.text()

        if self.Asset_Check(AssetNum):
            AssetList = self.Asset_List_Fetch(AssetNum)
            self.search_PopulateTable(AssetList)

    def search_searchAssetandIDButtonClicked(self):
        print('Search Tab Search Asset and ID Button Clicked')
        AssetNum = self.ui.Search_Asset_Numbers_Field.text()
        EmployeeNum = self.ui.Search_Employee_ID_Entry_Field.text()

        if self.Asset_Check(AssetNum) and self.Employee_ID_Check(EmployeeNum):
           EmployeeAndAssetList = self.search_fetchAssetAndID(AssetNum, EmployeeNum)
           if EmployeeAndAssetList:
            self.search_PopulateTable(EmployeeAndAssetList)

    def search_searchDateButtonClicked(self):
        print('Search Tab Search Date Button Clicked')

        dateTimeLowerBound = self.ui.Search_Datetime_From.text()
        dateTimeUpperBound = self.ui.Search_Datetime_To.text()

        if self.search_checkDateTimeBounds(dateTimeLowerBound, dateTimeUpperBound):
            DateList = self.search_fetchDateTime(dateTimeLowerBound, dateTimeUpperBound)
            if DateList:
                self.search_PopulateTable(DateList)

        #self.search_checkDateTimeBounds(dateTimeLowerBound, dateTimeUpperBound)
        #print(self.search_fetchDateTime(dateTimeLowerBound, dateTimeUpperBound))


    def search_printPDFButtonClicked(self):
        print('Search Tab Print Button Clicked')


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



    def edit_clearButtonClicked(self):
        print('Edit Tab Clear Button Clicked')
    def edit_searchButtonClicked(self):
        print('Edit Tab Search Button Clicked')
        self.edit_clearTableResults()
        if self.Asset_Check(self.ui.Edit_Asset_Num_Field.text()):
            print('Edit search found the asset!')
            EntryList = self.edit_Asset_Info_Fetch(self.ui.Edit_Asset_Num_Field.text())
            self.edit_AssetSearchedInDatabase = self.ui.Edit_Asset_Num_Field.text()
            self.edit_PopulateTable(EntryList)





            print(self.edit_AssetsInGUITable)
            print(self.edit_EmployeesInGUITable)


        else:
            print('Edit search did not find the asset!')
    def edit_deleteButtonClicked(self):
        print('Edit Tab Delete Button Clicked')
    def edit_commitButtonClicked(self):
        print('Edit Tab Commit Button Clicked')

        EntryList = self.edit_Asset_Info_Fetch(self.edit_AssetSearchedInDatabase)

        # Store the search results for later comparison if edits are made on interface
        for i in range(self.ui.Edit_Display_Results_Table.rowCount()):
            if EntryList[i][3] == None:
                EntryList[i][3] = ''
                self.edit_AssetsInGUITable.append(str(EntryList[i][3]))
            else:
                self.edit_AssetsInGUITable.append(str(EntryList[i][3]))

            if EntryList[i][2] == None:
                EntryList[i][2] = ''
                self.edit_EmployeesInGUITable.append(str(EntryList[i][2]))
            else:
                self.edit_EmployeesInGUITable.append(str(EntryList[i][2]))

            if EntryList[i][4] == None:
                EntryList[i][4] = 'Unknown'
                self.edit_StatusInGUITable.append(str(EntryList[i][4]))
            else:
                self.edit_StatusInGUITable.append(str(EntryList[i][4]))

        Edit_Table_Length = self.ui.Edit_Display_Results_Table.rowCount()
        for i in range(Edit_Table_Length):

            # Show items on row in interface
            Edit_Asset_Fetched = self.ui.Edit_Display_Results_Table.item(i, 0).text()
            Edit_Employee_Fetched = self.ui.Edit_Display_Results_Table.item(i, 1).text()
            #Edit_Datetime_Fetched = self.ui.Edit_Display_Results_Table.item(i, 2).text()
            Edit_Status_Fetched = self.ui.Edit_Display_Results_Table.item(i, 4).text()


            #NOTE:WRITING THE ASSET TO ANOTHER VARIABLE DOESN'T TRIGGER THE CONDITIONAL STATEMENT CORRECTLY, hence why the statement below is so long
            #If either the employeeID or the AssetID has been changed, then make a new event in the event log table

            print(self.ui.Edit_Display_Results_Table.item(i, 0).text())
            print(self.edit_AssetsInGUITable[i])

            if (self.ui.Edit_Display_Results_Table.item(i, 0).text() != self.edit_AssetsInGUITable[i]) or (self.ui.Edit_Display_Results_Table.item(i, 1).text() != (self.edit_EmployeesInGUITable[i])) or (self.ui.Edit_Display_Results_Table.item(i, 4).text() != self.edit_StatusInGUITable[i]):
                print(Edit_Asset_Fetched, Edit_Employee_Fetched)
                insert_event_query = ''' INSERT INTO [Event Log Table] (EmployeeID, AssetID, Status) VALUES(?,?,?);'''
                #Next two lines commit the edits present in the table
                self.cursor.execute(insert_event_query, str(Edit_Employee_Fetched), str(Edit_Asset_Fetched),str(Edit_Status_Fetched))
                self.cnxn.commit()
            else:
                print("Row "+ str(i + 1) + " has not been edited")
    def create_clearButtonClicked(self):
        print('Create Tab Clear Button Clicked')
    def create_confirmEntryButtonClicked(self):
        print('Create Tab Confirm Entry Button Clicked')

    # ****************************************End Class Methods for Tab Button(s)*****************************
    # ****************************************Class Methods for Running Queries*******************************
    #Searches for employee_ID in database, returns true if it exists else returns false
    def Employee_ID_Check(self, input):
        check_query = '''SELECT TOP 1 * FROM [Event Log Table] WHERE EmployeeID = (?);'''  # '?' is a placeholder
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

        self.search_clearTableResults()

        if self.ui.Search_Employee_ID_Entry_Field.text() and not self.ui.Search_Asset_Numbers_Field.text():
            self.search_searchIDButtonClicked()
        elif self.ui.Search_Asset_Numbers_Field.text() and not self.ui.Search_Employee_ID_Entry_Field.text():
            self.search_searchAssetButtonClicked()
        elif self.ui.Search_Asset_Numbers_Field.text() and self.ui.Search_Employee_ID_Entry_Field.text():
            self.search_searchAssetandIDButtonClicked()
        elif (self.ui.Search_Datetime_From.text() != "1/1/2021 00:00") and (self.ui.Search_Datetime_To.text() != "1/1/2021 00:00"):
            self.search_searchDateButtonClicked()
        elif not self.ui.Search_Employee_ID_Entry_Field.text() and not self.ui.Search_Asset_Numbers_Field.text() and (self.ui.Search_Datetime_From.text() == "1/1/2021 00:00") and (self.ui.Search_Datetime_To.text() == "1/1/2021 00:00"):
            print("No Asset or Employee ID or Date Range Entered!")


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
        check_query = '''SELECT * FROM [Event Log Table] WHERE (Timestamp >=  (?)) AND (Timestamp <=  (?));'''  # '?' is a placeholder
        self.cursor.execute(check_query, str(LowerBound), str(UpperBound))
        if self.cursor.fetchone():
            self.cursor.execute(check_query, str(LowerBound), str(UpperBound))

            return self.cursor.fetchall()
        else:

            return False



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
        #EmployeeAssetList = self.Employee_ID_FindAssets(EmployeeNum)
        print(EntryList)

        for i in range(len(EntryList)):
            # Create a row
            lastrow = self.ui.Search_Display_Results_Table.rowCount()
            self.ui.Search_Display_Results_Table.insertRow(lastrow)

            # Show items on row in interface
            self.ui.Search_Display_Results_Table.setItem(lastrow, 0, QTableWidgetItem(EntryList[i][3]))
            self.ui.Search_Display_Results_Table.setItem(lastrow, 1, QTableWidgetItem(EntryList[i][2]))
            self.ui.Search_Display_Results_Table.setItem(lastrow, 2, QTableWidgetItem(str(EntryList[i][1])))

    #Searchs for a list of assets specified by lower and upper bound of asset #'s
    #returns list within and including bounds
    def Asset_Check(self, AssetNum):
        check_query = '''SELECT TOP 1 * FROM [Event Log Table] WHERE (AssetID =  (?));'''  # '?' is a placeholder
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
                return False

