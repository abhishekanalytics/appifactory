
from flask import Flask
from flask_pymongo import PyMongo
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)
app.config['SECRET_KEY'] = 'hello'
from .views.user_views import user_blueprint
from .views.tasks_views import tasks_blueprint
app.register_blueprint(user_blueprint, url_prefix='/users')
app.register_blueprint(tasks_blueprint, url_prefix='/tasks')

