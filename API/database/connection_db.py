import psycopg2
import os

HOST_DATABSE = os.environ['HOST_DATABASE']

class ConnectionDatabase():

    def __init__(self):
        self.connection  = psycopg2.connect(
            host=HOST_DATABSE,
            port=5432,
            database="baseapplication",
            user="postgres",
            password="postgres")
        self.cursor = self.connection.cursor()
    
    def create_tables(self):
        self.cursor.execute("SELECT version();")
        record = self.cursor.fetchone()
        print("[X] You are connected to - ", record, "\n")

        create_table_query = '''
            CREATE TABLE IF NOT EXISTS users (
                user_id SERIAL NOT NULL,
                name varchar(50) NOT NULL,
                cpf integer NOT NULL,
                email varchar(50) NOT NULL,
                phone_number integer NOT NULL,
                created_at varchar(50),
                updated_at varchar(50),
                PRIMARY KEY (user_id)
            );

            CREATE TABLE IF NOT EXISTS orders (
                order_id SERIAL NOT NULL,
                user_id integer,
                item_description integer NOT NULL,
                item_quantity integer NOT NULL,
                item_price integer NOT NULL,
                PRIMARY KEY (order_id),
                FOREIGN KEY(user_id) REFERENCES users(user_id)
            );'''
        
        self.cursor.execute(create_table_query)
        self.connection.commit()
        print('[X] Created tables on DataBase \n')

        