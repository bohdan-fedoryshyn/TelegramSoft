import asyncio
import json
import time

import telethon


from Login import Login
from db import DB


async def main():
    clients = []
    db = DB(0)
    login = Login(db)

    offset = 0
    limit = 100
    all_participants = []


    with open('account.json','r') as f:
        account = json.loads(f.read())



    for el in account:
        client = (await login.get_custom_TelegramClient(el))
        if client != None:
            clients.append(client)
            break

    while True:
        for cl in clients:
            dialogs = await cl.get_dialogs()
            print('CHats: ' + str(len(dialogs)))
            for chat in dialogs:
                    fio_list = []
                   # participants = await cl(GetParticipantsRequest(
                   #     chat, ChannelParticipantsSearch(''), offset, limit,
                   #     hash=0
                   # ))
                    try:
                        participants = await cl.get_participants(chat)
                    except:
                        continue
                    for el in participants:

                        try:
                            fio_list.append({
                                "first_name":el.first_name,
                                "last_name":el.last_name,
                                "username":el.username
                            })
                        except Exception:
                            print("error")

                    try:
                        db.add_FIO(fio_list)

                    except:
                        print("Error Insert into")





if __name__ == '__main__':


        asyncio.set_event_loop(asyncio.SelectorEventLoop())
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())