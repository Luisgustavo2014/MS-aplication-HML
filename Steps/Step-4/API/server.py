#!/usr/bin/python
# -*- encoding: utf-8 -*-

from flask import Flask, request


class Api_server():
    app = Flask(__name__)

    # ---------------User Routes----------------
    @app.route("/user/create_user/", methods=['POST'])
    def create_user():
        if request.method == 'POST':
            payload = request.get_json()

            return {'Status': 200, 'Message': payload}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/user/show_all_user/", methods=['GET'])
    def list_user():
        if request.method == 'GET':
            payload = request.get_json()

            return {'Status': 200, 'Message': payload}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/user/show_one_user/", methods=['POST'])
    def show_user():
        if request.method == 'POST':
            payload = request.get_json()

            return {'Status': 200, 'Message': payload}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/user/edit_user/", methods=['PUT'])
    def edit_user():
        if request.method == 'PUT':
            payload = request.get_json()

            return {'Status': 200, 'Message': payload}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/user/edit_password/", methods=['PUT'])
    def edit_password():
        if request.method == 'PUT':
            payload = request.get_json()

            return {'Status': 200, 'Message': payload}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/user/delete_user/", methods=['DELETE'])
    def delete_user():
        if request.method == 'DELETE':
            payload = request.get_json()

            return {'Status': 200, 'Message': payload}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    # -----------------Order Routes-----------------

    @app.route("/order/create_order/", methods=['POST'])
    def create_order():
        if request.method == 'POST':
            payload = request.get_json()

            return {'Status': 200, 'Message': payload}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/order/list_order/", methods=['GET'])
    def list_order():
        if request.method == 'GET':
            payload = request.get_json()

            return {'Status': 200, 'Message': payload}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/order/display_by_order/", methods=['GET'])
    def display_by_order():
        if request.method == 'GET':
            payload = request.get_json()

            return {'Status': 200, 'Message': payload}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/order/edit_order/", methods=['POST'])
    def edit_order():
        if request.method == 'POST':
            payload = request.get_json()

            return {'Status': 200, 'Message': payload}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    @app.route("/order/delete_order/", methods=['DELETE'])
    def delete_order():
        if request.method == 'DELETE':
            payload = request.get_json()

            return {'Status': 200, 'Message': payload}
        else:
            return {'Status': 404, 'Message': 'Erro no envio do method'}

    app.run('0.0.0.0', 7000)


if __name__ == '__main__':

    APP = Api_server()
    APP.app.run('0.0.0.0', 7000)
