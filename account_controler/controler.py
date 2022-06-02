import asyncio

from telethon.errors import TypeNotFoundError
from telethon.sync import TelegramClient
from db import DB



class Controler():


    def __init__(self):

        self.accounts = {}
        self.db = DB(0)

    async def add_account(self,phone_number):
            client = TelegramClient(api_hash="7245de8e747a0d6fbe11f7cc14fcc0bb",api_id=8,session='sessions/'+phone_number)
            client.connect()
            client.send_code_request(phone_number)
            client.disconnect()


    def set_code(self,phone_number,code,owner_id):

        lb = lambda:code
        client = TelegramClient(api_hash="7245de8e747a0d6fbe11f7cc14fcc0bb",api_id=8,session='sessions/'+phone_number)

        client.start(
            phone=phone_number,
            code_callback=lb,
        )

        self.db.account_add(
            owner_id=owner_id,
            session=phone_number,
            status="NEW",
            project_id=0,
            proxy_id=0,
            api_id=8,
            api_hash="7245de8e747a0d6fbe11f7cc14fcc0bb",
            first_name =  client.get_me().first_name,
            last_name =  client.get_me().last_name,
            chats = len( client.get_dialogs())
        )



    def update(self,owner_id):
        accounts = self.db.get_user_accounts(owner_id)

        for el in accounts:
            client = TelegramClient(api_hash="7245de8e747a0d6fbe11f7cc14fcc0bb",api_id=8,session='sessions/'+el['session'])
            client.start()


        self.db.update_account(
            owner_id=owner_id,
            session=el['session'],
            first_name =  client.get_me().first_name,
            last_name =  client.get_me().last_name,
            chats = len( client.get_dialogs())
        )




if __name__ == "__main__":
    controller = Controler()
    controller.add_account('380502758539')
    code = input('code:')
    controller.set_code('380502758539',code)