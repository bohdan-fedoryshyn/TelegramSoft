import asyncio
import json
import os
import random
import sqlite3
import string
import time
import socks
from telethon import TelegramClient
from telethon.errors import PhoneNumberBannedError, FloodWaitError
from telethon.tl.functions.account import UpdateUsernameRequest

from Sms_activate import SmsActivate
from builtins import ConnectionError
from db import DB



def id_generator(size=2, chars=string.ascii_uppercase + string.digits):
    ...
    return ''.join(random.choice(chars) for _ in range(size))

async def filling_user(client,username):
    await client (UpdateUsernameRequest(username=username))

async def start(quantity,db,use_proxy):

    sms = SmsActivate()
    if use_proxy:
        prox = db.get_proxy()[0]
        if prox['type'] == 'SOCKS5':
            proxy = {
                # socks.SOCKS5,
                "proxy_type": 'socks5',
                "addr": prox['ip'],
                "port": prox['port'],
                "username": prox['username'],
                "password": prox['password']
            }

        print(proxy)



    for el in range(quantity):
        try:

            time.sleep(5)
            number_info = sms.get_numberTELEGRAM()
            phone_number = number_info[1]

            name = db.get_random_FIO()

            first_name = name['first_name']
            last_name = name['last_name']

            try:
                username = name['username'] + id_generator()
            except:
                pass


            #device = devices[random.randint(0,len(devices))]

            setting = dict({
                "session": phone_number,
                "api_id": 8,
                "api_hash": "7245de8e747a0d6fbe11f7cc14fcc0bb"
            })

            if use_proxy:
                setting_use["proxy"] = proxy

            setting_use = setting.copy()
            setting_use["session"] = "sessions/" + setting["session"]

            client = TelegramClient(**setting_use)

            await client.connect()
            await client.send_code_request(phone_number)

            await client.start(

                phone=phone_number,
                code_callback=sms.get_kod,
                first_name=first_name,
                last_name=last_name
            )

            db.account_add(
                session=setting['session'],
                status="NEW",
                project_id=0,
                proxy_id=0,
                api_id=setting['api_id'],
                api_hash=setting['api_hash']
            )

            await filling_user(client=client,username=username)
            await client.disconnect()


            time.sleep(10)

        except PhoneNumberBannedError:
            print('PhoneNumberBannedError')
        except sqlite3.OperationalError:
            print('sqlite3.OperationalError')
        except ConnectionError:
            print('ConnectionError')
        except FloodWaitError:
            print('FloodWaitError')
            time.sleep(60)

        except Exception as e:
            print(e)



def run(data):
    min_quantity_free = data['q']
    db = DB(0)
    quantity_free = len(db.get_Free_accounts())

    if data['use_proxy'] == 'true':
        use_proxy= True
    else:
        use_proxy= False

    if (quantity_free < min_quantity_free):
            asyncio.set_event_loop(asyncio.SelectorEventLoop())
            loop = asyncio.get_event_loop()
            loop.run_until_complete(start(quantity=int(min_quantity_free - quantity_free + 2),db=db,use_proxy=use_proxy))

#if __name__ == '__main__':

   # with open('device.json','r') as f:
   #     devices = json.loads(f.read())


    #min_quantity_free = 5

    #while True:
    #    db = DB(0)
    #    quantity_free = len(db.get_Free_accounts())
    #    if (quantity_free < min_quantity_free):
    #        asyncio.set_event_loop(asyncio.SelectorEventLoop())
    #        loop = asyncio.get_event_loop()
    #        loop.run_until_complete(start(quantity=int(min_quantity_free - quantity_free + 2),db=db))

    #   del db
    #    time.sleep(1800)


    ### Cro