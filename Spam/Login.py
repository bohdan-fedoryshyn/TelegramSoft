import asyncio
import json
import time
import socks
from telethon.errors.rpcerrorlist import AuthKeyDuplicatedError
from telethon.sync import TelegramClient
import os

class Login:

    def __init__(self,ip:str,port:int,authorized,username:str,password:str,proxy_type:str):

        if proxy_type == 'SOCKS5':
            self.proxy = (socks.SOCKS5, ip, port, authorized, username, password)


    async def get_custom_TelegramClient(self,client_settings):

        client_settings['proxy'] = self.proxy
        client = TelegramClient(session=client_settings['session'],
                                api_id=client_settings['api_id'],
                                api_hash=client_settings['api_hash']
                                )
        if TelegramClient.is_user_authorized(client):
            await client.start()
            print(await client.get_me())
            print("Chats: " + str(len(await client.get_dialogs())))

            return client
        else:
            return None


async def check(acc_list,proxy):
    accounts = []
    login = Login(**proxy)

    for el in acc_list:
        client = await login.get_custom_TelegramClient(el)
        if client != None:
            accounts.append(el)

    with open('valid_account.json','w+') as f:
        json.dump(accounts,f)

if __name__ == '__main__':
    ## Замінити на Базу
    with open('proxy.json', 'r') as f:
        proxy = json.loads(f.read())

    with open('account.json', 'r') as f:
        acc_list = json.loads(f.read())


    asyncio.set_event_loop(asyncio.SelectorEventLoop())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(check(acc_list,proxy))
