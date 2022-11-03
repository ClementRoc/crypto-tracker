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
