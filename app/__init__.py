from flask import Flask
from flask_pymongo import PyMongo
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

mongo = PyMongo(app)

from .views.tasks_views import tasks_blueprint
app.register_blueprint(tasks_blueprint, url_prefix='/tasks')


