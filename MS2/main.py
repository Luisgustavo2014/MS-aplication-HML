from rabbit_recive.revice_queue import RabbitMqCreate
from database_controller.database_manipulation import PostrgesManipulation

class Main():

    def __init__(self):
        self.RMQ = RabbitMqCreate()
        self.PSQL = PostrgesManipulation()

    def initialize_services(self):
        self.PSQL.select_version()
        self.RMQ.recive_queues()
        

if __name__ == '__main__':

    MA = Main()
    MA.initialize_services()
