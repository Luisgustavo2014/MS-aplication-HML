#!/usr/bin/python
# -*- encoding: utf-8 -*-

from config.rabbitmq_connection import RabbitConnection

class RabbitMqSend():

    def send_msg(self,route, msg):
        rabbit_config = RabbitConnection()
        rabbit_config.channel.basic_publish(exchange='database', routing_key=route, body=str(msg))
        print("     [✓] Sent 'Message'")
        rabbit_config.connection.close()
