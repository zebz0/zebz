import requests
import pazok
import threading
import random
import time
import re
token = "7120744671:AAEhbPH2Q9asoEQYO1wwWJZCUOlFiXHKlpY" #توكنك
id = 5593254184
#ايديك ↑
def cc(): 
    while True:
        b='_.'
        a="qwertyuioplkjhgfdsamnbvcxz1234567890"
        u=''.join(random.choices(a))
        s=''.join(random.choices(a))
        e=''.join(random.choices(a))
        r=''.join(random.choices(b))
        t=''.join(random.choices(a))
        U = r+e+s+u
        S = e+r+s+u
        E = e+s+r+u
        R = e+s+u+'_'
        T = u+s+e+t
        Y = u+u+s+e
        y = u+s+u+e
        I = u+s+e+u
        O = s+u+e+u
        P = s+e+u+u
        A = r+r+u+s
        S = r+u+r+s
        USER = U, S, E, R, T, Y, y, I, O, P, A, S
        user =''.join(random.choices(USER))
        #user = "uev_"
        
        
        headers = {'user-agent': pazok.agnt()}
        
        try:
            re = requests.get(f"https://www.tiktok.com/@{user}", headers=headers).text
            
            if '"statusCode":10221' in re:
                print(f'GOOD USER : {user}')
                RRT = f"""
                user → `{user}`
                """
                
                pooo = [
                    "المطور", f"t.me/justboy",
                    "فحص", f"https://www.tiktok.com/@{user}?",
                ]
                pazok.tele_ms(token, id, txt=RRT, buttons=pooo)
                
            elif '"statusCode":10222' in re:
                print(f'BAD USER : {user}')
                
            else:
                print(f'error USER : {user}')
                
        except requests.RequestException as e:
            time.sleep(70)
            print(' النت ضعيف')

Threads = []
for t in range(5):
    x = threading.Thread(target=cc)
    x.start()
    Threads.append(x)
for Th in Threads:
    Th.join()
