def test_home(client):
    response = client.get('/home')
    assert response.status_code == 200


def test_add(client):
    response = client.get('/add')
    assert response.status_code == 200


def test_edit(client):
    response = client.get('/edit')
    assert response.status_code == 200


def test_profit(client):
    response = client.get('/profit')
    assert response.status_code == 200


def test_add_data_redirect(client):
    response = client.post('/add_data', data={
        'name': 'Bitcoin',
        'quantity': 4,
        'price': 12000
    })

    assert response.status_code == 302


def test_edit_data_redirect(client):
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

