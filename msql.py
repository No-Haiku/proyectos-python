import pymysql 

class DataBase:
    def __init__(self):
        self.connection=pymysql.connect(
            host='localhost',#si es remota colocar la ip
            user='root',
            password='',
            db='demo'
        )

        self.cursor= self.connection.cursor()

dataBase=DataBase()