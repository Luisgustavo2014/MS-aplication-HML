
#!/usr/bin/python
# -*- encoding: utf-8 -*-

from re import T
import pika, uuid, time
from config.rabbitmq_connection import RabbitConnection

class RabbitQueue():

    def __init__(self) :
        self.RMQ = RabbitConnection()

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def send_msg(self, data, route):
        
        result = self.RMQ.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.RMQ.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.RMQ.channel.basic_publish(
            exchange='',
            routing_key=route,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(data))
        print("     [✓] Sent 'Message'")
        while self.response is None:
            self.RMQ.connection.process_data_events(time_limit=0)
        time.sleep(5)
        self.RMQ.channel.queue_delete(queue=self.callback_queue)
        return self.response
        

    def create_queues(self):
        self.RMQ.channel.queue_declare(queue='user')
        self.RMQ.channel.queue_declare(queue='order')
        

        print('     [✓] Queues created successful!')

