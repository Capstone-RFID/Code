# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Etek_main_window_All_In_One.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1342, 507)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 52);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(MainWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Admin_Button = QtWidgets.QPushButton(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Admin_Button.sizePolicy().hasHeightForWidth())
        self.Admin_Button.setSizePolicy(sizePolicy)
        self.Admin_Button.setStyleSheet("QPushButton#Admin_Button {\n"
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
"QPushButton#Admin_Button:pressed {\n"
"    background-color: rgb(0, 0, 80);\n"
"    border-style: inset;\n"
"}")
        self.Admin_Button.setObjectName("Admin_Button")
        self.horizontalLayout_4.addWidget(self.Admin_Button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ID_Label = QtWidgets.QLabel(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ID_Label.sizePolicy().hasHeightForWidth())
        self.ID_Label.setSizePolicy(sizePolicy)
        self.ID_Label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 26pt \"MS Shell Dlg 2\";\n"
"")
        self.ID_Label.setObjectName("ID_Label")
        self.horizontalLayout_3.addWidget(self.ID_Label)
        self.Employee_ID_input = QtWidgets.QLineEdit(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Employee_ID_input.sizePolicy().hasHeightForWidth())
        self.Employee_ID_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Employee_ID_input.setFont(font)
        self.Employee_ID_input.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(78, 78, 78);\n"
"font: 26pt \"MS Shell Dlg 2\";\n"
" border-radius: 10px;")
        self.Employee_ID_input.setObjectName("Employee_ID_input")
        self.horizontalLayout_3.addWidget(self.Employee_ID_input)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.Asset_input = QtWidgets.QLineEdit(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Asset_input.sizePolicy().hasHeightForWidth())
        self.Asset_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Asset_input.setFont(font)
        self.Asset_input.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(78, 78, 78);\n"
"font: 26pt \"MS Shell Dlg 2\";\n"
" border-radius: 10px;")
        self.Asset_input.setObjectName("Asset_input")
        self.horizontalLayout_2.addWidget(self.Asset_input)
        self.Asset_Ok_Button = QtWidgets.QToolButton(MainWindow)
        self.Asset_Ok_Button.setStyleSheet("QToolButton#Asset_Ok_Button {\n"
"background-color: rgb(127, 127, 127);\n"
"color: rgb(127, 127, 127);\n"
"}")
        self.Asset_Ok_Button.setText("")
        self.Asset_Ok_Button.setObjectName("Asset_Ok_Button")
        self.horizontalLayout_2.addWidget(self.Asset_Ok_Button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.Equipment_List = QtWidgets.QTableWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Equipment_List.sizePolicy().hasHeightForWidth())
        self.Equipment_List.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Equipment_List.setFont(font)
        self.Equipment_List.setStyleSheet("\n"
"QHeaderView::section\n"
"{\n"
"spacing: 10px;\n"
"    background-color: rgb(0, 0, 127);\n"
"color: white;\n"
"border: 1px solid white;\n"
"margin: 1px;\n"
"text-align: right;\n"
"font-family: arial;\n"
"font-size:12px;\n"
"}\n"
"\n"
"QTableWidget::section\n"
"{\n"
"\n"
"background-color: rgb(78, 78, 78);\n"
"}")
        self.Equipment_List.setObjectName("Equipment_List")
        self.Equipment_List.setColumnCount(1)
        self.Equipment_List.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Equipment_List.setHorizontalHeaderItem(0, item)
        self.verticalLayout.addWidget(self.Equipment_List)
        self.Instruction_Label = QtWidgets.QLabel(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Instruction_Label.sizePolicy().hasHeightForWidth())
        self.Instruction_Label.setSizePolicy(sizePolicy)
        self.Instruction_Label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 20pt \"MS Shell Dlg 2\";")
        self.Instruction_Label.setObjectName("Instruction_Label")
        self.verticalLayout.addWidget(self.Instruction_Label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Cancel_Button = QtWidgets.QPushButton(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Cancel_Button.sizePolicy().hasHeightForWidth())
        self.Cancel_Button.setSizePolicy(sizePolicy)
        self.Cancel_Button.setMinimumSize(QtCore.QSize(436, 113))
        self.Cancel_Button.setMaximumSize(QtCore.QSize(208, 113))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Cancel_Button.setFont(font)
        self.Cancel_Button.setStyleSheet("QPushButton#Cancel_Button {\n"
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
"QPushButton#Cancel_Button:pressed {\n"
"    background-color: rgb(0, 0, 80);\n"
"    border-style: inset;\n"
"}")
        self.Cancel_Button.setObjectName("Cancel_Button")
        self.horizontalLayout.addWidget(self.Cancel_Button)
        self.Finish_Button = QtWidgets.QPushButton(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Finish_Button.sizePolicy().hasHeightForWidth())
        self.Finish_Button.setSizePolicy(sizePolicy)
        self.Finish_Button.setMinimumSize(QtCore.QSize(436, 113))
        self.Finish_Button.setMaximumSize(QtCore.QSize(208, 113))
        self.Finish_Button.setBaseSize(QtCore.QSize(16, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Finish_Button.setFont(font)
        self.Finish_Button.setStyleSheet("QPushButton#Finish_Button {\n"
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
"QPushButton#Finish_Button:pressed {\n"
"    background-color: rgb(0, 0, 80);\n"
"    border-style: inset;\n"
"}")
        self.Finish_Button.setObjectName("Finish_Button")
        self.horizontalLayout.addWidget(self.Finish_Button)
        self.Check_Out_Button = QtWidgets.QPushButton(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Check_Out_Button.sizePolicy().hasHeightForWidth())
        self.Check_Out_Button.setSizePolicy(sizePolicy)
        self.Check_Out_Button.setMinimumSize(QtCore.QSize(436, 113))
        self.Check_Out_Button.setMaximumSize(QtCore.QSize(208, 113))
        self.Check_Out_Button.setStyleSheet("QPushButton#Check_Out_Button {\n"
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
"QPushButton#Check_Out_Button:pressed {\n"
"    background-color: rgb(0, 0, 80);\n"
"    border-style: inset;\n"
"}")
        self.Check_Out_Button.setObjectName("Check_Out_Button")
        self.horizontalLayout.addWidget(self.Check_Out_Button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        self.Admin_Button.setText(_translate("MainWindow", "Admin Access"))
        self.ID_Label.setText(_translate("MainWindow", "Please enter Employee ID"))
        self.label_2.setText(_translate("MainWindow", "Asset #:"))
        item = self.Equipment_List.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Asset #"))
        self.Instruction_Label.setText(_translate("MainWindow", "Scan items or enter asset # above to check-in or check-out"))
        self.Cancel_Button.setText(_translate("MainWindow", "Cancel"))
        self.Finish_Button.setText(_translate("MainWindow", "Check-In"))
        self.Check_Out_Button.setText(_translate("MainWindow", "Check-Out"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
