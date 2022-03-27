from socket import errorTab
import psycopg2

from config.database_connection import ConnectionDatabase
from datetime import datetime


class PostgresWorker():

    def __init__(self) :
      self.PSQL = ConnectionDatabase()
      self.date_time = datetime.now()
      self.date_time_formate = self.date_time.strftime('%Y/%m/%d %H:%M')

    # create a user in database
    def insert_user(self, data):

      try:
        query_insert = 'INSERT INTO users (_name, nick_name ,password ,cpf , email, phone_number, created_at, updated_at)VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
        vars_query = (data['name'],data['nick_name'],data['password'],data['cpf'],data['email'],data['phone_number'],self.date_time_formate,self.date_time_formate)
        self.PSQL.cursor.execute(query_insert, vars_query)
        self.PSQL.connection.commit()
        self.PSQL.cursor.close()

        print('[✓] INSERTION DONE IN POSTGRES!')
        return '[✓] User created successfully! '
      except Exception as error:
        print(error)
        return f'[X] ERROR INSERTING IN POSTGRES! \
        {error}'

    # Modify the informations of a user 
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
        print('[✓] UPDADE DONE SUCCESSFULLY IN POSTGRES!')
        return dict_response
      except Exception as error:
        print(error)
        return f'[X] ERROR IN UPDATED USER INFORMATION IN POSTGRES! \
        {error}'
    
    # Show all user on batabase
    def show_all_user(self):
      try:
        sql_select_query = 'SELECT * FROM users'
        self.PSQL.cursor.execute(sql_select_query)
        record = self.PSQL.cursor.fetchall()
        self.PSQL.connection.commit()

        dict_all_users = []
        for index in range(len(record)):
          dict_response = {
              'nick_name': record[index][1],
              'name':record[index][3],
              'email':record[index][5],
              'phone_number':record[index][6],
              'created_at':str(record[index][7]),
              'updated_at':str(record[index][8])
            
          }
          dict_all_users.append(dict_response)
        
        self.PSQL.cursor.close()
        print('[✓] SELECT DONE SUCCESSFULLY IN POSTGRES!')
        return {'users':dict_all_users}
      except Exception as error:
        print(error)
        return f'[X] ERROR ON SELECT IN POSTGRES! \
        {error}'

    # Show a user on database
    def show_one_user(self, data):
      try:
        sql_select_query = 'SELECT * FROM users WHERE nick_name=%s'
        vars_query_select= data['nick_name']
        self.PSQL.cursor.execute(sql_select_query, (vars_query_select,))
        record = self.PSQL.cursor.fetchone()
        dict_response = {
          'nick_name': record[1],
          'name':record[3],
          'email':record[5],
          'phone_number':record[6],
          'created_at':str(record[7]),
          'updated_at':str(record[8])
        }
        self.PSQL.cursor.close()
        print('[✓] SELECT DONE SUCCESSFULLY IN POSTGRES!')
        return dict_response
      except Exception as error:
        print(error)
        return f'[X] ERROR ON SELECT IN POSTGRES! \
        {error}'
    
    # Delete a user on database
    def delete_user(self, data):
      try:
        sql_delete_query = 'DELETE FROM users WHERE nick_name=%s'
        vars_query_select= data['nick_name']
        self.PSQL.cursor.execute(sql_delete_query, (vars_query_select,))
        row_count = self.PSQL.cursor.rowcount
        self.PSQL.connection.commit()
        self.PSQL.cursor.close()

        print('[✓] DELETE DONE SUCCESSFULLY IN POSTGRES!')
        return {'Altered Lines':row_count}
      except Exception as error:
        print(error)
        return f'[X] ERROR ON DELETE IN POSTGRES! \
        {error}'
    
    