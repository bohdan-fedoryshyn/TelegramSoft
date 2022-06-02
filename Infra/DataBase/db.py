import json
import pymysql
from pymysql.cursors import DictCursor
from contextlib import closing

class DB:

    def __init__(self):

        with open('db_config.json', 'r') as f:
            config = json.loads(f.read())

        self.connection =pymysql.connect(host=config['host'],
                                         port=config['port'],
                                         user=config['user'],
                                         password=config['passwd'],
                                         database=config['db'],
                                         #charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)

        self.cursor = self.connection.cursor()


    def create_tables(self):
        commansd = [
            "CREATE TABLE new_chats(link VARCHAR(32),project_id INT)",
            "CREATE TABLE chats(id INT, link VARCHAR(32))",
            "CREATE TABLE proxy(ip VARCHAR(32),port INT,username VARCHAR(32),password VARCHAR(32),type VARCHAR(32), project_id INT)"
        ]

        for el in commansd:
            self.cursor.execute(el)

        self.connection.commit()

    ### chats
    def add_new_chats(self,links,project_id):
        values_to_insert = []
        for el in links:
            values_to_insert.append((el,project_id))
        query_string = "INSERT INTO new_chats (link, project_id) VALUES " + ",".join("(%s, %s)" for _ in values_to_insert)
        values = [item for sublist in values_to_insert for item in sublist]
        print(query_string)
        self.cursor.execute(query_string, values)
        self.connection.commit()



if __name__ == '__main__':
    db =DB()
    #db.add_new_chats(['test1','test2','test3'],1)
    db.connection.close()
