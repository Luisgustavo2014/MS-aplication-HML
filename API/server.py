#!/usr/bin/env python

#          ──▒▒▒▒▒────▄████▄─────
#          ─▒─▄▒─▄▒──███▄█▀──────
#          ─▒▒▒▒▒▒▒─▐████──█──█──
#          ─▒▒▒▒▒▒▒──█████▄──────
#          ─▒─▒─▒─▒───▀████▀─────
#   ꧁——————Patrick Piccini——————꧂


from flask import Flask, request

app = Flask(__name__)

### User Routes
@app.route("/user/create_user/", methods=['POST'])
def create_user():
    if request.method == 'POST':
        return {'Status': 200, 'Message':'bem vindo'}
    else:
        return {'Status': 404, 'Message':'Erro no envio do method'}


@app.route("/user/list_user/", methods=['GET'])
def list_user():
    if request.method == 'GET':
        return {'Status': 200, 'Message':'bem vindo'}
    else:
        return {'Status': 404, 'Message':'Erro no envio do method'}


@app.route("/user/display_user/", methods=['GET'])
def display_user():
    if request.method == 'GET':
        return {'Status': 200, 'Message':'bem vindo'}
    else:
        return {'Status': 404, 'Message':'Erro no envio do method'}


@app.route("/user/edit_user/", methods=['POST'])
def edit_user():
    if request.method == 'POST':
        return {'Status': 200, 'Message':'bem vindo'}
    else:
        return {'Status': 404, 'Message':'Erro no envio do method'}


@app.route("/user/delete_user/", methods=['DELETE'])
def delete_user():
    if request.method == 'DELETE':
        return {'Status': 200, 'Message':'bem vindo'}
    else:
        return {'Status': 404, 'Message':'Erro no envio do method'}



### Order Routes
@app.route("/user/create_order/", methods=['POST'])
def create_order():
    if request.method == 'POST':
        return {'Status': 200, 'Message':'bem vindo'}
    else:
        return {'Status': 404, 'Message':'Erro no envio do method'}


@app.route("/user/list_order/", methods=['GET'])
def list_order():
    if request.method == 'GET':
        return {'Status': 200, 'Message':'bem vindo'}
    else:
        return {'Status': 404, 'Message':'Erro no envio do method'}


@app.route("/user/display_by_order/", methods=['GET'])
def display_by_order():
    if request.method == 'GET':
        return {'Status': 200, 'Message':'bem vindo'}
    else:
        return {'Status': 404, 'Message':'Erro no envio do method'}


@app.route("/user/edit_order/", methods=['POST'])
def edit_user():
    if request.method == 'POST':
        return {'Status': 200, 'Message':'bem vindo'}
    else:
        return {'Status': 404, 'Message':'Erro no envio do method'}


@app.route("/user/delete_prder/", methods=['DELETE'])
def delete_user():
    if request.method == 'DELETE':
        return {'Status': 200, 'Message':'bem vindo'}
    else:
        return {'Status': 404, 'Message':'Erro no envio do method'}



app.run('0.0.0.0', 7000)