# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alreadyCheckedOut.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class checkMsg(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.select_reject = QtWidgets.QDialogButtonBox(Dialog)
        self.select_reject.setGeometry(QtCore.QRect(-80, 150, 341, 32))
        self.select_reject.setOrientation(QtCore.Qt.Horizontal)
        self.select_reject.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.select_reject.setObjectName("select_reject")
        self.ConfirmMessage = QtWidgets.QLabel(Dialog)
        self.ConfirmMessage.setGeometry(QtCore.QRect(60, 40, 251, 81))
        self.ConfirmMessage.setWhatsThis("")
        self.ConfirmMessage.setObjectName("ConfirmMessage")

        self.retranslateUi(Dialog)
        self.select_reject.accepted.connect(Dialog.accept)
        self.select_reject.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ConfirmMessage.setText(_translate("Dialog", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = checkMsg()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
