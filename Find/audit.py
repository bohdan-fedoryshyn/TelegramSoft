import random
import string
import time

import socks
import telethon
import json

from telethon.errors import FloodWaitError, InviteHashExpiredError, AuthKeyDuplicatedError,UsernameNotOccupiedError
from telethon.errors import rpcerrorlist
from telethon import TelegramClient
from telethon.tl import functions
from telethon.tl.functions.channels import JoinChannelRequest, GetFullChannelRequest
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.types import PeerChat


with open('proxy.json') as f_proxy:
    proxys = json.loads(f_proxy.read())

with open('dataBase/username.json') as f_proxy:
    username = json.loads(f_proxy.read())

with open('dataBase/All_channel_with_chats.json', 'r', encoding='utf8') as f:
    chats = json.loads(f.read())

for el in range(110, 181):
    try:
        if proxy_iter >= len(proxys):
            proxy_iter = 0

        ip = proxys[proxy_iter][0]
        port = int(proxys[proxy_iter][1])
        login = proxys[proxy_iter][2]
        password = proxys[proxy_iter][3]
        proxy_iter += 1
        proxy = (socks.SOCKS5, ip, port, True, login, password)
        # print(el)
        client = TelegramClient(name + (str(el)), id, hash, proxy=proxy)

        try:
            client.connect()
            if not client.is_user_authorized():
                print("Не авторизований")
            else:
                client.start()
                # print('+')
                # us = client.get_me().to_dict()['username']
                # if us == None:
                #     z = username[random.randint(0,len(username))] + random.choice(string.ascii_letters)
                #     #print(z)
                #     client(UpdateUsernameRequest(username=z))
                #     us = client.get_me().to_dict()['username']
                #     print('@' +us)
                # else:
                #    print('@' + us)

                acc.append(client)
            # time.sleep(1)
        except ConnectionError:
            print('ConnectionError')
        except AuthKeyDuplicatedError:
            print("Працює на іншому")
    except ConnectionError:
        pass
print('Аккаунтвів: ' + str(len(acc)))
map = []
map_50 = []
map_do_50 = []
acc_iter = 1
channel = []
iter_chat = 4700
save = 0
other_iter = 0


def get_chat(z):
    global other_iter
    if 'megagroup' in z:
        if z['megagroup']:
            try:
                # if z['id'] in map:
                #    ls = map[z['id']]
                #    ls.append(chats[iter_chat])
                #    map[z['id']] = ls
                # else:
                #    map[z['id']] = [chats[iter_chat]]
                map.append(chats[iter_chat])
            except KeyError:
                other_iter += 1
                map.append(chats[iter_chat])
                # map['other_' + str(other_iter)] = [chats[iter_chat]]

        else:
            # channel[chats[iter_chat]] = z['id']
            channel.append(chats[iter_chat])
    else:
        print('Нема magagroup')


while True:
    iter_chat += 1

    if iter_chat >= len(chats):
        break
    if acc_iter >= len(acc):
        acc_iter = 0
    try:
        if 't.me/joinchat/' in chats[iter_chat]:
            chat = acc[acc_iter](functions.messages.CheckChatInviteRequest(chats[iter_chat][14:]))
            print("True чат")
        else:
            # print(chats[iter_chat][5:])
            try:
                # my_chat = acc[acc_iter].get_entity((chats[iter_chat]))
                result = acc[acc_iter](GetFullChannelRequest(channel=chats[iter_chat])).to_dict()

            # print(my_chat)

            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                print("Invalid username")
                continue

            except TypeError:
                print("Не чат")
                continue

            except FloodWaitError:
                acc_iter += 1
                print("Spam")
                # iter_chat -= 1

            except UsernameNotOccupiedError:
                pass
            except Exception as e:
                pass

        #        result = chat.to_dict()
        try:
            for element in result['chats']:
                if element['megagroup']:

                    id = element['id']
                    my_chat = acc[acc_iter].get_entity(id)
                    users = acc[acc_iter].get_participants(my_chat)
                    print(len(users))

                    if len(users) > 100:
                        map.append(chats[iter_chat])
                    elif len(users) > 50:
                        map_50.append(chats[iter_chat])
                    else:
                        map_do_50.append(chats[iter_chat])

        except FloodWaitError:
            acc_iter += 1
            print("Spam")
            # iter_chat -= 1

        except Exception as e:
            pass

            # try:
            # updates = acc[acc_iter](JoinChannelRequest(my_chat))
            # print('True')

        # print(str(chats[iter_chat]) + ' !- ' + str(z))
        # print('\n\n\n')
        # print(z)
        # print(z.keys())
        # if 'chats' in z:
        #    if type(z['chats']) == list:
        #        get_chat(z['chats'][0])
        #    else:
        #        get_chat(z['chats'])
        # elif 'chat' in z:
        #    get_chat(z['chat'])
        # elif 'megagroup' in z:
        #    print("Ключ megagroup")
        #    get_chat(z)
        # else:
        #    print("Not_key")

    except FloodWaitError:
        acc_iter += 1
        print("Spam")
        # iter_chat -= 1

        time.sleep(20)
    except InviteHashExpiredError:
        print("Не робочий")
    except KeyError:
        print('Key_Eror')

    time.sleep(0.2)
    save += 1
    if save >= 100:
        with open('dataBase/chats_100.json', 'a+') as f:
            json.dump(map, f)

        with open('dataBase/chats_50.json', 'a+') as f:
            json.dump(map_50, f)

        with open('dataBase/chats_do_50.json', 'a+') as f:
            json.dump(map_do_50, f)

        save = 0
        map = []
        map_50 = []
        map_do_50 = []
        acc_iter += 1

    print(str(iter_chat) + '/' + str(len(chats)))

with open('dataBase/chats_for_look_check.json', 'a+') as f:
    json.dump(map, f)

with open('dataBase/channel.json', 'w+') as f:
    json.dump(channel, f)





if __name__ == '__main__':


    with open('proxy.json', 'r') as f:
        proxy = json.loads(f.read())

    with open('dataBase/account.json', 'r') as f:
        acc_list = json.loads(f.read())


    asyncio.set_event_loop(asyncio.SelectorEventLoop())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(acc_list,proxy))



