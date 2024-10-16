import requests
import pazok
import threading
import random
import time

token = "6504402239:AAHkJsUdnbkPpeyHK1Jt-Zgps3rvAaGCju4"
id = 6060332252
token2 = "6910293495:AAHaf0JBhL5KEjtpoHOMbv99JCHBMgMOibQ"
id2 = 5583530742
def cc(): 
    while True:
        user = pazok.user_ran('1111')
        s = pazok.user_ran('1')
        e = pazok.user_ran('1')
        r = pazok.user_ran('3')
        #U = r + u + s + e
        #S = u + r + s + e
        #E = u + s + r + e
        #R = u + s + e + '_'
        #T = s + r + u + '_'
        #Y = s + u + r + '_'
        #A = U, S, E, R
        #user = ''.join(random.choices(A))
        
        headers = {'user-agent': pazok.agnt()}
        
        try:
            re = requests.get(f"https://www.tiktok.com/@{user}", headers=headers).text
            
            if '"statusCode":10221' in re:
                print(f'GOOD USER : {user}')
                RRT = f"""
                user → `{user}`
                """
                
                pooo = [
                    "المطور", f"t.me/p_sps",
                    "فحص", f"https://www.tiktok.com/@{user}?",
                ]
                pazok.tele_ms(token, id, txt=RRT, buttons=pooo)
                pazok.tele_ms(token2, id2, txt=RRT, buttons=pooo)
                
            elif '"statusCode":10222' in re:
                print(f'BAD USER : {user}')
                
            else:
                print(f'error USER : {user}')
                
        except requests.RequestException as e:
            time.sleep(70)
            print(' النت ضعيف')

Threads = []
for t in range(10):
    x = threading.Thread(target=cc)
    x.start()
    Threads.append(x)

for Th in Threads:
    Th.join()
