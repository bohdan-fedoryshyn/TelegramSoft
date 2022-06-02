import json
from datetime import time
import asyncio
from telethon.errors import FloodWaitError
from telethon.sync import TelegramClient
from telethon.tl.types import InputMessagesFilterUrl
from Login import Login
from db import DB
import random

async def main(acc_list,config,db):


    project_id = 1

    accounts = []
    login = Login(config['project_id'])
    for el in acc_list:
       # el['session'] = 'sessions/' + el['session']
        client = await login.get_custom_TelegramClient(el)
        if client != None:
            accounts.append(client)

    for client in accounts:
        entities = await client.get_dialogs()
       # random.shuffle(entities)
        step = 0
        for el in entities:
            find_chats = []
            try:
                step += 1

                find_chats = []
                historyUrl = await client.get_messages(el, filter=InputMessagesFilterUrl , limit=10000)
                for em in historyUrl:
                    k = em.message.find('t.me/')
                    if k != -1:
                        end = 0
                        for find in em.message[k:]:
                            if find == ' ' or find == '\n':
                                break
                            end += 1
                        if 'bot?' not in em.message[k:k + end]:
                            find_chats.append(em.message[k:k + end])

            except FloodWaitError:
                time.sleep(284)
            except e:
                print(e)

            print("Find: " + str(len(find_chats)))
            if len(find_chats) > 0:
                start_count = 0

                while True:
                    if start_count + 1000 < len(find_chats):
                        try:
                            db.add_new_chats(find_chats[start_count: start_count+1000],project_id)
                        except:
                            pass
                        start_count += 1000
                    else:
                        try:
                            db.add_new_chats(find_chats, project_id)
                        except:
                            pass
                        break

            del find_chats


if __name__ == '__main__':

    db = DB()

    with open('config.json', 'r') as f:
        config = json.loads(f.read())

    acc_list = db.get_accounts()


    asyncio.set_event_loop(asyncio.SelectorEventLoop())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(acc_list,config,db))
