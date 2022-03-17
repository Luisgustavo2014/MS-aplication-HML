#!/usr/bin/python
# -*- encoding: utf-8 -*-

import pika
import os

# HOST_RABBIT = os.environ['HOST']
HOST_RABBIT = '144.22.139.197'

class RabbitConnection():

    def __init__(self) :
        try:
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=HOST_RABBIT, port=5672))
            self.channel = self.connection.channel()
            print('[✓] Connected to RabbitMQ server')
            
        except Exception as error:
            print(f'[X] CONNECTING RABBIT MQ ERROR: {error}')
        
    def create_queues(self):
        
        self.channel.queue_declare(queue='database.user')
        self.channel.queue_declare(queue='database.order')

        self.channel.exchange_declare('database', 'topic',
            durable= True,
            auto_delete= False
        )

        self.channel.queue_bind(queue='database.user', exchange='database')
        self.channel.queue_bind(queue='database.order', exchange='database')

        print('     [✓] Queues created successful!')

