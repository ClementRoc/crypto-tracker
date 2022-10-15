
from base import BaseTestCase
from cryptoapp.database import Crypto


class ModelTest(BaseTestCase):
    c = Crypto('Crypto-Test', 'CRPT', 5, 1000, 1500, 6.5)
    assert c.name == 'Crypto-Test'
    assert c.symbol == 'CRPT'
    assert c.quantity == 5
    assert c.price == 1000
    assert c.value == 1500
    assert c.percent_change_24h == 6.5

