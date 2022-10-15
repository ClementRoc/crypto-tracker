import sass
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib

from cryptoapp.database import Crypto, get_crypto_data
from flask import url_for

matplotlib.use('Agg')

"""
Compile all the .scss files into .css files
"""


def scss_to_css():
    # Compile the fonts.scss file into a fonts.css file
    compiled_fonts_from_file = sass.compile(filename='cryptoapp/static/scss/fonts.scss', output_style='compressed')
    write_file = open('cryptoapp/static/fonts.css', 'w', encoding="utf-8")
    write_file.write(compiled_fonts_from_file)

    # Get all scss files in static/scss and compile them into one css file
    compiled_css_from_file = sass.compile(filename='cryptoapp/static/scss/app.scss', output_style='compressed')
    write_file = open('cryptoapp/static/app.css', 'w', encoding="utf-8")
    write_file.write(compiled_css_from_file)


"""
Calculate the total profit 

'market': False for calculating the profit based on the value when you bought it
          True for calculating the profit based on the market value right now
"""


def get_profit_total(profit=0):
    total_crypto_owned = Crypto.query.all()

    for data in total_crypto_owned:

        crypto = get_crypto_data(data.name)
        market_value = crypto['value'] * data.quantity

        if data.quantity > 0:
            profit += round(market_value - data.price)
        else:
            profit = 0

    return profit


"""
Calculate the total value of the cryptos
"""


def get_value_total(value=0):
    total_crypto_owned = Crypto.query.all()

    for data in total_crypto_owned:

        crypto = get_crypto_data(data.name)
        market_value = crypto['value'] * data.quantity

        if data.quantity > 0:
            value += round(market_value)
        else:
            value = 0

    return value


"""
Get the graph with Matplotlib, this graph defines the value of each cryptos owned

X-axis : Crypto's Name
Y-axis : Crypto's Total value
"""


def get_graph():
    url = url_for('static', filename='img/pages/profit/plot.png')
    crypto = Crypto.query.all()

    timeseries_crypto = {
        'Crypto': [],
        'Value': []
    }

    for data in crypto:
        crypto_data = get_crypto_data(data.name)
        market_value = crypto_data['value'] * data.quantity
        timeseries_crypto['Crypto'].append(data.name[0:7])
        timeseries_crypto['Value'].append(round(market_value))

    fig, ax = plt.subplots(squeeze=True)
    ax.barh(timeseries_crypto['Crypto'], timeseries_crypto['Value'], color='green', edgecolor='white')

    fmt = '€{x:,.0f}'
    tick = mtick.StrMethodFormatter(fmt)
    ax.xaxis.set_major_formatter(tick)

    ax.bar_label(ax.containers[0], color='white', fontsize='xx-large')

    ax.tick_params(color='white', labelcolor='white')
    for spine in ax.spines.values():
        spine.set_edgecolor('none')

    plt.savefig('cryptoapp' + url, transparent=True)

    plot_url = url

    return plot_url
