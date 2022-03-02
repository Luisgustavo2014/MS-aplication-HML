#!/usr/bin/env python
import pika

class RabbitMq():

    def send_msg_user(self, msg):
        try:
            print('[X] Connetcting server')
            connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',port=5672))
            channel = connection.channel()

        except Exception as e:
            print(f'[X] CONNECTING ERROR: {e}')

        channel.basic_publish(exchange='', routing_key='user', body='Hello World for user!')

        print("     [X] Sent 'Message'")
        connection.close()

if __name__ == '__main__':

    RMQ = RabbitMq()
    RMQ.send_msg_user()
