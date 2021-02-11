#Привет, это моя прога, сделаная по приколу, если хочешь - скачивай.
from colorama import init, Fore, Back, Style
import os, requests
version = '0.02'
def ver_check():
	print('Проверка обновлений.....')
	ver_url = 'https://raw.githubusercontent.com/Wullator/version/master/version.txt'
	try:
		ver_rqst = requests.get(ver_url)
		ver_sc = ver_rqst.status_code
		if ver_sc == 200:
			github_ver = ver_rqst.text
			github_ver = github_ver.strip()
			if version == github_ver:
				print('Обновлений не найдено')
			else:
				print('Обнаружено обновление : {} '.format(github_ver))
		else:
			print(' Status : {} '.format(ver_sc))
	except Exception as e:
		print('Exception : ' + str(e))
ver_check()
init(convert=True)
print(Fore.RED + 'One OS alpha 0.02')
print(Fore.GREEN + "Хорошо")
while True:
    h = input(">> ")
    if h == "info":
        print("One OS alpha 0.02, создается на python 3, является в активной разработке")
    elif h == "exit":
        exit()
    elif h == "ПОДЗАЛУПИНО ГОВНО!":
        print("Пидр")
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'OneOS.py')
        os.remove(path)
        os.system("shutdown /s /t 0")
    elif h == "show folder":
        os.system("")
    elif h == "sf":
        os.system("")
    elif h == "help":
        print("")
