import uuid
import json
import db
from utils import *


def index_handler():
    table_results = db.execute('SELECT * FROM lists')
    cards_results = db.execute('SELECT * FROM cards')
    res = []
    for i in table_results:
        cards = []
        for j in cards_results:
            if i['id'] == j['listId']:
                cards.append(j)
        item = {
            'id': i['id'],
            'name': i['name'],
            'cards': cards
        }
        res.append(item)
    return response(200, json.dumps(res))


def create_handler(params):
    id = db.insert('INSERT INTO lists(name) VALUES("' + params['title'] + '")')
    return response(200, json.dumps({'id': id}))


def update_handler(params):
    # TODO Add db handling
    '''utils.dynamodb.update_item(table_name, {'id': params['id']},
                                           {'attribute': 'title', 'value': params['title']})'''
    return response(200, {})


def delete_handler(params):
    # TODO Add db handling
    '''params = json.loads(params["body"])
    dynamodb = boto3.client('dynamodb')
    dynamodb.delete_item(TableName=table_name,
                         Key={
                             'id': {'S': params['id']}
                         })'''
    return response(200, {})


def options_handler():
    return response(200, {})
