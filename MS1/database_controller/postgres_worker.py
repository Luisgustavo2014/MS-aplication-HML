from socket import errorTab
import psycopg2

from config.database_connection import ConnectionDatabase
from datetime import datetime


class PostgresWorker():

    def __init__(self) :
      self.PSQL = ConnectionDatabase()
      self.date_time = datetime.now()
      self.date_time_formate = self.date_time.strftime('%Y/%m/%d %H:%M')

    def insert_user(self, data):

      try:
        query_insert = 'INSERT INTO users (_name, nick_name ,password ,cpf , email, phone_number, created_at, updated_at)VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
        vars_query = (data['name'],data['nick_name'],data['password'],data['cpf'],data['email'],data['phone_number'],self.date_time_formate,self.date_time_formate)
        self.PSQL.cursor.execute(query_insert, vars_query)
        self.PSQL.connection.commit()
        self.PSQL.cursor.close()

        print('[✓] INSERTION DONE IN POSTGRES!')
        return '[✓] User created successfully!'
      except Exception as error:
        print(error)
        return f'[X] ERROR INSERTING IN POSTGRES! \
        {error}'

    def alter_user(self, data):
      try:
        query_update = 'UPDATE users SET _name=%s ,password=%s ,cpf=%s , email=%s, phone_number=%s, updated_at=%s WHERE nick_name=%s'
        vars_query = (data['name'],data['password'],data['cpf'],data['email'],data['phone_number'],self.date_time_formate,data['nick_name'])
        self.PSQL.cursor.execute(query_update, vars_query)
        self.PSQL.connection.commit()
        row_count = self.PSQL.cursor.rowcount

        sql_select_query = 'SELECT * FROM users WHERE nick_name=%s'
        vars_query_select= data['nick_name']
        self.PSQL.cursor.execute(sql_select_query, (vars_query_select,))
        record = self.PSQL.cursor.fetchone()
        self.PSQL.cursor.close()
        
        dict_response = {
          'Altered Lines': row_count,
          'nick_name': record[1],
          'name':record[3],
          'password':record[2],
          'cpf':record[4],
          'email':record[5],
          'phone_number':record[6],
          'created_at':str(record[7]),
          'updated_at':str(record[8])
        }

        return dict_response
      except Exception as error:
        print(error)
        return '[X] ERROR IN UPDATED USER INFORMATION IN POSTGRES!'
      

    