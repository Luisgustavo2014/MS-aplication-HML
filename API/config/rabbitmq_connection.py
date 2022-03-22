#!/usr/bin/python
# -*- encoding: utf-8 -*-

import pika, uuid, time

# HOST_RABBIT = os.environ['HOST']
HOST_RABBIT = '144.22.139.197'

class RabbitConnection():

    def __init__(self) :
        try:
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=HOST_RABBIT, port=5672))
            self.channel = self.connection.channel()
            print('[✓] Connected to RabbitMQ server')

            # self.result = self.channel.queue_declare(queue='', exclusive=True)
            # self.callback_queue = self.result.method.queue
            # self.channel.basic_consume(
            #     queue=self.callback_queue,
            #     on_message_callback=self.on_response,
            #     auto_ack=True)
            
        except Exception as error:
            print(f'[X] CONNECTING RABBIT MQ ERROR: {error}')

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def send_msg(self, data, route):
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key=route,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(data))
        print("     [✓] Sent 'Message'")
        while self.response is None:
            self.connection.process_data_events()
        time.sleep(5)
        self.channel.queue_delete(queue=self.callback_queue)
        return self.response
        

    def create_queues(self):
        self.channel.queue_declare(queue='user')
        self.channel.queue_declare(queue='order')
        

        print('     [✓] Queues created successful!')

