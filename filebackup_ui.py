# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filebackup.ui'
#
# Created: Sun Feb 24 12:27:52 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(408, 347)
        self.backupFiles = QtGui.QRadioButton(Dialog)
        self.backupFiles.setGeometry(QtCore.QRect(30, 10, 108, 26))
        self.backupFiles.setObjectName(_fromUtf8("backupFiles"))
        self.backupDir = QtGui.QRadioButton(Dialog)
        self.backupDir.setGeometry(QtCore.QRect(150, 10, 151, 26))
        self.backupDir.setObjectName(_fromUtf8("backupDir"))
        self.lineEdit_file = QtGui.QLineEdit(Dialog)
        self.lineEdit_file.setGeometry(QtCore.QRect(30, 40, 251, 31))
        self.lineEdit_file.setObjectName(_fromUtf8("lineEdit_file"))
        self.listWidget_files = QtGui.QListWidget(Dialog)
        self.listWidget_files.setGeometry(QtCore.QRect(30, 80, 341, 141))
        self.listWidget_files.setObjectName(_fromUtf8("listWidget_files"))
        self.browserButton1 = QtGui.QPushButton(Dialog)
        self.browserButton1.setGeometry(QtCore.QRect(290, 40, 81, 31))
        self.browserButton1.setObjectName(_fromUtf8("browserButton1"))
        self.radioButton_local = QtGui.QRadioButton(Dialog)
        self.radioButton_local.setGeometry(QtCore.QRect(150, 230, 121, 26))
        self.radioButton_local.setChecked(True)
        self.radioButton_local.setObjectName(_fromUtf8("radioButton_local"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 230, 121, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.radioButton_dropbox = QtGui.QRadioButton(Dialog)
        self.radioButton_dropbox.setGeometry(QtCore.QRect(270, 230, 91, 26))
        self.radioButton_dropbox.setObjectName(_fromUtf8("radioButton_dropbox"))
        self.lineEdit_loc = QtGui.QLineEdit(Dialog)
        self.lineEdit_loc.setGeometry(QtCore.QRect(30, 260, 251, 31))
        self.lineEdit_loc.setObjectName(_fromUtf8("lineEdit_loc"))
        self.browserButton2 = QtGui.QPushButton(Dialog)
        self.browserButton2.setGeometry(QtCore.QRect(290, 260, 81, 31))
        self.browserButton2.setObjectName(_fromUtf8("browserButton2"))
        self.browserButton3 = QtGui.QPushButton(Dialog)
        self.browserButton3.setGeometry(QtCore.QRect(264, 300, 111, 31))
        self.browserButton3.setObjectName(_fromUtf8("browserButton3"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "FileBackup", None))
        self.backupFiles.setText(_translate("Dialog", "Backup Files", None))
        self.backupDir.setText(_translate("Dialog", "Backup Directory", None))
        self.lineEdit_file.setText(_translate("Dialog", "Select Files or Folders..", None))
        self.browserButton1.setText(_translate("Dialog", "Browse", None))
        self.radioButton_local.setText(_translate("Dialog", "Local Backup", None))
        self.label.setText(_translate("Dialog", "Backup Location:", None))
        self.radioButton_dropbox.setText(_translate("Dialog", "Dropbox", None))
        self.lineEdit_loc.setText(_translate("Dialog", "Select location for Backup..", None))
        self.browserButton2.setText(_translate("Dialog", "Browse", None))
        self.browserButton3.setText(_translate("Dialog", "Create Backup", None))

