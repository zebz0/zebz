import requests, pazok, threading,random
import time
from time import sleep
import os
token = "6974902819:AAF6Np8LxvbAWCtl512_6xsnvW4fmrhMGHM"
id = '6476911978'

bad=0
good=0
live=0
banned=0
O = '\x1b[38;5;208m'  # برتقالي
L = "\033[1;95m"  # ارجواني
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
Z1 = '\033[2;31m'  # احمر ثاني
F = '\033[2;32m'  # اخضر
A = '\033[2;39m'  # ازرق
C = '\033[2;35m'  # وردي
B = '\033[2;36m'  # سماوي
Y = '\033[1;34m'  # ازرق فاتح
T = "\033[1;97m"  # ابيض

def check(user):	
	headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7',
    'referer': 'https://www.instagram.com/mzgeen_math/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-asbd-id': '129477',
    'x-csrftoken': '3fJLs0ttK0xGD4N44h8dBrXEu1GKtpVy',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-requested-with': 'XMLHttpRequest',
}
	params = {
	    'username': user,
	}
	
	response = requests.get(
	    'https://www.instagram.com/api/v1/users/web_profile_info/',
	    params=params,
	    headers=headers,
	).status_code
	if response == 404:
	    global banned
	    banned+=1
	    print(f"{F}14days Banned @{user} ")
	    RRT = f"BAN USER INSTAGRAM\n\nuser → `{user}`\n"
	    pooo = ["فحص", f"instagram.com/{user}"]
	    pazok.tele_ms(token, id, txt=RRT, buttons=pooo)
	elif response == 200:
	    global live
	    live+=1
	    print(f"{X}14days Live @{user} ")    
	else:
	    print('Exists ')
 
def cc():
    while True:
        a = "".join(random.choice('qwertyuiopasdfghjklzxcvbnm1234567890') for i in range(1))
        b = "".join(random.choice('qwertyuiopasdfghjklzxcvbnm1234567890') for i in range(1))
        c = "".join(random.choice('qwertyuiopasdfghjklzxcvbnm1234567890') for i in range(1))
        d = "".join(random.choice('qwertyuiopasdfghjklzxcvbnm1234567890') for i in range(1))
        user = a+'_'+b+b+b
        #ser = "btttb"
        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'ar-US,ar;q=0.9,es-US;q=0.8,es;q=0.7,en-US;q=0.6,en;q=0.5',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/emailsignup/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'x-asbd-id': '129477',
            'x-csrftoken': 'ytgAvZRmGBmuNAcC9OTOr7N4PeOmyp1v',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-instagram-ajax': '1016981577',
            'x-requested-with': 'XMLHttpRequest',
        }
        
        data = {
            'username': user,
            'client_id': 'Zt6i7gABAAFIGL1bi4PB-M-S2bUz',
            'seamless_login_enabled': '1',
            'opt_into_one_tap': 'false',
            'use_new_suggested_user_name': 'true',
        }
        
        
        
        re = requests.post('https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/', headers=headers,data=data).text
        global good,bad,live,banned
        if '"code": "username_held_by_others"}], "__all__": [{"message"' in re:
            check(user)
        elif '"email_required"}], "__all__"' in re:
            os.system('clear||cls')
            good+=1
            print(f" 14days Banned : {banned}\n 14days Live : {live}\n Avalible User : {good}\n Bad User : {bad}\n User : {user}")
            RRT = f"GOOD USER INSTAGRAM\n\nuser → `{user}`\n"
            pooo = ["المطور", f"t.me/p_sps"]
            pazok.tele_ms(token, id, txt=RRT, buttons=pooo)
        elif '"spam":true' in re:
            print('VPN', end='\r')
        else:
            bad+=1
            os.system('clear||cls')
            print(f" 14days Banned : {banned}\n 14days Live : {live}\n Avalible User : {good}\n Bad User : {bad}\n User : {user}")    
            
Threads = []
for t in range(30):
    x = threading.Thread(target=cc)
    x.start()
    Threads.append(x)
for Th in Threads:
    Th.join()
