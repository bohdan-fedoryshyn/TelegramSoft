import json
import sqlite3
import pymysql


class DB:


    def __init__(self):
        #self.connection = sqlite3.connect('data.db')
        #self.cursor = self.connection.cursor()
        try:
            self.connection = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                password='password',
                database='coredb',
                cursorclass=pymysql.cursors.DictCursor
            )


            print('succsess')
        except Exception as ex:
            print(ex)

    def __query(self,q:str):

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(q)
                self.connection.commit()

                response = self.cursor.execute(q)
                self.connection.commit()
                return response

        except Exception as ex:
            print(ex)

    def create(self):


        ### sqlite3
        ### Зробити зв*язані поля api_id і api_hash о таблиці api_credentionals
        #self.cursor.execute(""" CREATE TABLE accounts (
        #                    country INTEGER, phone_number INTEGER,
        #                    api_id INTEGER, api_hash TEXT, device_model TEXT, system_version TEXT,
        #                    app_version TEXT, lang_code TEXT, system_lang_code TEXT, state INTEGER, project INTEGER );""")

        self.__query(""" CREATE TABLE accounts (
                        country int, phone_number int,
                        api_id int, api_hash varchar(24), device_model varchar(24), system_version varchar(24),
                        app_version varchar(24), lang_code varchar(4), system_lang_code varchar(4), state int, project int );""")


        #self.cursor.execute(""" CREATE TABLE channels (
        #                id INTEGER, link TEXT, members INTEGER, type TEXT, country TEXT, relevant_project TEXT);""")

        #self.cursor.execute(""" CREATE TABLE brut_channels (
        #                link TEXT, id INTEGER);""")

        ## Продумати архітектуру таблиці
        #self.cursor.execute(""" CREATE TABLE messages (id INTEGER PRIMARY KEY, project TEXT, message TEXT, file TEXT); """)

        # API credentionals
        #self.cursor.execute(""" CREATE TABLE api_credentional (api_id INTEGER, api_hash TEXT, name TEXT);""")

        ## gender - 0 жінка, 1 чоловік
        #self.cursor.execute(""" CREATE TABLE user_first_name (first_name TEXT, gender int)""")

        #self.cursor.execute(""" CREATE TABLE user_last_name (last_name TEXT);""")

        #self.cursor.execute(""" CREATE TABLE user_description (description TEXT);""")





    #print(__query("""
    #INSERT INTO accounts VALUES(1,79365086901,8,"de8e747a0d6fbe11f7cc14fcc0bb","iPhone 5S","12.5.5","Telegram iOS 5.11.0","ru","ru",0,0)
    #"""))

    ### Accounts
    def account_add(self,phone_number,api_id:int,api_hash:str,device_model:str,system_version:str,app_version:str,lang_code:str,system_lang_code:str,country=0):
        self.__query(f"""INSERT INTO accounts VALUES ({country},{int(phone_number)},{api_id},"{api_hash}","{device_model}",
                                "{system_version}","{app_version}","{lang_code}","{system_lang_code}",0,0);""")
    def account_remove(self,phone_number:str):
        self.__query(f"DELETE FROM accounts WHERE phone_number={phone_number};")
    def account_update_state(self,phone_number:int,state:str):
        self.__query(f"UPDATE accounts SET state = {state} WHERE phone_number = {phone_number};")

    def account_update_project(self,phone_number:int,project:str):
        self.__query(f"UPDATE accounts SET project = {project} WHERE phone_number = {phone_number};")

    def get_account(self,phone_number:int):
        return self.__query(f"SELECT * FROM users WHERE phone_number = {phone_number};")

    ### краще не використовувати, велика кількість даних
    def get_accounts(self):
        return self.__query("SELECT * FROM users;")

    def get_accounts_filter(self,filter:dict):
        filter_str = ""
        for el in filter:
            filter_str += f" {el}={str(filter[el])},"

        print(filter_str)
        return self.__query(f"SELECT * FROM accounts WHERE"+filter_str)+';'

    ### Channels
    def channels_add(self,id:int, link:str, members:int, type:str, country:str, relevant_project:str):
        self.__query(f"INSERT INTO channels VALUES ({id},{link},{members},{type},{country},{relevant_project});")

    def channels_remove(self,id:int):
        self.__query(f"DELETE FROM channels WHERE id = {id}")
    def channels_get_by_id(self,id:int):
        return self.__query(f"SELECT * FROM channels WHERE id = {id}")

    def channels_get_by_link(self,link:str):
        return self.__query(f"SELECT * FROM channels WHERE link = {link}")

    ### Brut channels

    def brut_channels_add(self,link:str,id:int):
        self.__query(f"INSERT INTO brut_channels VALUE ({link},{id})")

    def brut_channels_get_by_link(self,link:str):
        return self.__query(f"SELECT * FROM brut_channels WHERE link = {link}")

    def brut_channels_get_by_id(self,id:str):
        return self.__query(f"SELECT * FROM brut_channels WHERE id = {id}")

    # Messages
    def message_add(self,project:str,message:str,file:str):
        self.__query(f"INSERT INTO messages VALUES ({project},{message},{file})")

    def message_remove(self,id:int):
        self.__query(f"DELETE FROM messages WHERE id = {id}")

    def messages_get(self,project:str):
        return self.__query(f"SELECT * FROM messages WHERE project={project}")

    def messages_get_by_id(self,id:int):
        return self.__query(f"SELECT * FROM messages WHERE id={id}")


    #### API credentionals
    ### Зробити зв*язане поле
    ### Вроді програмісту не потрібний доступ до цієї таблиці


db = DB()

with open('../Register/account.json') as acc:
    accounts = json.loads(acc.read())

for el in accounts:
    #def account_add(self,phone_number,api_id:int,api_hash:str,device_model:str,system_version:str,app_version:str,lang_code:str,system_lang_code:str,country=0):
    print(el)
    #db.account_add(**el)