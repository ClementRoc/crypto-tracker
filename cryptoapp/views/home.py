from flask import Blueprint, render_template
from cryptoapp.database import Crypto, get_all_crypto
from cryptoapp.utils import scss_to_css, get_profit_total

mod = Blueprint('home', __name__)


@mod.route('/', methods=['GET', 'POST'])
def home():
    scss_to_css()
    return render_template(
        'home.html',
        title='Accueil - Crypto Tracker',
        profit=format(get_profit_total(), ',d'),
        crypto=Crypto.query.all()
    )


@mod.route('/add', methods=['GET', 'POST'])
def add():
    scss_to_css()
    return render_template(
        'add.html',
        title='Nouvelle transaction - Crypto Tracker',
        crypto_list=get_all_crypto()
    )


@mod.route('/edit', methods=['GET', 'POST'])
def edit():
    scss_to_css()
    return render_template(
        'edit.html',
        title='Modifier - Crypto Tracker',
        crypto=Crypto.query.all()
    )

