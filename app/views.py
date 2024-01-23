from flask import Blueprint, render_template      
from .schema import User
from . import mongo

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/users')
def get_users():
    users = mongo.db.users.find()
    user_list = [User(user['username'], user['email']).to_dict() for user in users]
    return render_template('users.html', users=user_list)
