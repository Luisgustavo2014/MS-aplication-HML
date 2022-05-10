#!/usr/bin/python
# -*- encoding: utf-8 -*-

import json, pika

class RabbitWorker():

    def __init__(self):
        self.data = ''

    def callback(self, ch, method, props, body):
        self.data = json.loads(body)
        response_work = self.database_manipulation(self.data)

        ch.basic_publish(exchange='',
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(
                             correlation_id=props.correlation_id),
                         body=json.dumps(response_work))
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def database_manipulation(self, data):
        # start connection whit postgres
        if data['type'] == 'create':
            pass
        elif data['type'] == 'update':
            pass
        elif data['type'] == 'update_password':
            pass
        elif data['type'] == 'show_all':
            pass
        elif data['type'] == 'show_one':
            pass
        elif data['type'] == 'delete_user':
            pass

# if __name__ == '__main__':

#     RMQ = RabbitMqCreate()
#     RMQ.recive_queues()
