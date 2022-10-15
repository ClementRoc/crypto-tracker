import json
import config

from flask import request, redirect
from flask_sqlalchemy import SQLAlchemy
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from cryptoapp import app

db = SQLAlchemy(app)

"""
Initiate the database
"""


def init_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.commit()


class Crypto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    symbol = db.Column(db.String(200), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    # Price you bought it
    price = db.Column(db.Integer, nullable=False)
    # Market value of the crypto
    value = db.Column(db.Integer, nullable=False)
    percent_change_24h = db.Column(db.Float, nullable=False)

    def __init__(self, name, symbol, quantity, price, value, percent_change_24h):
        self.name = name
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.value = value
        self.percent_change_24h = percent_change_24h


"""
Link between the form in add.html and the Crypto database
"""


@app.route('/add_data', methods=['POST'])
def add_data():
    # Get all the data from the form
    name = request.form.get('name')
    quantity = int(request.form.get('quantity'))
    price = int(request.form.get('price'))

    # Query, filtering by name, into the Crypto database
    crypto = Crypto.query.filter_by(name=name).first()

    # Condition if you are adding new data
    if not crypto:
        crypto_data = get_crypto_data(name)

        value = int(crypto_data['value']) * quantity
        price = price
        symbol = crypto_data['symbol']
        percent_change_24h = crypto_data['percent_change_24h']

        c = Crypto(name, symbol, quantity, price, value, percent_change_24h)
        db.session.add(c)
        db.session.commit()

    # Condition if you are adding new quantity to data already been there
    elif crypto in Crypto.query.all():
        crypto_data = get_crypto_data(name)

        crypto.quantity += quantity
        crypto.price += price
        crypto.value = int(crypto_data['value']) * crypto.quantity
        db.session.commit()

    return redirect('/')


"""
Link between the form in edit.html and the Crypto database
"""


@app.route('/edit_data', methods=['POST'])
def edit_data():
    # Get all the data from the form
    name = request.form.get('name')
    quantity = int(request.form.get('quantity'))

    # Get the data from CoinMarketCap
    crypto_data = get_crypto_data(name)

    # Query, filtering by name, into the Crypto database
    crypto = Crypto.query.filter_by(name=name).first()

    crypto.quantity -= quantity

    # Delete the crypto if the quantity is equal to 0
    if crypto.quantity == 0 or crypto.quantity < 0:
        db.session.delete(crypto)

    crypto.price -= int(crypto_data['value']) * quantity
    crypto.value = int(crypto_data['value']) * crypto.quantity

    db.session.commit()
    return redirect('/')


"""
Query the crypto data from CoinMarketCap based on the name
"""


def get_crypto_data(name):
    # Get the data
    data = coinmarket_parameters(name, config.COINMARKET_API_QUOTES_URL)

    crypto = json.loads(data.text)['data']
    crypto_data = list(crypto.values())[0]

    # Distribute the data into variables and the final dictionary
    value = crypto_data['quote']['EUR']['price']
    percent_change_24h = crypto_data['quote']['EUR']['percent_change_24h']
    symbol = crypto_data['symbol']

    data = {'value': value, 'symbol': symbol, 'percent_change_24h': percent_change_24h}

    return data


"""
Query all the crypto data from CoinMarketCap and add it up to a list
"""


def get_all_crypto():
    # Get data
    crypto = coinmarket_parameters(None, config.COINMARKET_API_LISTING_URL)
    crypto_json = json.loads(crypto.text)['data']

    crypto_list = []

    # Add all the data to the list
    for data in crypto_json:
        crypto = {}
        name = data['name']
        symbol = data['symbol']
        value = data['quote']['EUR']['price']
        crypto['name'] = name
        crypto['symbol'] = symbol
        crypto['value'] = round(value)
        crypto_list.append(crypto)

    return crypto_list


"""
Define the parameters of the Query
"""


def coinmarket_parameters(name, url):
    if name is not None:
        name = name.lower().replace(" ", "-")
        parameters = {
            'slug': name,
            'convert': 'EUR'
        }
    else:
        parameters = {
            'convert': 'EUR'
        }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': config.COINMARKET_API_KEY
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        response = e

    return response
