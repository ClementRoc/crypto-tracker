from flask_testing import TestCase

from cryptoapp import app
from cryptoapp.database import db, Crypto


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('config')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Crypto('Crypto-Test', 'CRPT', 5, 1000, 1200, 6.5))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

