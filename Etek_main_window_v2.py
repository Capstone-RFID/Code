# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Etek_main_window_v2.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1127, 885)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(MainWindow)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(520, 480, 521, 311))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.New_Item_List = QtWidgets.QListWidget(self.horizontalLayoutWidget_3)
        self.New_Item_List.setObjectName("New_Item_List")
        item = QtWidgets.QListWidgetItem()
        self.New_Item_List.addItem(item)
        self.horizontalLayout_3.addWidget(self.New_Item_List)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(MainWindow)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 479, 521, 311))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Existing_Item_list = QtWidgets.QListWidget(self.horizontalLayoutWidget_4)
        self.Existing_Item_list.setObjectName("Existing_Item_list")
        item = QtWidgets.QListWidgetItem()
        self.Existing_Item_list.addItem(item)
        self.horizontalLayout_4.addWidget(self.Existing_Item_list)
        self.Cancel_Button = QtWidgets.QPushButton(MainWindow)
        self.Cancel_Button.setGeometry(QtCore.QRect(260, 820, 75, 23))
        self.Cancel_Button.setObjectName("Cancel_Button")
        self.Done_Button = QtWidgets.QPushButton(MainWindow)
        self.Done_Button.setGeometry(QtCore.QRect(710, 820, 75, 23))
        self.Done_Button.setObjectName("Done_Button")
        self.Employee_ID_Label = QtWidgets.QLabel(MainWindow)
        self.Employee_ID_Label.setGeometry(QtCore.QRect(300, 60, 251, 51))
        self.Employee_ID_Label.setObjectName("Employee_ID_Label")
        self.Employee_ID_Input = QtWidgets.QLineEdit(MainWindow)
        self.Employee_ID_Input.setGeometry(QtCore.QRect(670, 60, 251, 41))
        self.Employee_ID_Input.setObjectName("Employee_ID_Input")
        self.Action_To_Perform_Label = QtWidgets.QLabel(MainWindow)
        self.Action_To_Perform_Label.setGeometry(QtCore.QRect(210, 190, 181, 21))
        self.Action_To_Perform_Label.setObjectName("Action_To_Perform_Label")
        self.Employee_ID_Enter = QtWidgets.QCommandLinkButton(MainWindow)
        self.Employee_ID_Enter.setGeometry(QtCore.QRect(930, 60, 185, 41))
        self.Employee_ID_Enter.setObjectName("Employee_ID_Enter")
        self.Asset_ID_Enter = QtWidgets.QCommandLinkButton(MainWindow)
        self.Asset_ID_Enter.setGeometry(QtCore.QRect(930, 320, 185, 41))
        self.Asset_ID_Enter.setObjectName("Asset_ID_Enter")
        self.Asset_ID_Label = QtWidgets.QLabel(MainWindow)
        self.Asset_ID_Label.setGeometry(QtCore.QRect(300, 320, 251, 51))
        self.Asset_ID_Label.setObjectName("Asset_ID_Label")
        self.Asset_ID_Input = QtWidgets.QLineEdit(MainWindow)
        self.Asset_ID_Input.setGeometry(QtCore.QRect(670, 320, 251, 41))
        self.Asset_ID_Input.setText("")
        self.Asset_ID_Input.setObjectName("Asset_ID_Input")
        self.Existing_Item_Label = QtWidgets.QLabel(MainWindow)
        self.Existing_Item_Label.setGeometry(QtCore.QRect(100, 450, 171, 21))
        self.Existing_Item_Label.setObjectName("Existing_Item_Label")
        self.New_Item_Label = QtWidgets.QLabel(MainWindow)
        self.New_Item_Label.setGeometry(QtCore.QRect(680, 450, 47, 13))
        self.New_Item_Label.setObjectName("New_Item_Label")
        self.groupBox = QtWidgets.QGroupBox(MainWindow)
        self.groupBox.setGeometry(QtCore.QRect(420, 170, 291, 91))
        self.groupBox.setObjectName("groupBox")
        self.Check_In_Box = QtWidgets.QRadioButton(self.groupBox)
        self.Check_In_Box.setGeometry(QtCore.QRect(70, 60, 82, 17))
        self.Check_In_Box.setObjectName("Check_In_Box")
        self.Check_Out_Box = QtWidgets.QRadioButton(self.groupBox)
        self.Check_Out_Box.setGeometry(QtCore.QRect(170, 60, 82, 17))
        self.Check_Out_Box.setObjectName("Check_Out_Box")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        __sortingEnabled = self.New_Item_List.isSortingEnabled()
        self.New_Item_List.setSortingEnabled(False)
        item = self.New_Item_List.item(0)
        item.setText(_translate("MainWindow", "Asset"))
        self.New_Item_List.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.Existing_Item_list.isSortingEnabled()
        self.Existing_Item_list.setSortingEnabled(False)
        item = self.Existing_Item_list.item(0)
        item.setText(_translate("MainWindow", "Asset"))
        self.Existing_Item_list.setSortingEnabled(__sortingEnabled)
        self.Cancel_Button.setText(_translate("MainWindow", "Cancel"))
        self.Done_Button.setText(_translate("MainWindow", "Done"))
        self.Employee_ID_Label.setText(_translate("MainWindow", "Employee ID"))
        self.Action_To_Perform_Label.setText(_translate("MainWindow", "Action to perform?"))
        self.Employee_ID_Enter.setText(_translate("MainWindow", "ENTER"))
        self.Asset_ID_Enter.setText(_translate("MainWindow", "Asset #"))
        self.Asset_ID_Label.setText(_translate("MainWindow", "Asset #"))
        self.Existing_Item_Label.setText(_translate("MainWindow", "Currently Assigned Items:"))
        self.New_Item_Label.setText(_translate("MainWindow", "New Items"))
        self.groupBox.setTitle(_translate("MainWindow", "Action to Perform?"))
        self.Check_In_Box.setText(_translate("MainWindow", "Check IN"))
        self.Check_Out_Box.setText(_translate("MainWindow", "Check OUT"))
