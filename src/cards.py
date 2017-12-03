import uuid
import json
import db
from utils import *


def create_handler_cards(params):
    # TODO Add db handling
    '''params = json.loads(params["body"])
    list = dynamodb.get_item(table_name, {'id': params['list_id']})
    card = {
        'id': str(uuid.uuid4()),
        'question': params["question"],
        'answer': params["answer"],
        'date': params["date"],
    }
    cards = list['cards']
    cards.append(card)
    dynamodb.update_item(table_name, {'id': list['id']}, {'attribute': 'cards', 'value': cards})
    return response(200, card)'''


def delete_handler_cards(params):
    # TODO Add db handling
    '''params = json.loads(params["body"])
    list = dynamodb.get_item(table_name, {'id': params['list_id']})
    card_id = params['card_id']
    cards = [card for card in list['cards'] if card['id'] != card_id]
    dynamodb.update_item(table_name, {'id': list['id']}, {'attribute': 'cards', 'value': cards})'''
    return response(200, {})


def options_handler_cards():
    return response(200, {})
