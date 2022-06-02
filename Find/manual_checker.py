import json
from db import DB

class Manual_Cheacker():

    def __init__(self):
        self.db = DB()

    def get_chat(self):
        chat =  self.db.get_chat_No_subId(limit=1)
        if len(chat) == 0:
            print("End")
            return None

        return {chat['id']:chat["link"]}


    def set_result(self,id,result):
        self.db.set_result_chat(id,result)

if __name__ == '__main__':
    mn = Manual_Cheacker()

    while True:
        chat = mn.get_chat()
        print(chat['link'])
        mn.set_result(chat['id'],input("Результат:"))


