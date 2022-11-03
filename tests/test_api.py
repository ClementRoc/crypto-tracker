from requests import Session

import config


def test_api_response():
    url = config.COINMARKET_API_LISTING_URL
    parameters = {
        'convert': 'EUR'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': config.COINMARKET_API_KEY
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)

    assert response.status_code == 200
