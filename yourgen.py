import time, os, secrets, random, threading, requests, sys
from colorama import Fore, Style, init
from threading import Thread
from httpx import Client
from httpx_socks import SyncProxyTransport
from hfuck import Bypass

sys.dont_write_bytecode = True

class Info:


    def cls():  os.system('cls' if os.name == 'nt' else 'clear')

    cls()

    def Title(message):
        title = ''
        for char in message: title += char;os.system(f'title {title}');time.sleep(0.018)

    def write(text): 
        for x in text: print('' + x, end="");sys.stdout.flush();time.sleep(0.009)

    genned = 0
    bypassed = 0

    def title():
        global genned, bypassed
        while True: os.system(f'title Your-Gen.xyz - Token Gen 🚀: {Info.genned} ^| Captcha ✔️: {Info.bypassed} ^| yatsuu#0020')
            

class Menu:
    

    color = f'{Fore.CYAN}{Style.BRIGHT}'
    os.system('mode 100, 24')
    Info.Title('Your-Gen.xyz 🚀 - Generator Menu')
    Info.cls()
    print(f'\n\t\t\t\t\u001b[38;5;50m╦ ╦╔═╗╦ ╦╦═╗   ╔═╗╔═╗╔╗╔\n\t\t\t\t\u001b[38;5;50m╚╦╝║ ║║ ║╠╦╝───║ ╦║╣ ║║║\n\t\t\t\t\u001b[38;5;50m ╩ ╚═╝╚═╝╩╚═   ╚═╝╚═╝╝╚╝{Fore.RESET}\n\n\n')
    
    proxytype = 'http'
    Info.write(f"{color}>{Fore.RESET} Token Pseudo{color}:{Fore.RESET} ")
    username = input()
    Info.write(f"{color}>{Fore.RESET} Discord Invite{color}:{Fore.RESET} discord.gg/")
    invite = input()
    Info.write(f'{color}>{Fore.RESET} Nombre de Token{color}:{Fore.RESET} ')
    maxThreads = input()
    if not maxThreads.isdigit():
        Info.write(f'{color}>{Fore.RESET} Le montant doit être un nombre.')
    thread = threading.Thread(target=Info.title, daemon=True).start()


Menu()

class Generator:

    def __init__(self):
        self.tokens = open('Data/tokens.txt', 'a')
        self.proxies = open('Data/proxies.txt').read().splitlines()
        self.color = f'{Fore.MAGENTA}{Style.BRIGHT}'
        self.xsup = 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkzLjAuNDU3Ny42MyBTYWZhcmkvNTM3LjM2IEVkZy85My4wLjk2MS40NyIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAuNDU3Ny42MyIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS9jaGFubmVscy81NTQxMjU3Nzc4MTg2MTU4NDQvODcwODgxOTEyMzQyODUxNTk1IiwicmVmZXJyaW5nX2RvbWFpbiI6ImRpc2NvcmQuY29tIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk3NTA3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='
        self.headers = {
            'Host': 'discord.com', 'Connection': 'keep-alive',
            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            'X-Super-Properties': self.xsup,
            'Accept-Language': 'en-US', 'sec-ch-ua-mobile': '?0',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47",
            'Content-Type': 'application/json', 'Authorization': 'undefined',
            'Accept': '*/*', 'Origin': 'https://discord.com',
            'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty', 'Referer': 'https://discord.com/register',
            'X-Debug-Options': 'bugReporterEnabled',
            'Accept-Encoding': 'gzip, deflate, br',
            'Cookie': 'OptanonConsent=version=6.17.0; locale=th'
        }

    def GetProxy(self): return random.choice(self.proxies)
        
    def gen(self):
        global genned, bypassed, savetokens
        bypassCaptcha = Bypass()
        Info.bypassed += 1
        while True:
            try:
                with Client(transport=SyncProxyTransport.from_url(f'{Menu.proxytype}://{self.GetProxy()}')) as request:
                    r = request.post('https://discord.com/api/v9/auth/register', headers=self.headers,
                                     json={'username': f'{Menu.username}',# | {secrets.token_urlsafe(4)}
                                           'email': secrets.token_hex(6) + '@gmail.com', 'password': 'YazatoOnTop100',
                                           'invite': Menu.invite, 'consent': True,
                                           'captcha_key': bypassCaptcha
                                           }).json()
                self.tokens.write(f'{r["token"]}\n')
                self.tokens.flush()
                Info.genned += 1
                toe = r['token']
                re = requests.get(f'https://discord.com/api/v9//users/@me', headers={'Authorization': toe})
                usernamee = re.json()['username'] + '#' + re.json()['discriminator']
                return r['token'], usernamee
            except Exception as e:
                try:
                    #print(e)
                    self.proxies.remove(self.getProxy)
                except:
                    pass
                pass

    def start(self):
        print(
            f'{self.color}>{Fore.RESET} Token Crée {self.color}:{Fore.RESET} {self.gen()}'.replace('(', '').replace("'", '').replace(')', '').replace(',', f'{self.color} >{Fore.RESET}'))

    def Client(self):
        for i in range(int(Menu.maxThreads)):
            try:
                threading.Thread(target=self.start).start()
            except Exception as e:
                #print(e)
                pass

if __name__ == '__main__':  Generator().Client()