import json
import db
from utils import *


def create_handler_cards(params):
    card = {
        'answer': params['answer'],
        'question': params['question'],
        'date': params['date'],
        'listId': params['list_id']
    }
    card['id'] = db.write('INSERT INTO cards(answer, question, date, listId) VALUES("' +
                          card['answer'] + '", "' + card['question'] + '", "' + card['date'] + '", "' + card['listId'] + '")')
    return response(200, json.dumps(card))


def delete_handler_cards(params):
    db.write('DELETE FROM cards WHERE id = ' + str(params['id']))
    return response(200, {})


def options_handler_cards():
    return response(200, {})
