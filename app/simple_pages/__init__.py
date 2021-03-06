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
    'limit': '10',
    'convert': 'USD'
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json = requests.get(url, params=params, headers=headers).json()

coins = json['data']

for x in coins[0:1]:

    crypto_1_num = '1',

    crypto_1_index = x['name'], x['symbol'], '$' + "{:,}".format(round(x['quote']['USD']['price'], 2)),

    crypto_1_rest = "{:,}".format(round(x['quote']['USD']['percent_change_24h'], 2)), \
                    "{:,}".format(round(x['quote']['USD']['percent_change_7d'], 2)),\
                    "{:,}".format(round(x['circulating_supply']), 0) + ' ' + x['symbol'],

    crypto_1 = crypto_1_num + crypto_1_index + crypto_1_rest

for x in coins[0:2]:

    crypto_2_num = '2',

    crypto_2_index = x['name'], x['symbol'], '$' + "{:,}".format(round(x['quote']['USD']['price'], 2)),

    crypto_2_rest = "{:,}".format(round(x['quote']['USD']['percent_change_24h'], 2)), \
                    "{:,}".format(round(x['quote']['USD']['percent_change_7d'], 2)), \
                    "{:,}".format(round(x['circulating_supply']), 0) + ' ' + x['symbol'],

    crypto_2 = crypto_2_num + crypto_2_index + crypto_2_rest

for x in coins[0:3]:

    crypto_3_num = '3',

    crypto_3_index = x['name'], x['symbol'], '$' + "{:,}".format(round(x['quote']['USD']['price'], 4)),

    crypto_3_rest = "{:,}".format(round(x['quote']['USD']['percent_change_24h'], 4)), \
                    "{:,}".format(round(x['quote']['USD']['percent_change_7d'], 4)), \
                    "{:,}".format(round(x['circulating_supply']), 0) + ' ' + x['symbol'],

    crypto_3 = crypto_3_num + crypto_3_index + crypto_3_rest

for x in coins[0:4]:

    crypto_4_num = '4',

    crypto_4_index = x['name'], x['symbol'], '$' + "{:,}".format(round(x['quote']['USD']['price'], 4))

    crypto_4_rest = "{:,}".format(round(x['quote']['USD']['percent_change_24h'], 4)), \
                    "{:,}".format(round(x['quote']['USD']['percent_change_7d'], 4)), \
                    "{:,}".format(round(x['circulating_supply']), 0) + ' ' + x['symbol']

    crypto_4 = crypto_4_num + crypto_4_index + crypto_4_rest

for x in coins[0:5]:

    crypto_5_num = '5',

    crypto_5_index = x['name'], x['symbol'], '$' + "{:,}".format(round(x['quote']['USD']['price'], 2)),

    crypto_5_rest = "{:,}".format(round(x['quote']['USD']['percent_change_24h'], 2)), \
                    "{:,}".format(round(x['quote']['USD']['percent_change_7d'], 2)), \
                    "{:,}".format(round(x['circulating_supply']), 0) + ' ' + x['symbol']

    crypto_5 = crypto_5_num + crypto_5_index + crypto_5_rest

for x in coins[0:6]:

    crypto_6_num = '6',

    crypto_6_index = x['name'], x['symbol'], '$' + "{:,}".format(round(x['quote']['USD']['price'], 4))

    crypto_6_rest = "{:,}".format(round(x['quote']['USD']['percent_change_24h'], 4)), \
                    "{:,}".format(round(x['quote']['USD']['percent_change_7d'], 4)), \
                    "{:,}".format(round(x['circulating_supply']), 0) + ' ' + x['symbol']

    crypto_6 = crypto_6_num + crypto_6_index + crypto_6_rest

for x in coins[0:7]:

    crypto_7_num = '7',

    crypto_7_index = x['name'], x['symbol'], '$' + "{:,}".format(round(x['quote']['USD']['price'], 4))

    crypto_7_rest = "{:,}".format(round(x['quote']['USD']['percent_change_24h'], 4)), \
                    "{:,}".format(round(x['quote']['USD']['percent_change_7d'], 4)), \
                    "{:,}".format(round(x['circulating_supply']), 0) + ' ' + x['symbol']

    crypto_7 = crypto_7_num + crypto_7_index + crypto_7_rest

for x in coins[0:8]:

    crypto_8_num = '8',

    crypto_8_index = x['name'], x['symbol'], '$' + "{:,}".format(round(x['quote']['USD']['price'], 4))

    crypto_8_rest = "{:,}".format(round(x['quote']['USD']['percent_change_24h'], 4)), \
                    "{:,}".format(round(x['quote']['USD']['percent_change_7d'], 4)), \
                    "{:,}".format(round(x['circulating_supply']), 0) + ' ' + x['symbol']

    crypto_8 = crypto_8_num + crypto_8_index + crypto_8_rest


for x in coins[0:9]:

    crypto_9_num = '9',

    crypto_9_index = x['name'], x['symbol'], '$' + "{:,}".format(round(x['quote']['USD']['price'], 4))

    crypto_9_rest = "{:,}".format(round(x['quote']['USD']['percent_change_24h'], 4)), \
                    "{:,}".format(round(x['quote']['USD']['percent_change_7d'], 4)), \
                    "{:,}".format(round(x['circulating_supply']), 0) + ' ' + x['symbol']

    crypto_9 = crypto_9_num + crypto_9_index + crypto_9_rest

for x in coins[0:10]:

    crypto_10_num = '10',

    crypto_10_index = x['name'], x['symbol'], '$' + "{:,}".format(round(x['quote']['USD']['price'], 4))

    crypto_10_rest = "{:,}".format(round(x['quote']['USD']['percent_change_24h'], 4)), \
                    "{:,}".format(round(x['quote']['USD']['percent_change_7d'], 4)), \
                    "{:,}".format(round(x['circulating_supply']), 0) + ' ' + x['symbol']

    crypto_10 = crypto_10_num + crypto_10_index + crypto_10_rest


simple_pages = Blueprint('simple_pages', __name__,
                         template_folder='templates')

headings = ("#", "Name", "Symbol", "Price", "24h %", "7d %", "Circulating Supply")

data = (
    crypto_1,
    crypto_2,
    crypto_3,
    crypto_4,
    crypto_5,
    crypto_6,
    crypto_7,
    crypto_8,
    crypto_9,
    crypto_10,
)

headings_index = ("Name", "Symbol", "Price")

data_index = (
    crypto_1_index,
    crypto_2_index,
    crypto_3_index,
    crypto_4_index,
    crypto_5_index,
)


@simple_pages.route('/')
def index():
    try:
        return render_template('index.html', headings=headings_index, data=data_index)
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
