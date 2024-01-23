# from flask import Blueprint,jsonify        
# from .schema import User
# from . import mongo

# main_blueprint = Blueprint('main', __name__)

# @main_blueprint.route('/')
# def home():
#     return 'Hello, World!'

# @main_blueprint.route('/users')
# def get_users():
#     users = mongo.db.users.find()
#     user_list = [User(user['username'], user['email']).to_dict() for user in users]
#     return jsonify(users=user_list)

# your_app/routes.py



from flask import Blueprint, jsonify,request


main_blueprint = Blueprint('main', __name__)


