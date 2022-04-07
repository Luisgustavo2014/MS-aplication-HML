import psycopg2

from config.database_connection import ConnectionDatabase
from datetime import datetime


class PostgresWorker():

    def __init__(self):
        self.PSQL = ConnectionDatabase()
        self.date_time = datetime.now()
        self.date_time_formate = self.date_time.strftime('%Y/%m/%d %H:%M')

    
    def create_order(self, data):
        try:
            user_id = self.information_user(data['nick_name'])
            if user_id == None:
                return f"[X] DON'T HAVE THIS USER IN DATA-BASE!"

            total_value = data['item_quantity'] * data['item_price']

            query_insert = 'INSERT INTO orders (user_id ,item_description ,item_quantity , item_price, total_value, created_at, updated_at)VALUES (%s,%s,%s,%s,%s,%s,%s)'
            vars_query = (user_id[0], data['item_description'], data['item_quantity'],
                          data['item_price'], total_value, self.date_time_formate, self.date_time_formate)
            self.PSQL.cursor.execute(query_insert, vars_query)
            self.PSQL.connection.commit()

            print('[✓] INSERTION DONE IN POSTGRES!')
            return '[✓] Order created successfully! '
        except Exception as error:
            print(error)
            return f'[X] ERROR INSERTING IN POSTGRES! {error}'
        finally:
            self.PSQL.cursor.close()
        pass

    def edit_order(self, data):
        try:
            user_id = self.information_user(data['nick_name'])
            if user_id == None:
                return f"[X] DON'T HAVE THIS USER IN DATA-BASE!"

            total_value = data['item_quantity'] * data['item_price']
            
            query_update = 'UPDATE orders SET user_id=%s, item_description=%s, item_quantity=%s, item_price=%s, total_value=%s, updated_at=%s WHERE order_id=%s'
            vars_query = (user_id[0], data['item_description'], data['item_quantity'],
                          data['item_price'], total_value, self.date_time_formate, data['order_id'])
            self.PSQL.cursor.execute(query_update, vars_query)
            self.PSQL.connection.commit()
            row_count = self.PSQL.cursor.rowcount
            record = self.information_order(data['order_id'])

            if record == None:
                return record

            dict_response = {
                'Altered Lines': row_count,
                'order_id': record[0],
                'user_id': record[1],
                'item_description': record[2],
                'item_quantity': record[3],
                'item_price': record[4],
                'total_value': record[5],
                'created_at': str(record[6]),
                'updated_at': str(record[7])
            }
            print('[✓] UPDADE DONE SUCCESSFULLY IN POSTGRES!')
            return dict_response
        except Exception as error:
            print(error)
            return f'[X] ERROR IN UPDATED ORDER INFORMATION IN POSTGRES! {error}'
        finally:
            self.PSQL.cursor.close()

    def list_all_orders(self):
        pass

    def list_for_users(self):
        pass

    def show_order(self):
        pass

    def delete_order(self):
        pass

    # get all user's ID on database
    def information_user(self, data):
        try:
            sql_select_query = 'SELECT user_id FROM users WHERE nick_name=%s'
            vars_query_select = data
            self.PSQL.cursor.execute(sql_select_query, (vars_query_select,))
            record = self.PSQL.cursor.fetchone()
            return record
        except Exception as error:
            print(error)
            return f'[X] ERROR ON SELECT ID_USER IN POSTGRES! \
        {error}'

    
     # get all order's irformation on database
    def information_order(self, data):
        try:
            sql_select_query = 'SELECT * FROM orders WHERE order_id=%s'
            vars_query_select = data
            self.PSQL.cursor.execute(sql_select_query, (vars_query_select,))
            record = self.PSQL.cursor.fetchone()
            return record
        except Exception as error:
            print(error)
            return f'[X] ERROR ON SELECT ORDER INFORMATION IN POSTGRES! \
        {error}'
        finally:
            self.PSQL.cursor.close()

    
