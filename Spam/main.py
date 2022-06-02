from flask import Flask, jsonify, request

import time
from threading import Thread

from Spamer import run

app = Flask(__name__)


@app.route('/spam', methods=['POST'])
app.config['SERVER_NAME'] = '0.0.0.0:5003'

def echo():
    th = Thread(target=run, args=(request.get_json(force=True),))
    th.start()

    return jsonify(request.get_json(force=True))




if __name__ == '__main__':
    app.run(debug=True)



