import asyncio

import telethon
from telethon import functions, TelegramClient
from telethon.errors.rpcerrorlist import UserAlreadyParticipantError
from telethon.errors.rpcerrorlist import FloodWaitError
import time
from telethon.tl.functions.channels import JoinChannelRequest
from General.Login import Login
from db import DB


class Follow:

        def __init__(self,data):
                self.data = data

        async def follow(self,chats,acc):
                iter = 0

                for el in chats[60:]:
                        for cl in acc:
                                try:
                                        if 'joinchat/' in el:
                                                updates = await cl(functions.messages.ImportChatInviteRequest(hash=el[14:]))
                                                print("good")
                                        else:

                                                await cl(JoinChannelRequest(await cl.get_entity(el[5:])))
                                                print("good @")

                                except UserAlreadyParticipantError:
                                        print("Вже підписаний")

                                except FloodWaitError:
                                        print("sleep")
                                        time.sleep(250)

                                except:
                                        print('eror')

                        iter += 1
                        print("Прошол : " + str(iter))
                        time.sleep(5)


        async def start(self):

                if self.data['use_proxy'] == 'true':
                        self.use_proxy = True
                else:
                        self.use_proxy = False

                clients = []
                db = DB(self.data['project_id'])
                login = Login(db,self.use_proxy)
                chats = []
                for el in db.get_chats():
                        chats.append(el['link'])

                for el in db.get_Free_accounts():
                        clients.append(await login.get_custom_TelegramClient(el))

                await self.follow(chats,clients)

def run(config):
        print(config)
        follow = Follow(config)
        asyncio.set_event_loop(asyncio.SelectorEventLoop())
        loop = asyncio.get_event_loop()
        loop.run_until_complete(follow.start())

        print("End Follow")

if __name__ == '__main__':
        client = telethon.TelegramClient
        chats = ["@V_Zelenskiy_official","@UkraineNow","@UkrainaOnlline"]
        input('Start')
        with TelegramClient('name', 1442515, '5e3ddc1fd6a74b014d7b89c7f74a305c') as client:
                for el in chats:
                                try:
                                                client(JoinChannelRequest( client.get_entity(el)))
                                                print("good @")

                                except UserAlreadyParticipantError:
                                        print("Вже підписаний")

                                except FloodWaitError:
                                        print("sleep")
                                        time.sleep(250)

                                except:
                                        print('eror')

                                iter += 1
                                print("Прошол : " + str(iter))
                                time.sleep(5)



