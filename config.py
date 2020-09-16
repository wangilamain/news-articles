import os
class Config:
    ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/{}?&apiKey={}'
    BASE_URL = "https://newsapi.org/v2/{}?language=en&apiKey={}"
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True
config_options = {
    'development':DevConfig,
    'production':ProdConfig,
}