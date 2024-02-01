
from flask import Flask
from flask_pymongo import PyMongo
from .config import Config
import os
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager

load_dotenv()
app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'everything'
app.config['JWT_SECRET_KEY'] = os.getenv('nothing')
jwt = JWTManager(app)
mongo = PyMongo(app)
from .views.user_views import user_blueprint
from .views.tasks_views import tasks_blueprint
app.register_blueprint(user_blueprint, url_prefix='/users')
app.register_blueprint(tasks_blueprint, url_prefix='/tasks')

