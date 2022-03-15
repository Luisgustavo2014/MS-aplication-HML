import psycopg2

from .database_connection import ConnectionDatabase
from datetime import datetime


class PostrgesManipulation():

    def __init__(self) :
      self.PSQL = ConnectionDatabase()

    def select_version(self):
        print("PostgreSQL server information")
        print(self.PSQL.connection.get_dsn_parameters())
        self.PSQL.cursor.execute("SELECT version();")

        record = self.PSQL.cursor.fetchone()
        print("[X] You are connected to - ", record, "\n")
        self.PSQL.cursor.close()

    def insert_user(self, data):
      date_time = datetime.now()
      date_time_formate = date_time.strftime('%Y/%m/%d %H:%M')

      query_insert = f'INSERT INTO users (_name, cpf, email, phone_number,created_at,updated_at)VALUES (%s,%s,%s,%s,%s,%s)'
      vars_query = (data['name'],data['cpf'],data['email'],data['phone_number'],date_time_formate,date_time_formate)
      self.PSQL.cursor.execute(query_insert, vars_query)
      self.PSQL.connection.commit()

      print('[X] INSERTION DONE IN POSTGRES!')
      self.PSQL.cursor.close()
