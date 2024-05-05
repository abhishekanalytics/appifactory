import os
from dotenv import load_dotenv
from flask import Flask
from .config import Config
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
load_dotenv()
app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

jwt = JWTManager(app)
mongo = PyMongo(app)
from .views.user_views import user_blueprint
from .views.tasks_views import tasks_blueprint
from app.static.load_views import login_manager  
app.register_blueprint(user_blueprint, url_prefix='/users')
app.register_blueprint(tasks_blueprint, url_prefix='/tasks')