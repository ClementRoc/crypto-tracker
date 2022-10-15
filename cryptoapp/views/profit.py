from flask import Blueprint, render_template
from cryptoapp.database import Crypto
from cryptoapp.utils import scss_to_css, get_graph, get_value_total

mod = Blueprint('profit', __name__)


@mod.route('/profit', methods=['GET', 'POST'])
def profit():
    scss_to_css()
    return render_template(
        'profit.html',
        title='Profit total - Crypto Tracker',
        crypto=Crypto.query.all(),
        value=format(get_value_total(), ',d'),
        graph=get_graph()
        )
