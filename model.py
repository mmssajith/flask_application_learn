'''
Fulfil the database needs for the project.
'''

import json

def load_db():
    with open('db.json', 'r') as f:
        return json.load(f)

def save_db(db):
    with open('db.json', 'w') as f:
        json.dump(db, f)

def delete_card(card_id):
    db.pop(card_id)

db = load_db()