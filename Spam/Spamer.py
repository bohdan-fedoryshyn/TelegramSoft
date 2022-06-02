import asyncio
import time
import json
from telethon.errors.rpcerrorlist import *
import random
from Login import Login


async def spam(acc_list,proxy,messages):

    login = Login(**proxy)
    accounts = []

    for el in acc_list:

        el['session'] = '/sessions/' + el['session']
        cl = await login.get_custom_TelegramClient(el)
        if cl != None:
            accounts.append(cl)


    while True:
        max_dialogs = 0

        for client in accounts:
            account_list = []
            try:
                await client.start()
                d = await client.get_dialogs()
                random.shuffle(d)

                if len(d) > max_dialogs:
                    max_dialogs = len(d)

                account_list.append({'dialogs': d, 'client': client})

                ### remove dialog with TelegramNews
                client.delete_dialog(await client.get_entity(42777))

            except:
                pass

            for el in range(max_dialogs):
                for cl in account_list:
                    try:

                        #await cl['client'].send_file(cl['dialogs'][el], 'dataBase/' + str(random.randint(1, 12)) + '.gif',
                        #                       caption=messages[random.randint(len(messages))])
                        await cl['client'].send_message(cl['dialogs'][el], messages[random.randint(0,len(messages)-1)])

                    except FloodWaitError:
                        print("sleep")
                        time.sleep(250)

                    except Exception as e:
                        print(e)

                time.sleep(250)

if __name__ == '__main__':
    print("SPAMER______________________")

    ## Замінити на Базу
    with open('proxy.json','r') as f:
        proxy = json.loads(f.read())

    with open('dataBase/account.json', 'r') as f:
        acc_list = json.loads(f.read())

    with open('dataBase/message.json', 'r') as f:
        messages = json.loads(f.read())


    asyncio.set_event_loop(asyncio.SelectorEventLoop())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(spam(acc_list=acc_list,proxy=proxy,messages=messages))




