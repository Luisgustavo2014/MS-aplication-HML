#!/usr/bin/python
# -*- encoding: utf-8 -*-

import json

from database_controller.postgres_worker import PostgresWorker


class RabbitWorker():

    def __init__(self):
        self.data = ''
        self.PSQL = PostgresWorker()

    def callback(self, ch, method, properties, body):
        self.data = json.loads(body)

        self.database_manipulation(self.data)

    def database_manipulation(self, data):
        print(data)
        if data['type'] == 'create':
            self.PSQL.insert_user(data)
        elif data['type'] == 'update':
            pass

if __name__ == '__main__':

    RMQ = RabbitMqCreate()
    RMQ.recive_queues()
