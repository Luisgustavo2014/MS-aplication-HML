import psycopg2

from .database_connection import Connection

PSQL = Connection()

class PostrgesManipulation():

    def __init__(self) :
      self.PSQL = Connection()

    def select_version(self):
        print("PostgreSQL server information")
        print(self.PSQL.connection.get_dsn_parameters(), "\n")
        self.PSQL.cursor.execute("SELECT version();")

        record = self.PSQL.cursor.fetchone()
        print("You are connected to - ", record, "\n")
