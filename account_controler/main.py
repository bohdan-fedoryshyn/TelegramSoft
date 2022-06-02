import asyncio

from flask import Flask, jsonify, request

import time
from threading import Thread
from controler import Controler

app = Flask(__name__)
controller = Controler()

@app.route('/add_account', methods=['POST'])
def add_account():
    phone_number = request.get_json(force=True)['phone_number']
    #th = Thread(target=controller.add_account, args=(phone_number,))
    #th.start()

    asyncio.set_event_loop(asyncio.SelectorEventLoop())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(controller.add_account(phone_number))

    controller.add_account(phone_number)
    return jsonify("200")

@app.route('/set_code', methods=['POST'])
def set_code():
    phone_number = request.get_json(force=True)['phone_number']
    code = request.get_json(force=True)['code']
    owner_id = request.get_json(force=True)['owner_id']
    #th = Thread(target=controller.set_code, args=(phone_number,code,))
    #th.start()

    asyncio.set_event_loop(asyncio.SelectorEventLoop())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(controller.set_code(phone_number, code))

    controller.set_code(phone_number, code,owner_id)
    return jsonify("200")


@app.route('/update', methods=['POST'])
def accounts_update():
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000, debug=True)
