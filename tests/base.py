from flask_testing import TestCase

from cryptoapp import app


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('config')
        return app


