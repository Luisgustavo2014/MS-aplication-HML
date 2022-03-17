#!/usr/bin/python
# -*- encoding: utf-8 -*-

import pika

HOST_RABBIT = '144.22.139.197'

class ConnectionRabbitMq():
    
    def __init__(self):
        try:
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=HOST_RABBIT, port=5672))
            self.channel = self.connection.channel()
            print('[✓] Conected to RabbitMQ server')

        except Exception as error:
            print(f'[X] CONNECTING RABBIT MQ ERROR: {error}')

