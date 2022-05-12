from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from app.crypto_api import apikey
import requests

headers = {
    'X-CMC_PRO_API_KEY': apikey.key,
    'Accepts': 'application/json'
}

params = {
    'start': '1',
    'limit': '5',
    'convert': 'USD'
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json = requests.get(url, params=params, headers=headers).json()

coins = json['data']

for x in coins[0:1]:
    crypto_1 = '1', x['name'], x['symbol'], "{:,}".format(round(x['quote']['USD']['price'], 2)), \
               "{:,}".format(round(x['quote']['USD']['percent_change_24h'], 2)), \
             "{:,}".format(round(x['quote']['USD']['percent_change_7d'], 2)),\
               "{:,}".format(round(x['circulating_supply']), 0) + ' ' + x['symbol']

for x in coins[0:2]:
    crypto_2 = '2', x['name'], x['symbol'], "{:,}".format(round(x['quote']['USD']['price'], 2)), \
               "{:,}".format(round(x['quote']['USD']['percent_change_24h'], 2)), \
             "{:,}".format(round(x['quote']['USD']['percent_change_7d'], 2)), \
               "{:,}".format(round(x['circulating_supply']), 0) + ' ' + x['symbol']

for x in coins[0:3]:
    crypto_3 = '3', x['name'], x['symbol'], "{:,}".format(round(x['quote']['USD']['price'], 4)), \
               "{:,}".format(round(x['quote']['USD']['percent_change_24h'], 4)), \
             "{:,}".format(round(x['quote']['USD']['percent_change_7d'], 4)), \
               "{:,}".format(round(x['circulating_supply']), 0) + ' ' + x['symbol']

for x in coins[0:4]:
    crypto_4 = '4', x['name'], x['symbol'], "{:,}".format(round(x['quote']['USD']['price'], 4)), \
               "{:,}".format(round(x['quote']['USD']['percent_change_24h'], 4)), \
             "{:,}".format(round(x['quote']['USD']['percent_change_7d'], 4)), \
               "{:,}".format(round(x['circulating_supply']), 0) + ' ' + x['symbol']

for x in coins[0:5]:
    crypto_5 = '5', x['name'], x['symbol'], "{:,}".format(round(x['quote']['USD']['price'], 2)), \
               "{:,}".format(round(x['quote']['USD']['percent_change_24h'], 2)), \
             "{:,}".format(round(x['quote']['USD']['percent_change_7d'], 2)), \
               "{:,}".format(round(x['circulating_supply']), 0) + ' ' + x['symbol']

simple_pages = Blueprint('simple_pages', __name__,
                         template_folder='templates')

headings = ("#", "Name", "Symbol", "Price", "24h %", "7d %", "Circulating Supply")

data = (
    crypto_1,
    crypto_2,
    crypto_3,
    crypto_4,
    crypto_5,
)


@simple_pages.route('/')
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@simple_pages.route('/about')
def about():
    try:
        return render_template('about.html')
    except TemplateNotFound:
        abort(404)


@simple_pages.route('/welcome')
def welcome():
    try:
        return render_template('welcome.html')
    except TemplateNotFound:
        abort(404)


@simple_pages.route('/crypto')
def crypto():
    try:
        return render_template('crypto.html', headings=headings, data=data)
    except TemplateNotFound:
        abort(404)
