#!/usr/bin/python
# -*- encoding: utf-8 -*-

import json, pika

from database_controller.postgres_worker import PostgresWorker


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
        psql = PostgresWorker()
        if data['type'] == 'create':
            return psql.insert_user(data)
        elif data['type'] == 'update':
            return psql.alter_user(data)
        elif data['type'] == 'all_user':
            return psql.show_all_user()
        elif data['type'] == 'show_user':
            return psql.show_one_user(data)
        elif data['type'] == 'delete_user':
            return psql.delete_user(data)
# if __name__ == '__main__':

#     RMQ = RabbitMqCreate()
#     RMQ.recive_queues()
