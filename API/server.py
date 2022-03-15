#!/usr/bin/python
# -*- encoding: utf-8 -*-

import json
from flask import Flask, request
from queues.send_queue import RabbitMqSend
from queues.rabbit_server import RabbitMqCreate
from database.connection_db import ConnectionDatabase

Rmq = RabbitMqSend()

class Api_server():

    def __init__(self):
        pass
    
    app = Flask(__name__)
    database = ConnectionDatabase()
    database.create_tables()
    queue_create = RabbitMqCreate()
    queue_create.create_queues()

    # User Routes

    @app.route("/user/create_user/", methods=['POST'])
    def create_user():
        if request.method == 'POST':
            imput_msg = request.get_json()
            imput_msg['type']='create'
            print(imput_msg)
            Rmq.send_msg(route="user", msg=json.dumps(imput_msg))
            return {'Status': 200, 'Message': 'Send to queue user -> create'}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/user/list_user/", methods=['GET'])
    def list_user():
        if request.method == 'GET':
            return {'Status': 200, 'Message': 'bem vindo'}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/user/display_user/", methods=['GET'])
    def display_user():
        if request.method == 'GET':
            return {'Status': 200, 'Message': 'bem vindo'}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/user/edit_user/", methods=['POST'])
    def edit_user():
        if request.method == 'POST':
            return {'Status': 200, 'Message': 'bem vindo'}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/user/delete_user/", methods=['DELETE'])
    def delete_user():
        if request.method == 'DELETE':
            return {'Status': 200, 'Message': 'bem vindo'}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    # Order Routes
    @app.route("/order/create_order/", methods=['POST'])
    def create_order():
        if request.method == 'POST':
            imput_msg = request.get_json()
            Rmq.send_msg(route="order", msg=imput_msg)

            return {'Status': 200, 'Message': imput_msg}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/order/list_order/", methods=['GET'])
    def list_order():
        if request.method == 'GET':
            return {'Status': 200, 'Message': 'bem vindo'}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/order/display_by_order/", methods=['GET'])
    def display_by_order():
        if request.method == 'GET':
            return {'Status': 200, 'Message': 'bem vindo'}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/order/edit_order/", methods=['POST'])
    def edit_order():
        if request.method == 'POST':
            return {'Status': 200, 'Message': 'bem vindo'}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/order/delete_order/", methods=['DELETE'])
    def delete_order():
        if request.method == 'DELETE':
            return {'Status': 200, 'Message': 'bem vindo'}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    app.run('0.0.0.0', 7000)


# if __name__ == '__main__':

#     APP = Api_server()
#     APP.app.run('0.0.0.0', 7000)
