#!/usr/bin/python
# -*- encoding: utf-8 -*-

import pika, os, json
from pprint import pprint
from database_controller.database_manipulation import PostrgesManipulation

HOST_RABBIT = os.environ['HOST']


class RabbitMqCreate():

    def __init__(self):
        self.type_of=''
        self.PSQL = PostrgesManipulation()

    def callback(self, ch, method, properties, body):
        self.type_of = json.loads(body)

        self.database_manipulatio(self.type_of)
        
    def recive_queues(self):
        try:
            print('[X] Connetcting RabbitMQ server')
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=HOST_RABBIT, port=5672))
            channel = connection.channel()

        except Exception as e:
            print(f'[X] CONNECTING ERROR: {e}')


        channel.basic_consume(
            queue='user', on_message_callback=self.callback, auto_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()

    def database_manipulatio(self, data):
        data['type']

        if data['type'] == 'crerate':
            self.PSQL.insert_user(data)


# if __name__ == '__main__':

#     RMQ = RabbitMqCreate()
#     RMQ.recive_queues()
