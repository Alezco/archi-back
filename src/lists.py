import json
import db
from utils import *


def index_handler():
    table_results = db.read('SELECT * FROM lists')
    cards_results = db.read('SELECT * FROM cards')
    res = []
    for i in table_results:
        cards = []
        for j in cards_results:
            if i['id'] == j['listId']:
                cards.append(j)
        item = {
            'id': i['id'],
            'title': i['name'],
            'cards': cards
        }
        res.append(item)
    return response(200, json.dumps(res))


def create_handler(params):
    print(params)
    id = db.write('INSERT INTO lists(name) VALUES("' + params['title'] + '")')
    return response(200, json.dumps({'id': id}))


def update_handler(params):
    db.write('UPDATE lists SET name = "' + params['title'] + '" WHERE lists.id = ' + str(params['id']))
    return response(200, {})


def delete_handler(params):
    db.write('DELETE FROM lists WHERE id = ' + str(params['id']))
    return response(200, {})


def options_handler():
    return response(200, {})
