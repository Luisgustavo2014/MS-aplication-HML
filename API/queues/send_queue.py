#!/usr/bin/python
# -*- encoding: utf-8 -*-

import pika
import os

# HOST_RABBIT = os.environ['HOST']
HOST_RABBIT = '144.22.139.197'

class RabbitMqSend():

    def send_msg(self, route, msg):
        try:
            print('[X] Connetcting server')
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=HOST_RABBIT, port=5672))
            channel = connection.channel()

        except Exception as e:
            print(f'[X] CONNECTING ERROR: {e}')

        channel.basic_publish(exchange='', routing_key=route, body=str(msg))

        print("     [X] Sent 'Message'")
        connection.close()


# if __name__ == '__main__':

#     RMQ = RabbitMq()
#     RMQ.send_msg_user()
