#!/usr/bin/python
# -*- encoding: utf-8 -*-

import pika
import os

HOST_RABBIT = os.environ['HOST']

class RabbitMqCreate():

    def callback(self, ch, method, properties, body):
        print(f" [X] Received {body}")

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


# if __name__ == '__main__':

#     RMQ = RabbitMqCreate()
#     RMQ.recive_queues()
