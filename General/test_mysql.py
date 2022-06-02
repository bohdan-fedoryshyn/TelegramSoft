import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='password',
        database='coredb',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            create_tasble_str = "CREATE  TABLE users2"
            cursor.execute(create_tasble_str)
            connection.commit()
            print('Good')
    finally:
        connection.close()
    print('succsess')
except Exception as ex:
    print(ex)



