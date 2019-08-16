from flask import Flask
from config import config


def create_app(config_name):
    app = Flask('api-CAHD')

    app.config.from_object(config[config_name])

    return app