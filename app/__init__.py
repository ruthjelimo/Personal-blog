
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads,IMAGES
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_simplemde import SimpleMDE
import os


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

simple = SimpleMDE()

db = SQLAlchemy()
mail = Mail()
bootstrap = Bootstrap()
photos = UploadSet('photos',IMAGES)

def create_app(config_name):
    app = Flask(__name__)
    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    

    # Initializing flask extensions
    db.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    simple.init_app(app)


    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as main_blueprint
    app.register_blueprint(main_blueprint)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    return app

