from cryptoapp.database import Crypto


def test_add_crypto_data(client):
    response = client.post('/add_data', data={
        'name': 'Bitcoin',
        'quantity': 4,
        'price': 12000
    })

    assert response.status_code == 302


def test_edit_crypto_data(client):
    data = client.post('/add_data', data={
        'name': 'Bitcoin',
        'quantity': 4,
        'price': 12000
    })

    response = client.post('/edit_data', data={
        'name': 'Bitcoin',
        'quantity': 2,
    })

    assert response.status_code == 302


def test_adding_random_data_to_database():
    c = Crypto('Crypto-Test', 'CRPT', 5, 1000, 1500, 6.5)
    assert c.name == 'Crypto-Test'
    assert c.symbol == 'CRPT'
    assert c.quantity == 5
    assert c.price == 1000
    assert c.value == 1500
    assert c.percent_change_24h == 6.5


