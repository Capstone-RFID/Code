# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'password_change_prompt.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PasswordChangeDialog(object):
    def setupUi(self, PasswordChangeDialog):
        PasswordChangeDialog.setObjectName("PasswordChangeDialog")
        PasswordChangeDialog.resize(882, 238)
        PasswordChangeDialog.setStyleSheet("background-color: #5a5c5e;")
        self.horizontalLayout = QtWidgets.QHBoxLayout(PasswordChangeDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(PasswordChangeDialog)
        self.widget.setStyleSheet("QWidget#centralWidget{\n"
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
"}\n"
"QPushButton::pressed{\n"
"    background-color: #577590; \n"
"}\n"
"QPushButton:hover:!pressed{\n"
"    background-color: #739bbe; \n"
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
"")
        self.widget.setObjectName("widget")
        self._2 = QtWidgets.QGridLayout(self.widget)
        self._2.setObjectName("_2")
        self.cancel = QtWidgets.QPushButton(self.widget)
        self.cancel.setMinimumSize(QtCore.QSize(100, 50))
        self.cancel.setObjectName("cancel")
        self._2.addWidget(self.cancel, 6, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self._2.addItem(spacerItem, 7, 1, 1, 1)
        self.CurrentPassword_Field = QtWidgets.QLineEdit(self.widget)
        self.CurrentPassword_Field.setObjectName("CurrentPassword_Field")
        self._2.addWidget(self.CurrentPassword_Field, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self._2.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self._2.addWidget(self.label_4, 3, 1, 1, 1)
        self.NewPassword_Field = QtWidgets.QLineEdit(self.widget)
        self.NewPassword_Field.setMinimumSize(QtCore.QSize(466, 0))
        self.NewPassword_Field.setObjectName("NewPassword_Field")
        self._2.addWidget(self.NewPassword_Field, 4, 1, 1, 1)
        self.CurrentPassword_Label = QtWidgets.QLabel(self.widget)
        self.CurrentPassword_Label.setObjectName("CurrentPassword_Label")
        self._2.addWidget(self.CurrentPassword_Label, 2, 0, 1, 1)
        self.ConfirmPassword_Label = QtWidgets.QLabel(self.widget)
        self.ConfirmPassword_Label.setObjectName("ConfirmPassword_Label")
        self._2.addWidget(self.ConfirmPassword_Label, 5, 0, 1, 1)
        self.NewPassword_Label = QtWidgets.QLabel(self.widget)
        self.NewPassword_Label.setObjectName("NewPassword_Label")
        self._2.addWidget(self.NewPassword_Label, 4, 0, 1, 1)
        self.ConfirmPassword_Field = QtWidgets.QLineEdit(self.widget)
        self.ConfirmPassword_Field.setObjectName("ConfirmPassword_Field")
        self._2.addWidget(self.ConfirmPassword_Field, 5, 1, 1, 1)
        self.ok = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok.sizePolicy().hasHeightForWidth())
        self.ok.setSizePolicy(sizePolicy)
        self.ok.setMinimumSize(QtCore.QSize(100, 50))
        self.ok.setObjectName("ok")
        self._2.addWidget(self.ok, 6, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self._2.addItem(spacerItem1, 5, 4, 1, 1)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(PasswordChangeDialog)
        QtCore.QMetaObject.connectSlotsByName(PasswordChangeDialog)

    def retranslateUi(self, PasswordChangeDialog):
        _translate = QtCore.QCoreApplication.translate
        PasswordChangeDialog.setWindowTitle(_translate("PasswordChangeDialog", "Change Password"))
        self.cancel.setText(_translate("PasswordChangeDialog", "Cancel"))
        self.label_2.setText(_translate("PasswordChangeDialog", "Please enter the old password"))
        self.label_4.setText(_translate("PasswordChangeDialog", "Enter the new password twice and press ok to change it"))
        self.CurrentPassword_Label.setText(_translate("PasswordChangeDialog", "Current Password"))
        self.ConfirmPassword_Label.setText(_translate("PasswordChangeDialog", "Confirm Password"))
        self.NewPassword_Label.setText(_translate("PasswordChangeDialog", "New Password"))
        self.ok.setText(_translate("PasswordChangeDialog", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PasswordChangeDialog = QtWidgets.QWidget()
    ui = Ui_PasswordChangeDialog()
    ui.setupUi(PasswordChangeDialog)
    PasswordChangeDialog.show()
    sys.exit(app.exec_())
