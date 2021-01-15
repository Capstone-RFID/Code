# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin_Level2_Access.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Admin_Interface(object):
    def setupUi(self, Admin_Interface):
        Admin_Interface.setObjectName("Admin_Interface")
        Admin_Interface.resize(860, 821)
        self.Admin_Select = QtWidgets.QTabWidget(Admin_Interface)
        self.Admin_Select.setGeometry(QtCore.QRect(50, 50, 701, 601))
        self.Admin_Select.setObjectName("Admin_Select")
        self.Home_Tab = QtWidgets.QWidget()
        self.Home_Tab.setObjectName("Home_Tab")
        self.Home_Force_Sync_Button = QtWidgets.QPushButton(self.Home_Tab)
        self.Home_Force_Sync_Button.setGeometry(QtCore.QRect(0, 0, 151, 23))
        self.Home_Force_Sync_Button.setObjectName("Home_Force_Sync_Button")
        self.Home_Welcome_Message = QtWidgets.QLabel(self.Home_Tab)
        self.Home_Welcome_Message.setGeometry(QtCore.QRect(50, 50, 301, 16))
        self.Home_Welcome_Message.setObjectName("Home_Welcome_Message")
        self.Home_User_Prompt = QtWidgets.QLabel(self.Home_Tab)
        self.Home_User_Prompt.setGeometry(QtCore.QRect(50, 100, 251, 16))
        self.Home_User_Prompt.setObjectName("Home_User_Prompt")
        self.Admin_Select.addTab(self.Home_Tab, "")
        self.Search_Tab = QtWidgets.QWidget()
        self.Search_Tab.setObjectName("Search_Tab")
        self.Search_Datetime_From = QtWidgets.QDateTimeEdit(self.Search_Tab)
        self.Search_Datetime_From.setGeometry(QtCore.QRect(50, 0, 194, 22))
        self.Search_Datetime_From.setObjectName("Search_Datetime_From")
        self.Search_Datetime_To = QtWidgets.QDateTimeEdit(self.Search_Tab)
        self.Search_Datetime_To.setGeometry(QtCore.QRect(50, 50, 194, 22))
        self.Search_Datetime_To.setObjectName("Search_Datetime_To")
        self.Search_Datetime_From_Label = QtWidgets.QLabel(self.Search_Tab)
        self.Search_Datetime_From_Label.setGeometry(QtCore.QRect(0, 0, 47, 13))
        self.Search_Datetime_From_Label.setObjectName("Search_Datetime_From_Label")
        self.Search_Datetime_To_Label = QtWidgets.QLabel(self.Search_Tab)
        self.Search_Datetime_To_Label.setGeometry(QtCore.QRect(0, 50, 47, 13))
        self.Search_Datetime_To_Label.setObjectName("Search_Datetime_To_Label")
        self.Search_Employee_ID_Entry_Field = QtWidgets.QLineEdit(self.Search_Tab)
        self.Search_Employee_ID_Entry_Field.setGeometry(QtCore.QRect(100, 100, 151, 20))
        self.Search_Employee_ID_Entry_Field.setObjectName("Search_Employee_ID_Entry_Field")
        self.Search_Employee_ID_Label = QtWidgets.QLabel(self.Search_Tab)
        self.Search_Employee_ID_Label.setGeometry(QtCore.QRect(0, 100, 101, 16))
        self.Search_Employee_ID_Label.setObjectName("Search_Employee_ID_Label")
        self.Search_Search_Query_Button = QtWidgets.QPushButton(self.Search_Tab)
        self.Search_Search_Query_Button.setGeometry(QtCore.QRect(300, 50, 75, 23))
        self.Search_Search_Query_Button.setObjectName("Search_Search_Query_Button")
        self.Search_Print_PDF_Button = QtWidgets.QPushButton(self.Search_Tab)
        self.Search_Print_PDF_Button.setGeometry(QtCore.QRect(300, 100, 75, 23))
        self.Search_Print_PDF_Button.setObjectName("Search_Print_PDF_Button")
        self.Search_Asset_Num_From_Label = QtWidgets.QLabel(self.Search_Tab)
        self.Search_Asset_Num_From_Label.setGeometry(QtCore.QRect(0, 150, 101, 16))
        self.Search_Asset_Num_From_Label.setObjectName("Search_Asset_Num_From_Label")
        self.Search_Asset_Numbers_From_Field = QtWidgets.QLineEdit(self.Search_Tab)
        self.Search_Asset_Numbers_From_Field.setGeometry(QtCore.QRect(100, 150, 151, 20))
        self.Search_Asset_Numbers_From_Field.setObjectName("Search_Asset_Numbers_From_Field")
        self.Search_Asset_Numbers_To_Field = QtWidgets.QLineEdit(self.Search_Tab)
        self.Search_Asset_Numbers_To_Field.setGeometry(QtCore.QRect(100, 200, 151, 20))
        self.Search_Asset_Numbers_To_Field.setObjectName("Search_Asset_Numbers_To_Field")
        self.Search_Asset_Num_To_Label = QtWidgets.QLabel(self.Search_Tab)
        self.Search_Asset_Num_To_Label.setGeometry(QtCore.QRect(0, 200, 101, 16))
        self.Search_Asset_Num_To_Label.setObjectName("Search_Asset_Num_To_Label")
        self.Search_Display_Results_Table = QtWidgets.QTableWidget(self.Search_Tab)
        self.Search_Display_Results_Table.setGeometry(QtCore.QRect(0, 250, 451, 301))
        self.Search_Display_Results_Table.setObjectName("Search_Display_Results_Table")
        self.Search_Display_Results_Table.setColumnCount(4)
        self.Search_Display_Results_Table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Search_Display_Results_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Search_Display_Results_Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Search_Display_Results_Table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Search_Display_Results_Table.setHorizontalHeaderItem(3, item)
        self.Admin_Select.addTab(self.Search_Tab, "")
        self.Edit_Tab = QtWidgets.QWidget()
        self.Edit_Tab.setObjectName("Edit_Tab")
        self.Edit_Name_Label = QtWidgets.QLabel(self.Edit_Tab)
        self.Edit_Name_Label.setGeometry(QtCore.QRect(50, 100, 47, 13))
        self.Edit_Name_Label.setObjectName("Edit_Name_Label")
        self.Edit_Name_Field = QtWidgets.QLineEdit(self.Edit_Tab)
        self.Edit_Name_Field.setGeometry(QtCore.QRect(150, 100, 113, 20))
        self.Edit_Name_Field.setObjectName("Edit_Name_Field")
        self.Edit_Asset_Num_Label = QtWidgets.QLabel(self.Edit_Tab)
        self.Edit_Asset_Num_Label.setGeometry(QtCore.QRect(50, 50, 47, 13))
        self.Edit_Asset_Num_Label.setObjectName("Edit_Asset_Num_Label")
        self.Edit_Asset_Num_Field = QtWidgets.QLineEdit(self.Edit_Tab)
        self.Edit_Asset_Num_Field.setGeometry(QtCore.QRect(150, 50, 113, 20))
        self.Edit_Asset_Num_Field.setObjectName("Edit_Asset_Num_Field")
        self.Edit_Status_Label = QtWidgets.QLabel(self.Edit_Tab)
        self.Edit_Status_Label.setGeometry(QtCore.QRect(50, 150, 47, 13))
        self.Edit_Status_Label.setObjectName("Edit_Status_Label")
        self.Edit_Status_Field = QtWidgets.QLineEdit(self.Edit_Tab)
        self.Edit_Status_Field.setGeometry(QtCore.QRect(150, 150, 113, 20))
        self.Edit_Status_Field.setObjectName("Edit_Status_Field")
        self.Edit_Clear_Button = QtWidgets.QPushButton(self.Edit_Tab)
        self.Edit_Clear_Button.setGeometry(QtCore.QRect(400, 200, 101, 23))
        self.Edit_Clear_Button.setObjectName("Edit_Clear_Button")
        self.Edit_Commit_Edits_Button = QtWidgets.QPushButton(self.Edit_Tab)
        self.Edit_Commit_Edits_Button.setGeometry(QtCore.QRect(550, 200, 101, 23))
        self.Edit_Commit_Edits_Button.setObjectName("Edit_Commit_Edits_Button")
        self.Edit_Search_Button = QtWidgets.QPushButton(self.Edit_Tab)
        self.Edit_Search_Button.setGeometry(QtCore.QRect(300, 50, 75, 23))
        self.Edit_Search_Button.setObjectName("Edit_Search_Button")
        self.Edit_Datetime = QtWidgets.QDateTimeEdit(self.Edit_Tab)
        self.Edit_Datetime.setGeometry(QtCore.QRect(150, 200, 194, 22))
        self.Edit_Datetime.setObjectName("Edit_Datetime")
        self.Edit_Last_Activity_Label = QtWidgets.QLabel(self.Edit_Tab)
        self.Edit_Last_Activity_Label.setGeometry(QtCore.QRect(50, 200, 101, 16))
        self.Edit_Last_Activity_Label.setObjectName("Edit_Last_Activity_Label")
        self.Edit_Delete_Entry_Button = QtWidgets.QPushButton(self.Edit_Tab)
        self.Edit_Delete_Entry_Button.setGeometry(QtCore.QRect(300, 100, 75, 23))
        self.Edit_Delete_Entry_Button.setObjectName("Edit_Delete_Entry_Button")
        self.Edit_Prompt1_Label = QtWidgets.QLabel(self.Edit_Tab)
        self.Edit_Prompt1_Label.setGeometry(QtCore.QRect(400, 50, 251, 16))
        self.Edit_Prompt1_Label.setObjectName("Edit_Prompt1_Label")
        self.Edit_Prompt2_Label = QtWidgets.QLabel(self.Edit_Tab)
        self.Edit_Prompt2_Label.setGeometry(QtCore.QRect(400, 100, 301, 16))
        self.Edit_Prompt2_Label.setObjectName("Edit_Prompt2_Label")
        self.Admin_Select.addTab(self.Edit_Tab, "")
        self.Create_Tab = QtWidgets.QWidget()
        self.Create_Tab.setObjectName("Create_Tab")
        self.Create_Name_Label = QtWidgets.QLabel(self.Create_Tab)
        self.Create_Name_Label.setGeometry(QtCore.QRect(0, 100, 47, 13))
        self.Create_Name_Label.setObjectName("Create_Name_Label")
        self.Create_Asset_Num_Label = QtWidgets.QLabel(self.Create_Tab)
        self.Create_Asset_Num_Label.setGeometry(QtCore.QRect(0, 50, 47, 13))
        self.Create_Asset_Num_Label.setObjectName("Create_Asset_Num_Label")
        self.Create_Clear_Fields_Button = QtWidgets.QPushButton(self.Create_Tab)
        self.Create_Clear_Fields_Button.setGeometry(QtCore.QRect(250, 100, 75, 23))
        self.Create_Clear_Fields_Button.setObjectName("Create_Clear_Fields_Button")
        self.Create_Confirm_Entry_Button = QtWidgets.QPushButton(self.Create_Tab)
        self.Create_Confirm_Entry_Button.setGeometry(QtCore.QRect(250, 50, 75, 23))
        self.Create_Confirm_Entry_Button.setObjectName("Create_Confirm_Entry_Button")
        self.Create_Prompt_Label = QtWidgets.QLabel(self.Create_Tab)
        self.Create_Prompt_Label.setGeometry(QtCore.QRect(350, 50, 301, 16))
        self.Create_Prompt_Label.setObjectName("Create_Prompt_Label")
        self.Create_Asset_Num_Field = QtWidgets.QLineEdit(self.Create_Tab)
        self.Create_Asset_Num_Field.setGeometry(QtCore.QRect(100, 50, 113, 20))
        self.Create_Asset_Num_Field.setObjectName("Create_Asset_Num_Field")
        self.Create_Name_Field = QtWidgets.QLineEdit(self.Create_Tab)
        self.Create_Name_Field.setGeometry(QtCore.QRect(100, 100, 113, 20))
        self.Create_Name_Field.setObjectName("Create_Name_Field")
        self.Create_RFID_Tag_Label = QtWidgets.QLabel(self.Create_Tab)
        self.Create_RFID_Tag_Label.setGeometry(QtCore.QRect(0, 150, 101, 16))
        self.Create_RFID_Tag_Label.setObjectName("Create_RFID_Tag_Label")
        self.Create_Part_Number_Field = QtWidgets.QLineEdit(self.Create_Tab)
        self.Create_Part_Number_Field.setGeometry(QtCore.QRect(100, 200, 113, 20))
        self.Create_Part_Number_Field.setText("")
        self.Create_Part_Number_Field.setObjectName("Create_Part_Number_Field")
        self.Create_RFID_Tag_Field_3 = QtWidgets.QLineEdit(self.Create_Tab)
        self.Create_RFID_Tag_Field_3.setGeometry(QtCore.QRect(100, 150, 113, 20))
        self.Create_RFID_Tag_Field_3.setText("")
        self.Create_RFID_Tag_Field_3.setObjectName("Create_RFID_Tag_Field_3")
        self.Create_Part_Number_Label = QtWidgets.QLabel(self.Create_Tab)
        self.Create_Part_Number_Label.setGeometry(QtCore.QRect(0, 200, 101, 16))
        self.Create_Part_Number_Label.setObjectName("Create_Part_Number_Label")
        self.Admin_Select.addTab(self.Create_Tab, "")
        self.Resolve_Tab = QtWidgets.QWidget()
        self.Resolve_Tab.setObjectName("Resolve_Tab")
        self.Resolve_Display_Conflicts_Table = QtWidgets.QTableWidget(self.Resolve_Tab)
        self.Resolve_Display_Conflicts_Table.setGeometry(QtCore.QRect(50, 50, 601, 401))
        self.Resolve_Display_Conflicts_Table.setObjectName("Resolve_Display_Conflicts_Table")
        self.Resolve_Display_Conflicts_Table.setColumnCount(6)
        self.Resolve_Display_Conflicts_Table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Resolve_Display_Conflicts_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Resolve_Display_Conflicts_Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Resolve_Display_Conflicts_Table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Resolve_Display_Conflicts_Table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Resolve_Display_Conflicts_Table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Resolve_Display_Conflicts_Table.setHorizontalHeaderItem(5, item)
        self.pushButton = QtWidgets.QPushButton(self.Resolve_Tab)
        self.pushButton.setGeometry(QtCore.QRect(275, 450, 100, 100))
        self.pushButton.setObjectName("pushButton")
        self.Admin_Select.addTab(self.Resolve_Tab, "")

        self.retranslateUi(Admin_Interface)
        self.Admin_Select.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Admin_Interface)

    def retranslateUi(self, Admin_Interface):
        _translate = QtCore.QCoreApplication.translate
        Admin_Interface.setWindowTitle(_translate("Admin_Interface", "Form"))
        self.Home_Force_Sync_Button.setText(_translate("Admin_Interface", "Force Sync with central"))
        self.Home_Welcome_Message.setText(_translate("Admin_Interface", "Welcome to Admin Access, "))
        self.Home_User_Prompt.setText(_translate("Admin_Interface", "please use tabs along top to navigate options"))
        self.Admin_Select.setTabText(self.Admin_Select.indexOf(self.Home_Tab), _translate("Admin_Interface", "Home"))
        self.Search_Datetime_From_Label.setText(_translate("Admin_Interface", "From:"))
        self.Search_Datetime_To_Label.setText(_translate("Admin_Interface", "To:"))
        self.Search_Employee_ID_Label.setText(_translate("Admin_Interface", "Employee ID:"))
        self.Search_Search_Query_Button.setText(_translate("Admin_Interface", "Search"))
        self.Search_Print_PDF_Button.setText(_translate("Admin_Interface", "Print to PDF"))
        self.Search_Asset_Num_From_Label.setText(_translate("Admin_Interface", "Asset numbers from"))
        self.Search_Asset_Num_To_Label.setText(_translate("Admin_Interface", "Assest numbers to"))
        item = self.Search_Display_Results_Table.horizontalHeaderItem(0)
        item.setText(_translate("Admin_Interface", "Asset#"))
        item = self.Search_Display_Results_Table.horizontalHeaderItem(1)
        item.setText(_translate("Admin_Interface", "Employee ID"))
        item = self.Search_Display_Results_Table.horizontalHeaderItem(2)
        item.setText(_translate("Admin_Interface", "Date checked out"))
        item = self.Search_Display_Results_Table.horizontalHeaderItem(3)
        item.setText(_translate("Admin_Interface", "Date checked in"))
        self.Admin_Select.setTabText(self.Admin_Select.indexOf(self.Search_Tab), _translate("Admin_Interface", "Search"))
        self.Edit_Name_Label.setText(_translate("Admin_Interface", "Name"))
        self.Edit_Asset_Num_Label.setText(_translate("Admin_Interface", "Asset #"))
        self.Edit_Status_Label.setText(_translate("Admin_Interface", "Status"))
        self.Edit_Clear_Button.setText(_translate("Admin_Interface", "Clear"))
        self.Edit_Commit_Edits_Button.setText(_translate("Admin_Interface", "Commit Edits"))
        self.Edit_Search_Button.setText(_translate("Admin_Interface", "Search"))
        self.Edit_Last_Activity_Label.setText(_translate("Admin_Interface", "Last Activity"))
        self.Edit_Delete_Entry_Button.setText(_translate("Admin_Interface", "Delete Entry"))
        self.Edit_Prompt1_Label.setText(_translate("Admin_Interface", "Enter Asset # then search for existing asset"))
        self.Edit_Prompt2_Label.setText(_translate("Admin_Interface", "Edit fields then click commit to change in local database"))
        self.Admin_Select.setTabText(self.Admin_Select.indexOf(self.Edit_Tab), _translate("Admin_Interface", "Edit"))
        self.Create_Name_Label.setText(_translate("Admin_Interface", "Name"))
        self.Create_Asset_Num_Label.setText(_translate("Admin_Interface", "Asset #"))
        self.Create_Clear_Fields_Button.setText(_translate("Admin_Interface", "Clear Fields"))
        self.Create_Confirm_Entry_Button.setText(_translate("Admin_Interface", "Confirm Entry"))
        self.Create_Prompt_Label.setText(_translate("Admin_Interface", "Enter asset info, then confirm new entry in local database"))
        self.Create_RFID_Tag_Label.setText(_translate("Admin_Interface", "RFID Tag #"))
        self.Create_Part_Number_Label.setText(_translate("Admin_Interface", "Part Number"))
        self.Admin_Select.setTabText(self.Admin_Select.indexOf(self.Create_Tab), _translate("Admin_Interface", "Create"))
        item = self.Resolve_Display_Conflicts_Table.horizontalHeaderItem(0)
        item.setText(_translate("Admin_Interface", "Asset #"))
        item = self.Resolve_Display_Conflicts_Table.horizontalHeaderItem(1)
        item.setText(_translate("Admin_Interface", "RFID #"))
        item = self.Resolve_Display_Conflicts_Table.horizontalHeaderItem(2)
        item.setText(_translate("Admin_Interface", "Employee ID"))
        item = self.Resolve_Display_Conflicts_Table.horizontalHeaderItem(3)
        item.setText(_translate("Admin_Interface", "Date checked out"))
        item = self.Resolve_Display_Conflicts_Table.horizontalHeaderItem(4)
        item.setText(_translate("Admin_Interface", "Date checked in"))
        item = self.Resolve_Display_Conflicts_Table.horizontalHeaderItem(5)
        item.setText(_translate("Admin_Interface", "Conflict Msg"))
        self.pushButton.setText(_translate("Admin_Interface", "Conflict Details"))
        self.Admin_Select.setTabText(self.Admin_Select.indexOf(self.Resolve_Tab), _translate("Admin_Interface", "Resolve"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Admin_Interface = QtWidgets.QWidget()
    ui = Ui_Admin_Interface()
    ui.setupUi(Admin_Interface)
    Admin_Interface.show()
    sys.exit(app.exec_())
