from flask import *
from lists import *
from cards import *

app = Flask(__name__)


@app.route('/lists', methods=['GET', 'POST', 'PATCH', 'DELETE', 'OPTIONS'])
def lists():
    params = request.form.to_dict()
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
        print('Unhandled request')
        return Response('Unhandled request')


@app.route('/cards', methods=['POST', 'DELETE', 'OPTIONS'])
def cards():
    params = request.form.to_dict()
    if request.method == 'POST':
        return create_handler_cards(params)
    elif request.method == 'DELETE':
        return delete_handler_cards(params)
    elif request.method == 'OPTIONS':
        return options_handler_cards()
    else:
        print('Unhandled request')
        return Response('Unhandled request')

app.run()
