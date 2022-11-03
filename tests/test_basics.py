import unittest
from flask import current_app
from cryptoapp import app


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

