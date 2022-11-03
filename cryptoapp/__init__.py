from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')


@app.errorhandler(404)
def not_found(e):
    return render_template(
        'error/404.html',
        error=e
    )


@app.errorhandler(500)
def internal_error(e):
    return render_template(
        'error/500.html',
        error=e
    )


from cryptoapp.views import home
from cryptoapp.views import profit

app.register_blueprint(home.mod)
app.register_blueprint(profit.mod)


from cryptoapp.database import Crypto, init_db

init_db()
