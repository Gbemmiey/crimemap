import pymysql
import dbconfig
from datetime import datetime
from json import dumps


class DBHelper:

    def connect(self, database="crimemap"):
        return pymysql.connect(host='localhost',
                               user=dbconfig.db_user,
                               passwd=dbconfig.db_password,
                               db=database)

    def get_all_inputs(self):
        connection = self.connect()
        try:
            query = "SELECT category, latitude, longitude, date, description FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()
        named_crimes = []
        for crime in cursor:
            named_crime = {
                'category': crime[0],
                'latitude': crime[1],
                'longitude': crime[2],
                'date': datetime.datetime.strftime(crime[3], '%Y-%m-%d'),
                'description': crime[4]
            }
            named_crimes.append(named_crime)
        return named_crimes

    # Use placeholders %s to prevent SQL injection
    def add_input(self, data):
        connection = self.connect()
        try:
            query = "INSERT INTO crimes (category, date, description, latitude, longitude) " \
                    "VALUES(%s, %s, %s, %s, %s);"
            with connection.cursor() as cursor:
                cursor.execute(query, (data["category"], data["date"], data["description"],
                                       data["latitude"], data["longitude"]))
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

