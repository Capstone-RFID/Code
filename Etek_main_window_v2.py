# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Etek_main_window_v2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 900))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(90, 92, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 92, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 92, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 92, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 92, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 92, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 92, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 92, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 92, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../Balkaran/Pictures/rcmp.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QWidget#centralWidget{\n"
"    background-color: #5a5c5e;\n"
"}\n"
"QWidget#Base{\n"
" color: #5a5c5e;\n"
"}\n"
"\n"
"QLabel{\n"
"    Font: 14pt \"Arial\";\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton{\n"
"    font: 14pt \"Arial\";\n"
"    color: white;\n"
"    background-color: #282c30;\n"
"    border-radius: 5px;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: #577590; \n"
"}\n"
"QPushButton:hover:!pressed{\n"
"    background-color: #739bbe; \n"
"}\n"
"QToolButton:disabled {\n"
"    color:  #5a5c5e;\n"
"    background-color: #5a5c5e;\n"
"}\n"
"QToolButton{\n"
"    font: 14pt \"Arial\";\n"
"    color: white;\n"
"    background-color: #282c30;\n"
"    border-radius: 5px;\n"
"}\n"
"QToolButton::pressed{\n"
"    background-color: #577590; \n"
"}\n"
"QToolButton:hover:!pressed{\n"
"    background-color: #739bbe; \n"
"}\n"
"\n"
"QLineEdit{\n"
"    font: 14pt \"Arial\";\n"
"    background-color: #282c30;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    padding-left: 10;\n"
"}\n"
"\n"
"QComboBox{\n"
"    font: 14pt \"Arial\";\n"
"    color: white;\n"
"    background-color: #282c30;\n"
"    border-radius: 5px;\n"
"    padding-left: 30px;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"    width: 25;\n"
"}\n"
"\n"
"QMessageBox {\n"
"    background-color: #0D1218;\n"
"    Font: 14pt \"Arial\";\n"
"}\n"
"QMessageBox QPushButton {\n"
"    font: 14pt \"Arial\";\n"
"    color: white;\n"
"    background-color: #1e2733    ;\n"
"    border-radius: 5px;\n"
"    height: 40;\n"
"    width: 100;\n"
"}\n"
"\n"
"/*TABLE VIEW */\n"
"QTableView{\n"
"    border-radius: 8;\n"
"    background-color: #3f464d;\n"
"    alternate-background-color: rgb(159, 162, 166);\n"
"    Font: 14pt;\n"
"    color: white;\n"
"    gridline-color: #1C2321;\n"
"}\n"
"\n"
"QTableView:item:selected:focus {background-color: #577590 ;}\n"
"QTableView:item:selected {background-color: #577590 ;}\n"
"\n"
"QTableView QTableCornerButton::section {\n"
"    border-top-left-radius: 8;\n"
"    background-color: #5F6366;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #282c30   ;\n"
"    color: white;\n"
"    font: Bold 14pt;\n"
"    padding: 5;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"QHeaderView::section:checked\n"
"{\n"
"    background-color:#0D1218   ;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border-radius: 2;\n"
"}\n"
"QProgressBar::chunk{\n"
"    background-color:#53a369;\n"
"}\n"
"\n"
"/*SCROLL BAR*/\n"
"QScrollBar:vertical {\n"
"     background:white;\n"
"     width: 10;\n"
"     margin: 0px 0 0px 0;\n"
"     border-radius: 2;\n"
" }\n"
" QScrollBar::handle:vertical {\n"
"     background: #0D1218        ;\n"
"     min-height: 30px;\n"
"    border-radius: 2;\n"
" }\n"
"QScrollBar::add-line:vertical {\n"
"     background: #0D1218  ;\n"
"     height: 0px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     background: #0D1218  ;\n"
"     height: 0px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" ")
        self.gridLayout_2 = QtWidgets.QGridLayout(MainWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.WelcomeMessage = QtWidgets.QHBoxLayout()
        self.WelcomeMessage.setObjectName("WelcomeMessage")
        self.Welcome_to_ETEK_Label = QtWidgets.QLabel(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.Welcome_to_ETEK_Label.setFont(font)
        self.Welcome_to_ETEK_Label.setStyleSheet("font: 75 italic 28pt \"Arial\";")
        self.Welcome_to_ETEK_Label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.Welcome_to_ETEK_Label.setObjectName("Welcome_to_ETEK_Label")
        self.WelcomeMessage.addWidget(self.Welcome_to_ETEK_Label)
        self.Name_Label = QtWidgets.QLabel(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.Name_Label.setFont(font)
        self.Name_Label.setStyleSheet("font: 75 italic 28pt \"Arial\";")
        self.Name_Label.setText("")
        self.Name_Label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.Name_Label.setObjectName("Name_Label")
        self.WelcomeMessage.addWidget(self.Name_Label)
        self.gridLayout.addLayout(self.WelcomeMessage, 0, 2, 1, 5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Existing_Item_list = QtWidgets.QTableWidget(MainWindow)
        self.Existing_Item_list.setMinimumSize(QtCore.QSize(200, 100))
        self.Existing_Item_list.setMaximumSize(QtCore.QSize(600, 500))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 70, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 70, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 70, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 162, 166))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 70, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 70, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 70, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 162, 166))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 70, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 70, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 70, 77))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 162, 166))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.Existing_Item_list.setPalette(palette)
        self.Existing_Item_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.Existing_Item_list.setObjectName("Existing_Item_list")
        self.Existing_Item_list.setColumnCount(1)
        self.Existing_Item_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Existing_Item_list.setHorizontalHeaderItem(0, item)
        self.Existing_Item_list.horizontalHeader().setDefaultSectionSize(225)
        self.Existing_Item_list.horizontalHeader().setStretchLastSection(True)
        self.Existing_Item_list.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.Existing_Item_list)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.New_Item_List = QtWidgets.QTableWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.New_Item_List.sizePolicy().hasHeightForWidth())
        self.New_Item_List.setSizePolicy(sizePolicy)
        self.New_Item_List.setMinimumSize(QtCore.QSize(200, 100))
        self.New_Item_List.setMaximumSize(QtCore.QSize(600, 500))
        self.New_Item_List.setStyleSheet("forground-color: rgb(94, 167, 255)")
        self.New_Item_List.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.New_Item_List.setObjectName("New_Item_List")
        self.New_Item_List.setColumnCount(1)
        self.New_Item_List.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.New_Item_List.setHorizontalHeaderItem(0, item)
        self.New_Item_List.horizontalHeader().setDefaultSectionSize(225)
        self.New_Item_List.horizontalHeader().setStretchLastSection(True)
        self.New_Item_List.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.New_Item_List)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 2, 1, 5)
        self.Employee_Section = QtWidgets.QFrame(MainWindow)
        self.Employee_Section.setMaximumSize(QtCore.QSize(16777215, 100))
        self.Employee_Section.setStyleSheet("")
        self.Employee_Section.setObjectName("Employee_Section")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.Employee_Section)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.Employee_ID_Label = QtWidgets.QLabel(self.Employee_Section)
        self.Employee_ID_Label.setMinimumSize(QtCore.QSize(150, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.Employee_ID_Label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Employee_ID_Label.setFont(font)
        self.Employee_ID_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Employee_ID_Label.setObjectName("Employee_ID_Label")
        self.horizontalLayout_6.addWidget(self.Employee_ID_Label)
        self.Employee_ID_Input = QtWidgets.QLineEdit(self.Employee_Section)
        self.Employee_ID_Input.setMinimumSize(QtCore.QSize(300, 30))
        self.Employee_ID_Input.setMaximumSize(QtCore.QSize(700, 30))
        self.Employee_ID_Input.setMaxLength(9)
        self.Employee_ID_Input.setObjectName("Employee_ID_Input")
        self.horizontalLayout_6.addWidget(self.Employee_ID_Input)
        self.Employee_ID_Enter = QtWidgets.QPushButton(self.Employee_Section)
        self.Employee_ID_Enter.setMinimumSize(QtCore.QSize(150, 30))
        self.Employee_ID_Enter.setMaximumSize(QtCore.QSize(150, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 44, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 44, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 44, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 44, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 44, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 44, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 44, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 44, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 44, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.Employee_ID_Enter.setPalette(palette)
        self.Employee_ID_Enter.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Employee_ID_Enter.setStyleSheet("")
        self.Employee_ID_Enter.setObjectName("Employee_ID_Enter")
        self.horizontalLayout_6.addWidget(self.Employee_ID_Enter)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.gridLayout.addWidget(self.Employee_Section, 1, 2, 1, 5)
        self.Done_Button = QtWidgets.QPushButton(MainWindow)
        self.Done_Button.setMinimumSize(QtCore.QSize(150, 50))
        self.Done_Button.setStyleSheet("")
        self.Done_Button.setObjectName("Done_Button")
        self.gridLayout.addWidget(self.Done_Button, 6, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 6, 4, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.groupBox = QtWidgets.QGroupBox(MainWindow)
        self.groupBox.setMaximumSize(QtCore.QSize(700, 100))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.groupBox.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Check_In_Box = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Check_In_Box.setFont(font)
        self.Check_In_Box.setStyleSheet("QRadioButton{ color: rgb(255, 255, 255); background-color: rgba(255, 255, 255, 0);}")
        self.Check_In_Box.setObjectName("Check_In_Box")
        self.horizontalLayout_2.addWidget(self.Check_In_Box)
        self.Check_Out_Box = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Check_Out_Box.setFont(font)
        self.Check_Out_Box.setStyleSheet("QRadioButton{ color: rgb(255, 255, 255); background-color: rgba(255, 255, 255, 0);}")
        self.Check_Out_Box.setObjectName("Check_Out_Box")
        self.horizontalLayout_2.addWidget(self.Check_Out_Box)
        self.horizontalLayout_9.addWidget(self.groupBox)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout_9, 2, 2, 1, 5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 6, 6, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 2, 1, 5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.Asset_ID_Label = QtWidgets.QLabel(MainWindow)
        self.Asset_ID_Label.setMinimumSize(QtCore.QSize(150, 0))
        self.Asset_ID_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Asset_ID_Label.setObjectName("Asset_ID_Label")
        self.horizontalLayout_7.addWidget(self.Asset_ID_Label)
        self.Asset_ID_Input = QtWidgets.QLineEdit(MainWindow)
        self.Asset_ID_Input.setMinimumSize(QtCore.QSize(300, 30))
        self.Asset_ID_Input.setMaximumSize(QtCore.QSize(700, 30))
        self.Asset_ID_Input.setText("")
        self.Asset_ID_Input.setMaxLength(8)
        self.Asset_ID_Input.setObjectName("Asset_ID_Input")
        self.horizontalLayout_7.addWidget(self.Asset_ID_Input)
        self.Asset_ID_Enter = QtWidgets.QPushButton(MainWindow)
        self.Asset_ID_Enter.setMinimumSize(QtCore.QSize(150, 30))
        self.Asset_ID_Enter.setMaximumSize(QtCore.QSize(150, 50))
        self.Asset_ID_Enter.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Asset_ID_Enter.setStyleSheet("")
        self.Asset_ID_Enter.setObjectName("Asset_ID_Enter")
        self.horizontalLayout_7.addWidget(self.Asset_ID_Enter)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 2, 1, 5)
        self.Cancel_Button = QtWidgets.QPushButton(MainWindow)
        self.Cancel_Button.setMinimumSize(QtCore.QSize(150, 50))
        self.Cancel_Button.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Cancel_Button.setStyleSheet("")
        self.Cancel_Button.setObjectName("Cancel_Button")
        self.gridLayout.addWidget(self.Cancel_Button, 6, 3, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 6, 7, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 6, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Remove_Button = QtWidgets.QToolButton(MainWindow)
        self.Remove_Button.setMinimumSize(QtCore.QSize(20, 20))
        self.Remove_Button.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Remove_Button.setStyleSheet("")
        self.Remove_Button.setObjectName("Remove_Button")
        self.verticalLayout_2.addWidget(self.Remove_Button)
        self.Mark_Button = QtWidgets.QToolButton(MainWindow)
        self.Mark_Button.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Mark_Button.setStyleSheet("")
        self.Mark_Button.setObjectName("Mark_Button")
        self.verticalLayout_2.addWidget(self.Mark_Button)
        self.gridLayout.addLayout(self.verticalLayout_2, 5, 7, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem11)
        self.Admin_Button = QtWidgets.QToolButton(MainWindow)
        self.Admin_Button.setMinimumSize(QtCore.QSize(250, 30))
        self.Admin_Button.setMaximumSize(QtCore.QSize(50, 25))
        self.Admin_Button.setObjectName("Admin_Button")
        self.horizontalLayout_8.addWidget(self.Admin_Button)
        self.gridLayout.addLayout(self.horizontalLayout_8, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.Help_Button = QtWidgets.QPushButton(MainWindow)
        self.Help_Button.setMinimumSize(QtCore.QSize(100, 50))
        self.Help_Button.setObjectName("Help_Button")
        self.horizontalLayout_4.addWidget(self.Help_Button)
        self.gridLayout.addLayout(self.horizontalLayout_4, 6, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Employee_ID_Input, self.Check_Out_Box)
        MainWindow.setTabOrder(self.Check_Out_Box, self.Asset_ID_Input)
        MainWindow.setTabOrder(self.Asset_ID_Input, self.Done_Button)
        MainWindow.setTabOrder(self.Done_Button, self.Remove_Button)
        MainWindow.setTabOrder(self.Remove_Button, self.Employee_ID_Enter)
        MainWindow.setTabOrder(self.Employee_ID_Enter, self.Asset_ID_Enter)
        MainWindow.setTabOrder(self.Asset_ID_Enter, self.Cancel_Button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        self.Welcome_to_ETEK_Label.setText(_translate("MainWindow", "Welcome to E-TEK,"))
        item = self.Existing_Item_list.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Currently Assigned Assets"))
        item = self.New_Item_List.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Assets"))
        self.Employee_ID_Label.setText(_translate("MainWindow", "Employee ID:"))
        self.Employee_ID_Enter.setText(_translate("MainWindow", "Enter"))
        self.Done_Button.setText(_translate("MainWindow", "Done"))
        self.groupBox.setTitle(_translate("MainWindow", "Action to Perform?"))
        self.Check_In_Box.setText(_translate("MainWindow", "Check IN"))
        self.Check_Out_Box.setText(_translate("MainWindow", "Check OUT"))
        self.Asset_ID_Label.setText(_translate("MainWindow", "Asset #:"))
        self.Asset_ID_Enter.setText(_translate("MainWindow", "Enter"))
        self.Cancel_Button.setText(_translate("MainWindow", "Cancel"))
        self.Remove_Button.setText(_translate("MainWindow", "Remove Item"))
        self.Mark_Button.setText(_translate("MainWindow", "Mark Broken"))
        self.Admin_Button.setText(_translate("MainWindow", "Administrator Access"))
        self.Help_Button.setText(_translate("MainWindow", "Help"))
