#!/usr/bin/python
# -*- encoding: utf-8 -*-

from flask import Flask, request
from queues.send_queue import RabbitMqSend
from queues.rabbit_server import RabbitMqCreate

Rmq = RabbitMqSend()

class Api_server():

    def __init__(self):
        pass
    
    app = Flask(__name__)
    queue_create = RabbitMqCreate()
    queue_create.create_queues()

    # User Routes

    @app.route("/user/create_user/", methods=['POST'])
    def create_user():
        if request.method == 'POST':
            imput_msg = request.get_json()
            Rmq.send_msg_user(route="user", msg=imput_msg)
            return {'Status': 200, 'Message': imput_msg}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/user/list_user/", methods=['GET'])
    def list_user():
        if request.method == 'GET':
            return {'Status': 200, 'Message': 'bem vindo'}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/user/display_user/", methods=['GET'])
    def display_user(self):
        if request.method == 'GET':
            return {'Status': 200, 'Message': 'bem vindo'}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/user/edit_user/", methods=['POST'])
    def edit_user(self):
        if request.method == 'POST':
            return {'Status': 200, 'Message': 'bem vindo'}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/user/delete_user/", methods=['DELETE'])
    def delete_user(self):
        if request.method == 'DELETE':
            return {'Status': 200, 'Message': 'bem vindo'}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    # Order Routes
    @app.route("/user/create_order/", methods=['POST'])
    def create_order(self):
        if request.method == 'POST':
            imput_msg = request.get_json()
            self.Rmq.send_msg_user(route="order", msg=imput_msg)

            return {'Status': 200, 'Message': imput_msg}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/user/list_order/", methods=['GET'])
    def list_order(self):
        if request.method == 'GET':
            return {'Status': 200, 'Message': 'bem vindo'}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/user/display_by_order/", methods=['GET'])
    def display_by_order(self):
        if request.method == 'GET':
            return {'Status': 200, 'Message': 'bem vindo'}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/user/edit_order/", methods=['POST'])
    def edit_order(self):
        if request.method == 'POST':
            return {'Status': 200, 'Message': 'bem vindo'}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/user/delete_order/", methods=['DELETE'])
    def delete_order(self):
        if request.method == 'DELETE':
            return {'Status': 200, 'Message': 'bem vindo'}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    app.run('0.0.0.0', 7000)


# if __name__ == '__main__':

#     APP = Api_server()
#     APP.app.run('0.0.0.0', 7000)
