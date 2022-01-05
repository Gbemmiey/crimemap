import pymysql
import dbconfig


class DBHelper:

    def connect(self, database="crimemap"):
        return pymysql.connect(host='localhost',
                               user=dbconfig.db_user,
                               passwd=dbconfig.db_password,
                               db=database)

    def get_all_inputs(self):
        connection = self.connect()
        try:
            query = "SELECT description FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()

    def add_input(self, data):
        connection = self.connect()
        try:
            query = "INSERT INTO crimes (category, date, description, latitude, longitude) " \
                    "VALUES(%s, %s, %s, %s, %s);"
            with connection.cursor() as cursor:
                cursor.execute(query, (data["category"], data["date"], data["description"], data["latitude"], data["longitude"]))
                connection.commit()
        finally:
            connection.close()

    def clear_all(self):
        connection = self.connect()
        try:
            query = "DELETE FROM crimes"
            with connection.cursor() as cursor:
                cursor.execute(query)
            connection.commit()
        finally:
            connection.close()
