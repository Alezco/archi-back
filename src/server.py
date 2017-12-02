from flask import *
from lists import *
import cards

app = Flask(__name__)


@app.route('/lists', methods=['GET', 'POST', 'PATCH', 'DELETE', 'OPTIONS'])
def lists():
    if request.method == 'GET':
        return index_handler()
    elif request.method == 'POST':
        return lists.create_handler(None)
    elif request.method == 'PATCH':
        return lists.update_handler(None)
    elif request.method == 'DELETE':
        return lists.delete_handler(None)
    elif request.method == 'OPTIONS':
        return lists.options_handler()
    else:
        print('Unhandled request')
        return Response('Unhandled request')


@app.route('/cards', methods=['POST', 'DELETE', 'OPTIONS'])
def cards():
    if request.method == 'POST':
        return cards.create_handler(None)
    elif request.method == 'DELETE':
        return cards.delete_handler(None)
    elif request.method == 'OPTIONS':
        return cards.options_handler()
    else:
        print('Unhandled request')
        return Response('Unhandled request')

app.run()
