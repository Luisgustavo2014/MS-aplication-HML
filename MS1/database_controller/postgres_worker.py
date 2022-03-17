import psycopg2

from config.database_connection import ConnectionDatabase
from datetime import datetime


class PostgresWorker():

    def __init__(self) :
      self.PSQL = ConnectionDatabase()

    def insert_user(self, data):
      date_time = datetime.now()
      date_time_formate = date_time.strftime('%Y/%m/%d %H:%M')

      query_insert = f'INSERT INTO users (_name, password ,cpf , email, phone_number, created_at, updated_at)VALUES (%s,%s,%s,%s,%s,%s,%s)'
      vars_query = (data['name'],data['password'],data['cpf'],data['email'],data['phone_number'],date_time_formate,date_time_formate)
      self.PSQL.cursor.execute(query_insert, vars_query)
      self.PSQL.connection.commit()

      print('[X] INSERTION DONE IN POSTGRES!')
      self.PSQL.cursor.close()

    