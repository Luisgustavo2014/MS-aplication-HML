import psycopg2
import os

# HOST_DATABSE = os.environ['HOST_DATABASE'] or '144.22.139.197'
HOST_DATABSE = '144.22.139.197'

class ConnectionDatabase():

    def __init__(self):
        self.connection  = psycopg2.connect(
            host=HOST_DATABSE,
            port=5432,
            database="baseapplication",
            user="postgres",
            password="postgres")
        self.cursor = self.connection.cursor()
  