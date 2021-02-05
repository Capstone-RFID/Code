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
        Admin_Interface.resize(529, 492)
        Admin_Interface.setStyleSheet("background-color: rgb(0, 0, 52);")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Admin_Interface)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Admin_Select = QtWidgets.QTabWidget(Admin_Interface)
        self.Admin_Select.setStyleSheet("background-color: rgb(0, 0, 52);\n"
"QTabBar::Home_Tab { height: 100px; width: 100px; background: \'grey\'}")
        self.Admin_Select.setIconSize(QtCore.QSize(12, 12))
        self.Admin_Select.setObjectName("Admin_Select")
        self.Home_Tab = QtWidgets.QWidget()
        self.Home_Tab.setObjectName("Home_Tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Home_Tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Home_Welcome_Message = QtWidgets.QLabel(self.Home_Tab)
        self.Home_Welcome_Message.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 20pt \"MS Shell Dlg 2\";")
        self.Home_Welcome_Message.setObjectName("Home_Welcome_Message")
        self.verticalLayout.addWidget(self.Home_Welcome_Message)
        self.label = QtWidgets.QLabel(self.Home_Tab)
        self.label.setStyleSheet("\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(171, 171, 171);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(68, 38, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.Home_Force_Sync_Button = QtWidgets.QPushButton(self.Home_Tab)
        self.Home_Force_Sync_Button.setStyleSheet("QPushButton#Home_Force_Sync_Button {\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: 26pt \"MS Shell Dlg 2\";\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"}\n"
"QPushButton#Home_Force_Sync_Button:pressed {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border-style: inset;\n"
"}")
        self.Home_Force_Sync_Button.setObjectName("Home_Force_Sync_Button")
        self.horizontalLayout.addWidget(self.Home_Force_Sync_Button)
        spacerItem2 = QtWidgets.QSpacerItem(68, 38, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.Admin_Select.addTab(self.Home_Tab, "")
        self.Search_Tab = QtWidgets.QWidget()
        self.Search_Tab.setObjectName("Search_Tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Search_Tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(258, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(188, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Search_Filters_Title = QtWidgets.QLabel(self.Search_Tab)
        self.Search_Filters_Title.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: Bold 14pt \"MS Shell Dlg 2\";")
        self.Search_Filters_Title.setObjectName("Search_Filters_Title")
        self.gridLayout.addWidget(self.Search_Filters_Title, 0, 0, 1, 1)
        self.Search_SearchAsset_Query_Button = QtWidgets.QPushButton(self.Search_Tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Search_SearchAsset_Query_Button.sizePolicy().hasHeightForWidth())
        self.Search_SearchAsset_Query_Button.setSizePolicy(sizePolicy)
        self.Search_SearchAsset_Query_Button.setMinimumSize(QtCore.QSize(186, 51))
        self.Search_SearchAsset_Query_Button.setMaximumSize(QtCore.QSize(186, 51))
        self.Search_SearchAsset_Query_Button.setStyleSheet("QPushButton#Search_SearchAsset_Query_Button {\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"}\n"
"QPushButton#Search_SearchAsset_Query_Button:pressed {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border-style: inset;\n"
"}")
        self.Search_SearchAsset_Query_Button.setObjectName("Search_SearchAsset_Query_Button")
        self.gridLayout.addWidget(self.Search_SearchAsset_Query_Button, 8, 2, 1, 1)
        self.Search_Datetime_To_Label = QtWidgets.QLabel(self.Search_Tab)
        self.Search_Datetime_To_Label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Search_Datetime_To_Label.setObjectName("Search_Datetime_To_Label")
        self.gridLayout.addWidget(self.Search_Datetime_To_Label, 2, 0, 1, 1)
        self.Search_Datetime_From_Label = QtWidgets.QLabel(self.Search_Tab)
        self.Search_Datetime_From_Label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Search_Datetime_From_Label.setObjectName("Search_Datetime_From_Label")
        self.gridLayout.addWidget(self.Search_Datetime_From_Label, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 3, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 3, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 3, 2, 1, 1)
        self.Search_Employee_ID_Entry_Field = QtWidgets.QLineEdit(self.Search_Tab)
        self.Search_Employee_ID_Entry_Field.setMinimumSize(QtCore.QSize(0, 25))
        self.Search_Employee_ID_Entry_Field.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(78, 78, 78);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Search_Employee_ID_Entry_Field.setObjectName("Search_Employee_ID_Entry_Field")
        self.gridLayout.addWidget(self.Search_Employee_ID_Entry_Field, 4, 1, 1, 1)
        self.Search_Employee_ID_Label = QtWidgets.QLabel(self.Search_Tab)
        self.Search_Employee_ID_Label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Search_Employee_ID_Label.setObjectName("Search_Employee_ID_Label")
        self.gridLayout.addWidget(self.Search_Employee_ID_Label, 4, 0, 1, 1)
        self.Search_Asset_Num_From_Label = QtWidgets.QLabel(self.Search_Tab)
        self.Search_Asset_Num_From_Label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Search_Asset_Num_From_Label.setObjectName("Search_Asset_Num_From_Label")
        self.gridLayout.addWidget(self.Search_Asset_Num_From_Label, 6, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 5, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 5, 0, 1, 1)
        self.Search_Asset_Numbers_Field = QtWidgets.QLineEdit(self.Search_Tab)
        self.Search_Asset_Numbers_Field.setMinimumSize(QtCore.QSize(0, 25))
        self.Search_Asset_Numbers_Field.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(78, 78, 78);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Search_Asset_Numbers_Field.setObjectName("Search_Asset_Numbers_Field")
        self.gridLayout.addWidget(self.Search_Asset_Numbers_Field, 6, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 5, 2, 1, 1)
        self.Search_Datetime_From = QtWidgets.QDateEdit(self.Search_Tab)
        self.Search_Datetime_From.setMinimumSize(QtCore.QSize(0, 25))
        self.Search_Datetime_From.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(78, 78, 78);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Search_Datetime_From.setCalendarPopup(True)
        self.Search_Datetime_From.setObjectName("Search_Datetime_From")
        self.gridLayout.addWidget(self.Search_Datetime_From, 1, 1, 1, 1)
        self.Search_Datetime_To = QtWidgets.QDateEdit(self.Search_Tab)
        self.Search_Datetime_To.setMinimumSize(QtCore.QSize(0, 25))
        self.Search_Datetime_To.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(78, 78, 78);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Search_Datetime_To.setCalendarPopup(True)
        self.Search_Datetime_To.setObjectName("Search_Datetime_To")
        self.gridLayout.addWidget(self.Search_Datetime_To, 2, 1, 1, 1)
        self.Search_Reset_Fields_Button = QtWidgets.QPushButton(self.Search_Tab)
        self.Search_Reset_Fields_Button.setMinimumSize(QtCore.QSize(186, 51))
        self.Search_Reset_Fields_Button.setMaximumSize(QtCore.QSize(186, 51))
        self.Search_Reset_Fields_Button.setStyleSheet("QPushButton#Search_Reset_Fields_Button {\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"}\n"
"QPushButton#Search_Reset_Fields_Button:pressed {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border-style: inset;\n"
"}")
        self.Search_Reset_Fields_Button.setObjectName("Search_Reset_Fields_Button")
        self.gridLayout.addWidget(self.Search_Reset_Fields_Button, 7, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.Search_Display_Results_Table = QtWidgets.QTableWidget(self.Search_Tab)
        self.Search_Display_Results_Table.setStyleSheet("background-color: rgb(78, 78, 78);")
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
        self.verticalLayout_2.addWidget(self.Search_Display_Results_Table)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem11 = QtWidgets.QSpacerItem(258, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.Search_Print_PDF_Button = QtWidgets.QPushButton(self.Search_Tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Search_Print_PDF_Button.sizePolicy().hasHeightForWidth())
        self.Search_Print_PDF_Button.setSizePolicy(sizePolicy)
        self.Search_Print_PDF_Button.setMinimumSize(QtCore.QSize(186, 51))
        self.Search_Print_PDF_Button.setStyleSheet("QPushButton#Search_Print_PDF_Button {\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"}\n"
"QPushButton#Search_Print_PDF_Button:pressed {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border-style: inset;\n"
"}")
        self.Search_Print_PDF_Button.setObjectName("Search_Print_PDF_Button")
        self.horizontalLayout_3.addWidget(self.Search_Print_PDF_Button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.Admin_Select.addTab(self.Search_Tab, "")
        self.Edit_Tab = QtWidgets.QWidget()
        self.Edit_Tab.setObjectName("Edit_Tab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.Edit_Tab)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Edit_Prompt1_Label = QtWidgets.QLabel(self.Edit_Tab)
        self.Edit_Prompt1_Label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: Bold 14pt \"MS Shell Dlg 2\";")
        self.Edit_Prompt1_Label.setObjectName("Edit_Prompt1_Label")
        self.verticalLayout_7.addWidget(self.Edit_Prompt1_Label)
        self.Edit_Prompt2_Label = QtWidgets.QLabel(self.Edit_Tab)
        self.Edit_Prompt2_Label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: Bold 14pt \"MS Shell Dlg 2\";")
        self.Edit_Prompt2_Label.setObjectName("Edit_Prompt2_Label")
        self.verticalLayout_7.addWidget(self.Edit_Prompt2_Label)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        spacerItem12 = QtWidgets.QSpacerItem(298, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem13, 4, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem14, 6, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem15, 4, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem16, 6, 1, 1, 1)
        self.Edit_Status_Label = QtWidgets.QLabel(self.Edit_Tab)
        self.Edit_Status_Label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Edit_Status_Label.setObjectName("Edit_Status_Label")
        self.gridLayout_2.addWidget(self.Edit_Status_Label, 5, 0, 1, 1)
        self.Edit_Status_Field = QtWidgets.QLineEdit(self.Edit_Tab)
        self.Edit_Status_Field.setMinimumSize(QtCore.QSize(0, 25))
        self.Edit_Status_Field.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(78, 78, 78);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Edit_Status_Field.setObjectName("Edit_Status_Field")
        self.gridLayout_2.addWidget(self.Edit_Status_Field, 5, 1, 1, 1)
        self.Edit_Description_Field = QtWidgets.QLineEdit(self.Edit_Tab)
        self.Edit_Description_Field.setMinimumSize(QtCore.QSize(0, 25))
        self.Edit_Description_Field.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(78, 78, 78);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Edit_Description_Field.setObjectName("Edit_Description_Field")
        self.gridLayout_2.addWidget(self.Edit_Description_Field, 3, 1, 1, 1)
        self.Edit_Last_Activity_Label = QtWidgets.QLabel(self.Edit_Tab)
        self.Edit_Last_Activity_Label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Edit_Last_Activity_Label.setObjectName("Edit_Last_Activity_Label")
        self.gridLayout_2.addWidget(self.Edit_Last_Activity_Label, 7, 0, 1, 1)
        self.Edit_Datetime = QtWidgets.QDateTimeEdit(self.Edit_Tab)
        self.Edit_Datetime.setMinimumSize(QtCore.QSize(0, 25))
        self.Edit_Datetime.setAcceptDrops(False)
        self.Edit_Datetime.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(78, 78, 78);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Edit_Datetime.setCalendarPopup(True)
        self.Edit_Datetime.setObjectName("Edit_Datetime")
        self.gridLayout_2.addWidget(self.Edit_Datetime, 7, 1, 1, 1)
        self.Edit_Asset_Num_Label = QtWidgets.QLabel(self.Edit_Tab)
        self.Edit_Asset_Num_Label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Edit_Asset_Num_Label.setObjectName("Edit_Asset_Num_Label")
        self.gridLayout_2.addWidget(self.Edit_Asset_Num_Label, 0, 0, 1, 1)
        self.Edit_Description_Label = QtWidgets.QLabel(self.Edit_Tab)
        self.Edit_Description_Label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Edit_Description_Label.setObjectName("Edit_Description_Label")
        self.gridLayout_2.addWidget(self.Edit_Description_Label, 3, 0, 1, 1)
        self.Edit_Asset_Num_Field = QtWidgets.QLineEdit(self.Edit_Tab)
        self.Edit_Asset_Num_Field.setMinimumSize(QtCore.QSize(0, 25))
        self.Edit_Asset_Num_Field.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(78, 78, 78);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Edit_Asset_Num_Field.setObjectName("Edit_Asset_Num_Field")
        self.gridLayout_2.addWidget(self.Edit_Asset_Num_Field, 0, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 25, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem17, 1, 0, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(40, 25, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem18, 1, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem19, 2, 0, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem20, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 3, 1)
        self.Edit_Clear_Button = QtWidgets.QPushButton(self.Edit_Tab)
        self.Edit_Clear_Button.setMinimumSize(QtCore.QSize(186, 51))
        self.Edit_Clear_Button.setStyleSheet("QPushButton#Edit_Clear_Button {\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"}\n"
"QPushButton#Edit_Clear_Button:pressed {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border-style: inset;\n"
"}")
        self.Edit_Clear_Button.setObjectName("Edit_Clear_Button")
        self.gridLayout_3.addWidget(self.Edit_Clear_Button, 2, 2, 1, 1)
        self.Edit_Search_Button = QtWidgets.QPushButton(self.Edit_Tab)
        self.Edit_Search_Button.setMinimumSize(QtCore.QSize(186, 51))
        self.Edit_Search_Button.setStyleSheet("QPushButton#Edit_Search_Button {\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"}\n"
"QPushButton#Edit_Search_Button:pressed {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border-style: inset;\n"
"}")
        self.Edit_Search_Button.setObjectName("Edit_Search_Button")
        self.gridLayout_3.addWidget(self.Edit_Search_Button, 0, 2, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem21, 1, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(298, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem22, 0, 1, 1, 1)
        self.Edit_Display_Results_Table = QtWidgets.QTableWidget(self.Edit_Tab)
        self.Edit_Display_Results_Table.setMinimumSize(QtCore.QSize(0, 123))
        self.Edit_Display_Results_Table.setStyleSheet("background-color: rgb(78, 78, 78);")
        self.Edit_Display_Results_Table.setColumnCount(5)
        self.Edit_Display_Results_Table.setObjectName("Edit_Display_Results_Table")
        self.Edit_Display_Results_Table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Edit_Display_Results_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Edit_Display_Results_Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Edit_Display_Results_Table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Edit_Display_Results_Table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Edit_Display_Results_Table.setHorizontalHeaderItem(4, item)
        self.gridLayout_4.addWidget(self.Edit_Display_Results_Table, 1, 0, 1, 2)
        self.verticalLayout_5.addLayout(self.gridLayout_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Edit_Delete_Entry_Button = QtWidgets.QPushButton(self.Edit_Tab)
        self.Edit_Delete_Entry_Button.setMinimumSize(QtCore.QSize(186, 51))
        self.Edit_Delete_Entry_Button.setStyleSheet("QPushButton#Edit_Delete_Entry_Button {\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"}\n"
"QPushButton#Edit_Delete_Entry_Button:pressed {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border-style: inset;\n"
"}")
        self.Edit_Delete_Entry_Button.setObjectName("Edit_Delete_Entry_Button")
        self.horizontalLayout_4.addWidget(self.Edit_Delete_Entry_Button)
        spacerItem23 = QtWidgets.QSpacerItem(328, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem23)
        self.Edit_Commit_Edits_Button = QtWidgets.QPushButton(self.Edit_Tab)
        self.Edit_Commit_Edits_Button.setMinimumSize(QtCore.QSize(186, 51))
        self.Edit_Commit_Edits_Button.setStyleSheet("QPushButton#Edit_Commit_Edits_Button {\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"}\n"
"QPushButton#Edit_Commit_Edits_Button:pressed {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border-style: inset;\n"
"}")
        self.Edit_Commit_Edits_Button.setObjectName("Edit_Commit_Edits_Button")
        self.horizontalLayout_4.addWidget(self.Edit_Commit_Edits_Button)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_9.addLayout(self.verticalLayout_5)
        self.Admin_Select.addTab(self.Edit_Tab, "")
        self.Create_Tab = QtWidgets.QWidget()
        self.Create_Tab.setObjectName("Create_Tab")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.Create_Tab)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.Create_Prompt_Label = QtWidgets.QLabel(self.Create_Tab)
        self.Create_Prompt_Label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: Bold 14pt \"MS Shell Dlg 2\";")
        self.Create_Prompt_Label.setObjectName("Create_Prompt_Label")
        self.gridLayout_6.addWidget(self.Create_Prompt_Label, 0, 0, 1, 2)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem24 = QtWidgets.QSpacerItem(20, 88, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem24)
        self.Create_Clear_Fields_Button = QtWidgets.QPushButton(self.Create_Tab)
        self.Create_Clear_Fields_Button.setMinimumSize(QtCore.QSize(186, 51))
        self.Create_Clear_Fields_Button.setStyleSheet("QPushButton#Create_Clear_Fields_Button {\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"}\n"
"QPushButton#Create_Clear_Fields_Button:pressed {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border-style: inset;\n"
"}")
        self.Create_Clear_Fields_Button.setObjectName("Create_Clear_Fields_Button")
        self.verticalLayout_8.addWidget(self.Create_Clear_Fields_Button)
        self.Create_Confirm_Entry_Button = QtWidgets.QPushButton(self.Create_Tab)
        self.Create_Confirm_Entry_Button.setMinimumSize(QtCore.QSize(186, 51))
        self.Create_Confirm_Entry_Button.setStyleSheet("QPushButton#Create_Confirm_Entry_Button {\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"}\n"
"QPushButton#Create_Confirm_Entry_Button:pressed {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border-style: inset;\n"
"}")
        self.Create_Confirm_Entry_Button.setObjectName("Create_Confirm_Entry_Button")
        self.verticalLayout_8.addWidget(self.Create_Confirm_Entry_Button)
        self.gridLayout_6.addLayout(self.verticalLayout_8, 1, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.Create_RFID_Tag_Field_3 = QtWidgets.QLineEdit(self.Create_Tab)
        self.Create_RFID_Tag_Field_3.setMinimumSize(QtCore.QSize(0, 25))
        self.Create_RFID_Tag_Field_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(78, 78, 78);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Create_RFID_Tag_Field_3.setText("")
        self.Create_RFID_Tag_Field_3.setObjectName("Create_RFID_Tag_Field_3")
        self.gridLayout_5.addWidget(self.Create_RFID_Tag_Field_3, 1, 1, 1, 1)
        self.Create_Asset_Num_Label = QtWidgets.QLabel(self.Create_Tab)
        self.Create_Asset_Num_Label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Create_Asset_Num_Label.setObjectName("Create_Asset_Num_Label")
        self.gridLayout_5.addWidget(self.Create_Asset_Num_Label, 0, 0, 1, 1)
        self.Create_Asset_Num_Field = QtWidgets.QLineEdit(self.Create_Tab)
        self.Create_Asset_Num_Field.setMinimumSize(QtCore.QSize(0, 25))
        self.Create_Asset_Num_Field.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(78, 78, 78);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Create_Asset_Num_Field.setObjectName("Create_Asset_Num_Field")
        self.gridLayout_5.addWidget(self.Create_Asset_Num_Field, 0, 1, 1, 1)
        self.Create_RFID_Tag_Label = QtWidgets.QLabel(self.Create_Tab)
        self.Create_RFID_Tag_Label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Create_RFID_Tag_Label.setObjectName("Create_RFID_Tag_Label")
        self.gridLayout_5.addWidget(self.Create_RFID_Tag_Label, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.verticalLayout_11.addLayout(self.gridLayout_6)
        self.Admin_Select.addTab(self.Create_Tab, "")
        self.Resolve_Tab = QtWidgets.QWidget()
        self.Resolve_Tab.setObjectName("Resolve_Tab")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.Resolve_Tab)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.Resolve_Display_Conflicts_Table = QtWidgets.QTableWidget(self.Resolve_Tab)
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
        self.verticalLayout_12.addWidget(self.Resolve_Display_Conflicts_Table)
        self.pushButton = QtWidgets.QPushButton(self.Resolve_Tab)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_12.addWidget(self.pushButton)
        self.Admin_Select.addTab(self.Resolve_Tab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Import_ImportAssets_Button = QtWidgets.QPushButton(self.tab)
        self.Import_ImportAssets_Button.setGeometry(QtCore.QRect(270, 230, 186, 51))
        self.Import_ImportAssets_Button.setMinimumSize(QtCore.QSize(186, 51))
        self.Import_ImportAssets_Button.setStyleSheet("QPushButton#Import_ImportAssets_Button {\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"}\n"
"QPushButton#Import_ImportAssets_Button:pressed {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border-style: inset;\n"
"}")
        self.Import_ImportAssets_Button.setObjectName("Import_ImportAssets_Button")
        self.Import_ImportEmployees_Button = QtWidgets.QPushButton(self.tab)
        self.Import_ImportEmployees_Button.setGeometry(QtCore.QRect(270, 300, 186, 51))
        self.Import_ImportEmployees_Button.setMinimumSize(QtCore.QSize(186, 51))
        self.Import_ImportEmployees_Button.setStyleSheet("QPushButton#Import_ImportEmployees_Button {\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"}\n"
"QPushButton#Import_ImportEmployees_Button:pressed {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border-style: inset;\n"
"}")
        self.Import_ImportEmployees_Button.setObjectName("Import_ImportEmployees_Button")
        self.Admin_Select.addTab(self.tab, "")
        self.verticalLayout_6.addWidget(self.Admin_Select)

        self.retranslateUi(Admin_Interface)
        self.Admin_Select.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(Admin_Interface)

    def retranslateUi(self, Admin_Interface):
        _translate = QtCore.QCoreApplication.translate
        Admin_Interface.setWindowTitle(_translate("Admin_Interface", "Form"))
        self.Home_Welcome_Message.setText(_translate("Admin_Interface", "Welcome to Admin Access"))
        self.label.setText(_translate("Admin_Interface", "Select Tabs Above To Navigate"))
        self.Home_Force_Sync_Button.setText(_translate("Admin_Interface", "Force Sync with central"))
        self.Admin_Select.setTabText(self.Admin_Select.indexOf(self.Home_Tab), _translate("Admin_Interface", "Home"))
        self.Search_Filters_Title.setText(_translate("Admin_Interface", "Search Filters"))
        self.Search_SearchAsset_Query_Button.setText(_translate("Admin_Interface", "Search Asset"))
        self.Search_Datetime_To_Label.setText(_translate("Admin_Interface", "Date/Time To:"))
        self.Search_Datetime_From_Label.setText(_translate("Admin_Interface", "Date/Time From:"))
        self.Search_Employee_ID_Label.setText(_translate("Admin_Interface", "Employee ID:"))
        self.Search_Asset_Num_From_Label.setText(_translate("Admin_Interface", "Asset Numbers:"))
        self.Search_Reset_Fields_Button.setText(_translate("Admin_Interface", "Reset Filters"))
        self.Search_Display_Results_Table.setSortingEnabled(True)
        item = self.Search_Display_Results_Table.horizontalHeaderItem(0)
        item.setText(_translate("Admin_Interface", "Asset#"))
        item = self.Search_Display_Results_Table.horizontalHeaderItem(1)
        item.setText(_translate("Admin_Interface", "Employee ID"))
        item = self.Search_Display_Results_Table.horizontalHeaderItem(2)
        item.setText(_translate("Admin_Interface", "Date checked out"))
        item = self.Search_Display_Results_Table.horizontalHeaderItem(3)
        item.setText(_translate("Admin_Interface", "Date checked in"))
        self.Search_Print_PDF_Button.setText(_translate("Admin_Interface", "Print to PDF"))
        self.Admin_Select.setTabText(self.Admin_Select.indexOf(self.Search_Tab), _translate("Admin_Interface", "Search"))
        self.Edit_Prompt1_Label.setText(_translate("Admin_Interface", "Enter Asset # to search for existing asset"))
        self.Edit_Prompt2_Label.setText(_translate("Admin_Interface", "Edit fields then click commit to change in local database"))
        self.Edit_Status_Label.setText(_translate("Admin_Interface", "Status:"))
        self.Edit_Last_Activity_Label.setText(_translate("Admin_Interface", "Last Activity:"))
        self.Edit_Asset_Num_Label.setText(_translate("Admin_Interface", "Asset #:"))
        self.Edit_Description_Label.setText(_translate("Admin_Interface", "Description:"))
        self.Edit_Clear_Button.setText(_translate("Admin_Interface", "Clear"))
        self.Edit_Search_Button.setText(_translate("Admin_Interface", "Search"))
        item = self.Edit_Display_Results_Table.horizontalHeaderItem(0)
        item.setText(_translate("Admin_Interface", "Asset#"))
        item = self.Edit_Display_Results_Table.horizontalHeaderItem(1)
        item.setText(_translate("Admin_Interface", "Employee ID"))
        item = self.Edit_Display_Results_Table.horizontalHeaderItem(2)
        item.setText(_translate("Admin_Interface", "Date checked out"))
        item = self.Edit_Display_Results_Table.horizontalHeaderItem(3)
        item.setText(_translate("Admin_Interface", "Date checked in"))
        item = self.Edit_Display_Results_Table.horizontalHeaderItem(4)
        item.setText(_translate("Admin_Interface", "Status"))
        self.Edit_Delete_Entry_Button.setText(_translate("Admin_Interface", "Delete Entry"))
        self.Edit_Commit_Edits_Button.setText(_translate("Admin_Interface", "Commit Edits"))
        self.Admin_Select.setTabText(self.Admin_Select.indexOf(self.Edit_Tab), _translate("Admin_Interface", "Edit"))
        self.Create_Prompt_Label.setText(_translate("Admin_Interface", "Enter asset info, then confirm new entry in local database"))
        self.Create_Clear_Fields_Button.setText(_translate("Admin_Interface", "Clear Fields"))
        self.Create_Confirm_Entry_Button.setText(_translate("Admin_Interface", "Confirm Entry"))
        self.Create_Asset_Num_Label.setText(_translate("Admin_Interface", "Asset #:"))
        self.Create_RFID_Tag_Label.setText(_translate("Admin_Interface", "RFID Tag #:"))
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
        self.Import_ImportAssets_Button.setText(_translate("Admin_Interface", "Import Assets"))
        self.Import_ImportEmployees_Button.setText(_translate("Admin_Interface", "PushButton"))
        self.Admin_Select.setTabText(self.Admin_Select.indexOf(self.tab), _translate("Admin_Interface", "Import"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Admin_Interface = QtWidgets.QWidget()
    ui = Ui_Admin_Interface()
    ui.setupUi(Admin_Interface)
    Admin_Interface.show()
    sys.exit(app.exec_())
