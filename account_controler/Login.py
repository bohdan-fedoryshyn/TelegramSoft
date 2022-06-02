import asyncio
import json
import time
import socks
from telethon.errors.rpcerrorlist import AuthKeyDuplicatedError
from telethon.sync import TelegramClient
from General.db import DB

class Login:

   # def __init__(self,ip:str,port:int,authorized,username:str,password:str,proxy_type:str):
    def __init__(self,db,use_proxy):
        self.use_proxy = use_proxy
        if use_proxy:
            self.pr = db.get_proxy()
            self.proxy_iter = 0


    async def get_custom_TelegramClient(self,custom_client_settings):
        client_settings = {}
        if self.use_proxy:
            if self.proxy_iter > len(self.pr):
                self.proxy_iter = 0

            if self.pr[self.proxy_iter]['type'] == 'SOCKS5':
                self.proxy = {
                              #socks.SOCKS5,
                              "proxy_type": 'socks5',
                              "addr":self.pr[self.proxy_iter]['ip'],
                              "port":self.pr[self.proxy_iter]['port'],
                              "username":self.pr[self.proxy_iter]['username'],
                              "password":self.pr[self.proxy_iter]['password']
                }

            client_settings['proxy'] = self.proxy

        #client_settings['session'] = 'sessions/' + client_settings['session']
        client_settings["session"] = custom_client_settings["session"]
        client_settings["api_id"] = custom_client_settings["api_id"]
        client_settings["api_hash"] = custom_client_settings["api_hash"]

        client = TelegramClient(**client_settings)

        await client.connect()

        if await TelegramClient.is_user_authorized(client):
            await client.start()
            print(await client.get_me())
            print("Chats: " + str(len(await client.get_dialogs())))

            return client
        else:
            print('Not authorized')
            return None


async def check(acc_list,project_id):
    accounts = []
    db = DB(project_id)
    login = Login(db)

    for el in acc_list:
        client = await login.get_custom_TelegramClient(el)
        if client != None:
            accounts.append(el)
            print(await client.get_me())

        else:
            print('None')
            print(await client.get_me())


    with open('valid_account.json', 'w+') as f:
        json.dump(accounts,f)

async def manual_login(acc_list,project_id,use_proxy):
    db = DB(project_id)
    login = Login(db,use_proxy)

    for el in acc_list:
        client = await login.get_custom_TelegramClient(el)
        if client != None:
            print(await client.get_me())

            while True:
                    for ms in await client.get_messages( await client.get_entity(777000),10):
                        print(ms.message)
                    time.sleep(0.5)

        else:
            print('None')
            print(await client.get_me())

if __name__ == '__main__':
    ## Замінити на Базу


    with open('account.json', 'r') as f:
        acc_list = json.loads(f.read())

    use_proxy = False

    asyncio.set_event_loop(asyncio.SelectorEventLoop())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(manual_login(acc_list,0,use_proxy))
