#!/usr/bin/env python
import pika


class RabbitMq():

    def callback(self, ch, method, properties, body):
        print("     [x] Received %r" % body)

    def recive_msg(self):
        try:
            print('[X] Connetcting server')
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='localhost', port=5672))
            channel = connection.channel()

        except Exception as e:
            print(f'[X] CONNECTING ERROR: {e}')

        channel.queue_bind(queue='user',exchange='user_exchange')
        channel.queue_bind(queue='order',exchange='order_exchange')

        channel.basic_consume(
            queue='user', on_message_callback=self.callback, auto_ack=True)
        channel.basic_consume(
            queue='order', on_message_callback=self.callback, auto_ack=True)

        print('     [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()


if __name__ == '__main__':

    RMQ = RabbitMq()
    RMQ.recive_msg()
