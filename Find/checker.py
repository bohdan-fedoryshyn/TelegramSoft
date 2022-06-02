import telethon
from db import DB
from Login import Login
import json
import asyncio
import time
from telethon.errors.rpcerrorlist import UsernameNotOccupiedError, UsernameInvalidError,InviteHashExpiredError,FloodWaitError,InviteHashInvalidError,InviteHashEmptyError
from telethon import functions, types
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest,CheckChatInviteRequest

#from telethon.tl.functions.channels import InviteToChannelRequest,CheckChatInviteRequest

async def main(acc_list,config):
    accounts = []
    login = Login(config['project_id'])
    db = DB()
    print('f')

    for el in acc_list:
        try:
            client = await login.get_custom_TelegramClient(el)
            if client != None:
                accounts.append(client)
        except Exception as e:
            print(e)

    count_start = 2028

    while True:
        for client in accounts:

            chats = db.get_new_chats(count_start,count_start+20)
            if len(chats) == 0:
                continue

            print(chats)
            for el in chats:
                try:

                    count_start += 1
                    chat = await client(CheckChatInviteRequest(hash=el[14:]))

                    #chat = await client(functions.channels.JoinChannelRequest('t.me/+xC7Mfck2q6Y1ZWU6'))
                    #chat = await client.get_entity('t.me/+xC7Mfck2q6Y1ZWU6')
                    db.add_valid_chat(el,0)

                except (InviteHashExpiredError,InviteHashInvalidError,InviteHashEmptyError):
                    print("Invalid username")


                except UsernameInvalidError:
                    print("Invalid username")

                except (UsernameNotOccupiedError):
                    print("Не чат")

                except FloodWaitError:
                    print("Spam")
                    time.sleep(250)
                    break

                except (Exception,TypeError) as e:
                    print(e)
                time.sleep(3)


if __name__ == '__main__':


    with open('account.json', 'r') as f:
        acc_list = json.loads(f.read())

    with open('config.json','r') as f:
        config = json.loads(f.read())


    asyncio.set_event_loop(asyncio.SelectorEventLoop())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(acc_list,config))
