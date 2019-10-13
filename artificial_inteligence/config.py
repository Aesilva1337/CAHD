from os import getenv

DATA_BACKEND = 'mongodb'
MONGO_URI = 'mongodb://cahd:cahd@34.94.128.254:27017/CAHD'


class Config:
    APP_PORT = int(getenv('APP_PORT'))
    DEBUG = eval(getenv('DEBUG').title())
    MONGODB_HOST = getenv('MONGODB_URI', MONGO_URI)


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
