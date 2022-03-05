from crypt import methods
from traceback import print_tb
from flask import Flask, jsonify, render_template, abort, request, redirect, url_for
from numpy import save
from model import db, save_db

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template(
        'welcome.html',
        cards = db
        )

@app.route('/card/<int:card_id>')
def card_view(card_id):
    try:
        return render_template(
            'cards.html',
            card_id=card_id,
            card=db[card_id],
            max_id=len(db) - 1
            )
    except IndexError:
        abort(404)

@app.route('/api/card')
def card_list():
    return jsonify(db)

@app.route('/api/card/<int:card_id>')
def card_api(card_id):
    try:
        return db[card_id]
    except IndexError:
        abort(404)

@app.route('/add_card', methods=["GET", "POST"])
def add_card():
    if request.method == "POST":
        new_card = {
            "question": request.form["question"],
            "answer": request.form["answer"]
        }
        db.append(new_card)
        save_db(db)
        return redirect(url_for('card_view', card_id=len(db) - 1))
    else:
        return render_template('add_card.html')

@app.route('/delete_card/<int:card_id>', methods=["GET", "POST"])
def delete_card(card_id):
    if request.method == "POST":
        del db[card_id]
        save_db(db)
        return redirect(url_for('hello_world'))
    else:
        return render_template('delete_card.html', card=db[card_id])
