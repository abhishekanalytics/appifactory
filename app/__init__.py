from flask import Flask
from flask_pymongo import PyMongo
from .config import Config
import os
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)
jwt = JWTManager(app)
mongo = PyMongo(app)
from .views.user_views import user_blueprint
from .views.tasks_views import tasks_blueprint
from app.static.load_views import login_manager  
app.register_blueprint(user_blueprint, url_prefix='/users')
app.register_blueprint(tasks_blueprint, url_prefix='/tasks')

