from flask import Flask, jsonify, request

import time
from threading import Thread

from auto_reger import run

app = Flask(__name__)


@app.route('/register', methods=['POST'])
def echo():

    print(request.get_json(force=True))
    th = Thread(target=run, args=(request.get_json(force=True),))
    th.start()

    return jsonify(request.get_json(force=True))



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000, debug=True)
