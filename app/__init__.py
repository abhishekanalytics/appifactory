from flask import Flask
from flask_pymongo import PyMongo
from .config import Config
import os
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
# from .views.auth import auth_blueprint



load_dotenv()
app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'everything'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
jwt = JWTManager(app)
mongo = PyMongo(app)
login_manager = LoginManager(app)
from .views.user_views import user_blueprint
from .views.tasks_views import tasks_blueprint
from app.static.load_views import login_manager  

@login_manager.user_loader
def load_user(user_id):
    from app.schema.schema import User
    return User.get(user_id)
login_manager.login_view = 'user.login'

app.register_blueprint(user_blueprint, url_prefix='/users')
app.register_blueprint(tasks_blueprint, url_prefix='/tasks')
# app.register_blueprint(auth_blueprint, url_prefix='/auth')

