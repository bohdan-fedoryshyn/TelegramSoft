import asyncio
import time

from telethon.sync import TelegramClient

phone_number = '380668196026'



#print('f')
#client = TelegramClient(api_hash="7245de8e747a0d6fbe11f7cc14fcc0bb",api_id=8,session='sessions/'+phone_number)
#print('d')
#client.connect()
#client.send_code_request(phone_number)
#client.disconnect()

#code = input('print code')
#lb = lambda:code


async def run():
    client = TelegramClient(phone_number,8,"7245de8e747a0d6fbe11f7cc14fcc0bb")
    await client.start()
    print(await client.get_me())

asyncio.set_event_loop(asyncio.SelectorEventLoop())
loop = asyncio.get_event_loop()
loop.run_until_complete(run())

