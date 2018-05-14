import os
class Config:
    # BASE_URL = "https://newsapi.org/v2/sources?country=us&category={}&apiKey={}"
    NEWS_API_KEY=os.environ.get("NEWS_API_KEY")
    NEWS_SOURCES_URL = 'https://newsapi.org/v2/sources?category={}&language=en&apiKey={}'

    NEWS_ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?source={}&language=en&apiKey={}'



class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
    'development': DevConfig ,
    'production': ProdConfig
}
