import json
import random
import time

import pymysql
from pymysql.cursors import DictCursor
from contextlib import closing

class DB:

    def __init__(self,project_id):

        with open('../General/db_config.json', 'r') as f:
            config = json.loads(f.read())

        self.project_id = project_id
        self.connection =pymysql.connect(host=config['host'],
                                         port=config['port'],
                                         user=config['user'],
                                         password=config['passwd'],
                                         database=config['db'],
                                         #charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)

        self.cursor = self.connection.cursor()
        self.create_tables()



    def create_tables(self):
        commansd = [
            "CREATE TABLE IF NOT EXISTS new_chats(id int AUTO_INCREMENT PRIMARY KEY, link VARCHAR(50),project_id INT);",
            "CREATE TABLE IF NOT EXISTS chats(id int AUTO_INCREMENT PRIMARY KEY,project_id INT, chats_id INT, link VARCHAR(50));",
            "CREATE TABLE IF NOT EXISTS proxy(ip VARCHAR(32),port int,username VARCHAR(32),password VARCHAR(32),type VARCHAR(32), project_id int);",
            #"ALTER TABLE new_chats_tmp ADD id INT NOT NULL AUTO_INCREMENT"
            #"INSERT INTO new_chats SELECT * FROM new_chats_tmp"
            "CREATE TABLE IF NOT EXISTS account(session VARCHAR(32), status VARCHAR(10), owner_id INT,proxy_id INT, last_update DATETIME, api_id INT, api_hash VARCHAR(32),first_name VARCHAR(32), last_name VARCHAR(32),chats INT);",
            "CREATE TABLE IF NOT EXISTS new_chats_joinchat(id int AUTO_INCREMENT PRIMARY KEY, link VARCHAR(50),project_id INT);",
            "CREATE TABLE IF NOT EXISTS FIO(id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(32), last_name VARCHAR(32), username VARCHAR(32), project_id INT);"
        ]

        for el in commansd:
            print(el)
            self.cursor.execute(el)
            self.connection.commit()




### Proxy

    def add_proxy(self,ip,port,username,password,type):
        self.cursor.execute(f'''INSERT INTO proxy (ip,port,username,password,type,project_id)
                            VALUES("{ip}",{port},"{username}","{password}","{type}",{self.project_id})''')
        self.connection.commit()


    def get_proxy(self):
        self.cursor.execute(f'SELECT * FROM proxy WHERE project_id = {self.project_id}')
        return self.cursor.fetchall()

    ### chats
    def add_new_chats(self,links):
        values_to_insert = []
        print(links)
        for el in links:
            values_to_insert.append((el,self.project_id))
        query_string = "INSERT INTO new_chats (link, project_id) VALUES " + ",".join("(%s, %s)" for _ in values_to_insert)
        values = [item for sublist in values_to_insert for item in sublist]
        print(query_string)
        self.cursor.execute(query_string, values)
        self.connection.commit()


    def get_new_chats(self,count_start,count_end):
        self.cursor.execute(f"SELECT link FROM new_chats_joinchat WHERE id > {count_start} AND id < {count_end}")
        result = []
        for el in self.cursor.fetchall():
            result.append(el['link'])

        return result

    def add_valid_chat(self,link,chat_id):
        self.cursor.execute(f'INSERT INTO chats (link,chats_id) VALUES("{link}",{chat_id})')
        self.connection.commit()


    def get_chat_No_subId(self,limit):
        self.cursor.execute(f"SELECT * FROM chats LIMIT {limit}")
        return self.cursor.fetchall()

    def set_result_chat(self,id,result):
        self.cursor.execute(f"UPDATE chats SET sub_id = {int(result)} WHERE id = {id}")
        self.connection.commit()

    ### account

    def account_add(self,session,status,project_id,proxy_id,api_id,api_hash,first_name,last_name,chats):
        self.cursor.execute(f'''INSERT INTO account (session,status,project_id,proxy_id,last_update,api_id,api_hash,first_name,last_name,chats) VALUES (
        "{session}","{status}",{project_id},{proxy_id},NOW(),{api_id},"{api_hash}","{first_name}","{last_name}",{chats}
        )''')

        self.connection.commit()

    def get_account(self,session):
        self.cursor.execute(f'SELECT * FROM account WHERE session = "{session}"')
        return self.cursor.fetchall()[0]

#    def get_Free_accounts(self):
#        self.cursor.execute('SELECT * FROM account WHERE status = "FREE"')
#        return self.cursor.fetchall()

#    def get_Specific_accounts(self):
#        pass


    def get_chats(self):
        self.cursor.execute(f'SELECT * FROM chats WHERE project_id = {self.project_id}')
        return self.cursor.fetchall()


    ### FIO  - First_name, Last_name, Username
    def add_FIO (self,fio_list):
        values_to_insert = []
        for el in fio_list:

            values_to_insert.append((el['first_name'], el['last_name'], el['username'], self.project_id))

        query_string = "INSERT INTO FIO  (first_name, last_name,username,project_id) VALUES " + ",".join(
            "(%s, %s, %s, %s)" for _ in values_to_insert)
        values = [item for sublist in values_to_insert for item in sublist]

        self.cursor.execute(query_string,values)
        self.connection.commit()

    def get_random_FIO(self):
        self.cursor.execute(f'SELECT * FROM FIO ORDER BY RAND() LIMIT 1;')
        return self.cursor.fetchall()[0]





if __name__ == '__main__':
    db =DB(0)

    for el in ["@breakingmash","@nexta_live","@ptuxerman","@aviasales","@vandroukiru"]:
        db.add_valid_chat(el,0)
    #db.account_add(session='79912465055',status='FREE',project_id=0,proxy_id=0,api_id=8,api_hash='7245de8e747a0d6fbe11f7cc14fcc0bb')
    #pr = db.get_proxy()
    #print(pr)
    #db.cursor.execute(f'DELETE FROM proxy WHERE port = 8000')
    #db.connection.commit()
    #db.add_proxy("79.141.161.113",45786,"Selrobertros007","Q2p2UqX","SOCKS5")
    db.connection.close()