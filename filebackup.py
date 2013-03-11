#!/usr/bin/python -d

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
###########added#########  
    self.ui.radioButton_local.toggled.connect(self.radio1_clicked)
    self.ui.radioButton_dropbox.toggled.connect(self.radio2_clicked)

  def radio1_clicked(self, enabled):
        if enabled:
            self.ui.lineEdit_loc.setText('Select Files to Backup')
            self.ui.browserButton2.setText(str("Browse"))
  def radio2_clicked(self, enabled):
        if enabled:
            self.ui.lineEdit_loc.setText(str("Dropbox Account.."))
	    self.ui.browserButton2.setText(str("Add"))
############################
  filelist = []
  dirLoc = ""
  def selectFile(self):
    if self.ui.backupFiles.isChecked():
	tempList = QtGui.QFileDialog.getOpenFileNames(self, "Select Files to Backup")
	for elem in tempList:
		self.filelist.append(str(elem))
	self.ui.lineEdit_file.setText(str(self.filelist[-1]))
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
    token_key=""
    token_secret=""
    if open("access-token.txt").read()!="":
    	token_file = open("access-token.txt")
	token_key,token_secret = token_file.read().split('|')
	token_file.close()
        sess = session.DropboxSession(APP_KEY,APP_SECRET, ACCESS_TYPE )
	sess.set_token(token_key,token_secret)
	client = dbclient.DropboxClient(sess)
	try:
		accCheck = client.account_info()[u'display_name']
	except Exception as e:
		print e
		print e.message
		if e.message.split(" ")[0]=="[401]":
			print "hello"
			token_key=""
			token_secret=""
			f = open('access-token.txt', 'r+') 
			f.truncate()
			f.close()
		elif e.message=='Error connecting to "api.dropbox.com": [Errno 104] Connection reset by peer' or e.message=='Error connecting to "api.dropbox.com": [Errno -2] Name or service not known':
			QtGui.QMessageBox.about(self, 'Problem Connecting', 'Please check your internet connection or try creating a local backup')
    if token_key=="" and token_secret=="":
    	request_token = sess.obtain_request_token()
        url = sess.build_authorize_url(request_token)
	webbrowser.open(url)
        QtGui.QMessageBox.about(self, 'Dropbox Connection', 'Press OK when authorised in Browser window')
        access_token = sess.obtain_access_token(request_token)
	token_file = open("access-token.txt", "wb")
	token_file.write(access_token.key+ "|" + access_token.secret)
        token_file.close()
        client = dbclient.DropboxClient(sess)
        
    
    
    #self.ui.lineEdit_loc.setText(str("Account: " + client.account_info()[u'display_name']))


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
	cmd_list.append("location")
	for elem in self.filelist:
		cmd_list.append(elem)
		print elem
	if self.ui.radioButton_local.isChecked():
		dirLocation = self.dirLoc + os.sep + "backup@" + time.strftime('%Y%m%d') + ".zip"
		cmd_list[2] = str(dirLocation)
		print cmd_list
		if subprocess.call(cmd_list)==0:
			QtGui.QMessageBox.about(self, 'File Backup', 'Backup Succesfully Created') 
			self.ui.listWidget_files.clear()
			self.ui.lineEdit_file.setText("Select location for Backup..")
			self.ui.lineEdit_loc.setText("Select location for Backup..")
		else:
			QtGui.QMessageBox.about(self, 'File Backup', 'Please choose a different location for backup')
	elif self.ui.radioButton_dropbox.isChecked():
		dirLocation = "/tmp" + os.sep + "backup@" + time.strftime('%Y%m%d') + ".zip"
		cmd_list.append(str(dirLocation))
		if subprocess.call(cmd_list)==0:
			file_to_upload = open(dirLocation)
			response = client.put_file(dirLocation, f)
			msg = "uploaded: " + response
			QtGui.QMessageBox.about(self, 'File Backup', msg)
	else:
		QtGui.QMessageBox.about(self, 'File Backup', 'Backup Failed') 

if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  myapp = MyForm()
  myapp.show()
  sys.exit(app.exec_())
