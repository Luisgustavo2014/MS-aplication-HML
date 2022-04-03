#!/usr/bin/python
# -*- encoding: utf-8 -*-

import json
import time
from flask import Flask, request
from flask_caching import Cache  # Import Cache from flask_caching module
from config.database_connection import ConnectionDatabase
from config.rabbitmq_connection import RabbitConnection
from rabbitmq_controller.rabbit_queues import RabbitQueue


rabbit_queues = RabbitQueue()


class Api_server():
    app = Flask(__name__)
    # app.config.from_object({'CACHE_TYPE':'redis', 'CACHE_REDIS_HOST':'144.22.139.197','CACHE_REDIS_PORT':'6379'})  # Set the configuration variables to the flask application
    app.config.from_object('config.redis_connection.BaseConfig')
    cache = Cache(app)  # Initialize Cache
    ConnectionDatabase()
    rabbit_queues.create_queues()

    # ---------------Test Route----------------
    @app.route("/test/", methods=['POST'])
    @cache.cached(timeout=30, query_string=True)
    def test():
        if request.method == 'POST':
            payload = request.get_json()
            payload['type'] = 'create'

            corr_id = rabbit_queues.rpc_async(json.dumps(payload), "user")
            while rabbit_queues.queue[corr_id] is None:
                time.sleep(0.1)

            return {'Status': 200, 'Message': json.loads(rabbit_queues.queue[corr_id])}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    # ---------------User Routes----------------
    @app.route("/user/create_user/", methods=['POST'])
    def create_user():
        if request.method == 'POST':
            payload = request.get_json()
            payload['type'] = 'create'

            corr_id = rabbit_queues.rpc_async(json.dumps(payload), "user")
            while rabbit_queues.queue[corr_id] is None:
                time.sleep(0.1)

            return {'Status': 200, 'Message': json.loads(rabbit_queues.queue[corr_id])}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/user/show_all_user/", methods=['GET'])
    @cache.cached(timeout=30, query_string=True)
    def list_user():
        if request.method == 'GET':
            payload = {'type': 'show_all'}

            corr_id = rabbit_queues.rpc_async(json.dumps(payload), "user")
            while rabbit_queues.queue[corr_id] is None:
                time.sleep(0.1)

            return {'Status': 200, 'Message': json.loads(rabbit_queues.queue[corr_id])}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/user/show_one_user/", methods=['POST'])
    @cache.cached(timeout=30, query_string=True)
    def show_user():
        if request.method == 'POST':
            payload = request.get_json()
            payload['type'] = 'show_one'

            corr_id = rabbit_queues.rpc_async(json.dumps(payload), "user")
            while rabbit_queues.queue[corr_id] is None:
                time.sleep(0.1)

            return {'Status': 200, 'Message': json.loads(rabbit_queues.queue[corr_id])}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/user/edit_user/", methods=['PUT'])
    def edit_user():
        if request.method == 'PUT':
            payload = request.get_json()
            payload['type'] = 'update'

            corr_id = rabbit_queues.rpc_async(json.dumps(payload), "user")
            while rabbit_queues.queue[corr_id] is None:
                time.sleep(0.1)

            return {'Status': 200, 'Message': json.loads(rabbit_queues.queue[corr_id])}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/user/edit_password/", methods=['PUT'])
    def edit_password():
        if request.method == 'PUT':
            payload = request.get_json()
            payload['type'] = 'update_password'

            corr_id = rabbit_queues.rpc_async(json.dumps(payload), "user")
            while rabbit_queues.queue[corr_id] is None:
                time.sleep(0.1)

            return {'Status': 200, 'Message': json.loads(rabbit_queues.queue[corr_id])}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/user/delete_user/", methods=['DELETE'])
    def delete_user():
        if request.method == 'DELETE':
            payload = request.get_json()
            payload['type'] = 'delete_user'

            corr_id = rabbit_queues.rpc_async(json.dumps(payload), "user")
            while rabbit_queues.queue[corr_id] is None:
                time.sleep(0.1)

            return {'Status': 200, 'Message': json.loads(rabbit_queues.queue[corr_id])}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    # -----------------Order Routes-----------------

    @app.route("/order/create_order/", methods=['POST'])
    def create_order():
        if request.method == 'POST':
            imput_msg = request.get_json()
            rabbit_queues.send_msg(route="order", msg=imput_msg)

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
