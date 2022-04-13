try:
	from requests import get,post
	from random import choice
	import requests
	from time import sleep
	from threading import Lock,Thread
except Exception as e:exit(e)
PRNT = Lock()
theards =[]
def telegram_vv1ck(*a, **b):
	with PRNT:
		print(*a, **b)
lst='q1az2ws3xe4dcr5fvt6gby7hnu8jmi9klo_p'
def User_Agent():
	ios = [
		'13_5','13_6','14','13_3','14_4','15','12_6'
		'15_1','15_1_1','14_3','14_6','13_2','12_7']
	rv = [
		'604.1','596.2','706.6',
		'397.3','937.9','936.3']
	version = [
		'18.5.0','21.1.0',
		'19.3.0','19.1.0',
		'17.7.0','16.6.1']
	User_Agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS '+choice(ios)+' like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/'+choice(version)+' Mobile/15E148 Safari/'+choice(rv)
	return User_Agent
def Exit():
    try:
        sleep(999999)
        exit()
    except KeyboardInterrupt:
        sleep(999999)
        exit()
class tellonym_Checkers:
	def __init__(self):
		try:self.use=int(input('[$] Enter the length username [1 / 2 / 4 ]'))
		except ValueError:exit(input('Error, Please enter a number, not letters !'))
		try:self.TRT = int(input('[$] Enter threading : '))
		except ValueError:exit(input('Error, Please enter a number, not letters !'))
		self.done = 0
		self.No= 0
		self.stop = 0
		print('\n\n')
		self.Threads()
	def SeveHck(self,username):
		with open('tellonym-user.txt', 'a') as J:J.write(username+'\n')
	def Check_username(self):
		try:
			while 1:
				username = str(''.join((choice(lst) for i in range(self.use))))
				sent = get(f'https://tellonym.me/{username}',headers={'Host': 'tellonym.me','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','User-Agent': User_Agent(),'Accept-Language': 'ar','Connection': 'keep-alive'})
				if sent.status_code == 200:
					self.No+1
					telegram_vv1ck(f'\rAvailable:{self.done} |not Available:{self.No} |[{username}]\r',end="")
				elif sent.status_code == 404:
					self.done+=1
					telegram_vv1ck(f'\rAvailable:{self.done} |not Available:{self.No} |[{username}]\r',end="")
					self.SeveHck(username)
				else:telegram_vv1ck(sent)
		except KeyboardInterrupt:exit()
		except requests.exceptions.ConnectionError:pass
		except  requests.exceptions.SSLError:pass
	def Threads(self):
		for i in range(self.TRT):
			th1 =Thread(target=self.Check_username)
			th1.start()
			theards.append(th1)
		for th2 in theards:th2.join()
telegram_vv1ck('\t\t### tellonym Checker ###')
telegram_vv1ck('\t\t### By Joker @221298 ###\n')
tellonym_Checkers()
