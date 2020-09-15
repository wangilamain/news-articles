from flask import Flask
from  config import Config, config_options
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    # App configurations
    app.config.from_object(config_options[config_name])
    app.config.from_object(Config)

    #  initializing the app
    bootstrap.init_app(app)

    from .requests import configure
    configure(app)

    #registering blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint) 
    
    return app