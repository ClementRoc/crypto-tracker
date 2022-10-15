import os

_basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')

# COINMARKET CONFIG
# PRO
COINMARKET_API_KEY = '816e3ecc-02a3-4ea4-8e0f-5e1bfdf6a172'
COINMARKET_API_QUOTES_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
COINMARKET_API_LISTING_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# DEV
# COINMARKET_DEV_API_KEY = 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c'
# COINMARKET_DEV_API_URL = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

del os