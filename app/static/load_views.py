from flask_login import LoginManager
from app.schema.schema import User
from .. import app

login_manager = LoginManager(app)
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)