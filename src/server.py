from flask import *
from lists import *
from cards import *
from utils import *
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET', 'POST', 'PATCH', 'DELETE', 'OPTIONS'])
@cross_origin()
def root():
    params = request.get_json()
    if request.method == 'GET':
        return index_handler()
    elif request.method == 'POST':
        return create_handler(params)
    elif request.method == 'PATCH':
        return update_handler(params)
    elif request.method == 'DELETE':
        return delete_handler(params)
    elif request.method == 'OPTIONS':
        return options_handler()
    else:
        return response(404, {})


@app.route('/cards', methods=['POST', 'DELETE', 'OPTIONS'])
@cross_origin()
def cards():
    params = request.get_json()
    if request.method == 'POST':
        return create_handler_cards(params)
    elif request.method == 'DELETE':
        return delete_handler_cards(params)
    elif request.method == 'OPTIONS':
        return options_handler_cards()
    else:
        return response(404, {})

app.run()
