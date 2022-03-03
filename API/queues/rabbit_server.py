#!/usr/bin/python
# -*- encoding: utf-8 -*-

import pika


class RabbitMqCreate():

    def create_queues(self):
        try:
            print('[X] Connetcting RabbitMQ server')
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='localhost', port=5672))
            channel = connection.channel()

        except Exception as e:
            print(f'[X] CONNECTING ERROR: {e}')

        channel.queue_declare(queue='user')
        channel.queue_declare(queue='order')

        print('     [*] Queues created successful!')


# if __name__ == '__main__':

#     RMQ = RabbitMqCreate()
#     RMQ.create_queues()
