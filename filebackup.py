#!/usr/bin/python -d
#QProgressBar is not that hard. you instantiate it. you setMinimum and setMaximum as you like and the do setValue everytime you want to update
import sys, os, time, subprocess
from PyQt4 import QtCore, QtGui
from filebackup_ui import Ui_Dialog
from dropbox import  rest, session
from dropbox import client as dbclient
import webbrowser

class MyForm(QtGui.QMainWindow):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_Dialog()
    self.dialog = QtGui.QDialog(parent)
    self.ui.setupUi(self)
    
    QtCore.QObject.connect(self.ui.browserButton1, QtCore.SIGNAL("clicked()"), self.selectFile )
    QtCore.QObject.connect(self.ui.browserButton2, QtCore.SIGNAL("clicked()"), self.backupOption )
    QtCore.QObject.connect(self.ui.browserButton3, QtCore.SIGNAL("clicked()"), self.createBackup )

  filelist = []
  dirLoc = ""
  def selectFile(self):
    if self.ui.backupFiles.isChecked():
	tempList = QtGui.QFileDialog.getOpenFileNames(self, "Select Files to Backup")
	for elem in tempList:
		self.filelist.append(elem)
	self.ui.lineEdit_file.setText(str(self.filelist[1]))
	self.ui.listWidget_files.addItems(tempList)
	
    else: 
	dirAdd = QtGui.QFileDialog.getExistingDirectory(self, "Select Directory to Backup")
	self.filelist.append(dirAdd)
	self.ui.lineEdit_file.setText(dirAdd)
  	self.ui.listWidget_files.addItem(dirAdd)

  def dropboxControl(self):
    # Get your app key and secret from the Dropbox developer website
    APP_KEY = '7vgzlflg18n669z'
    APP_SECRET = 'vkt69dsslslegu5'

# ACCESS_TYPE should be 'dropbox' or 'app_folder' as configured for your app
    ACCESS_TYPE = 'app_folder'
    sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)

    request_token = sess.obtain_request_token()
# Make the user sign in and authorize this token
    url = sess.build_authorize_url(request_token)
    webbrowser.open(url)
    QtGui.QMessageBox.about(self, 'Dropbox Connection', 'Press OK when authorised in Browser window')
    access_token = sess.obtain_access_token(request_token)
    client = dbclient.DropboxClient(sess)
    self.ui.lineEdit_loc.setText(str("Account Owner: " + client.account_info()[u'display_name']))

#{u'referral_link': u'https://www.dropbox.com/referrals/NTMyNTU0NjA5', u'display_name': u'vikash bajaj', u'uid': 3255460, u'country': u'IN', u'quota_info': {u'shared': 9376, u'quota': 19595788288, u'normal': 1680501980}, u'email': u'contactvikashbajaj@gmail.com'}


  def backupOption(self):
    if self.ui.radioButton_local.isChecked():
	self.ui.lineEdit_loc.setText(str("Select Directory to Backup"))
	self.ui.browserButton2.setText(str("Browse"))
	self.selectLoc()
    elif self.ui.radioButton_dropbox.isChecked():
	self.ui.lineEdit_loc.setText(str("Dropbox Account.."))
	self.ui.browserButton2.setText(str("Add"))
	self.dropboxControl()
  def selectLoc(self):
	self.dirLoc = QtGui.QFileDialog.getExistingDirectory(self, "Select Location for Backup")
    	self.ui.lineEdit_loc.setText(self.dirLoc)

  def createBackup(self):
	cmd_list = []
	cmd_list.append("zip")
	cmd_list.append("-r")
	dirLocation = self.dirLoc + os.sep + "backup@" + time.strftime('%Y%m%d') + ".zip"
	cmd_list.append(dirLocation)
	for elem in self.filelist:
		cmd_list.append(elem)
	if subprocess.call(cmd_list)==0:
		QtGui.QMessageBox.about(self, 'File Backup', 'Backup Succesfully Created') 
		self.ui.listWidget_files.clear()
		self.ui.lineEdit_file.setText("Select location for Backup..")
		self.ui.lineEdit_loc.setText("Select location for Backup..")
	else:
		QtGui.QMessageBox.about(self, 'File Backup', 'Backup Failed') 

if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  myapp = MyForm()
  myapp.show()
  sys.exit(app.exec_())
