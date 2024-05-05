from flask_jwt_extended import get_jwt_identity
from flask import jsonify
from functools import wraps
from app.schema.schema import User

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        current_user_id = get_jwt_identity()
        current_user = User.get(current_user_id)
        if current_user.role =="admin":
            return f(*args, **kwargs)
        else:
            return jsonify(error="Unauthorized")
    return decorated_function


def manager_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        current_user_id = get_jwt_identity()
        current_user = User.get(current_user_id)
        if current_user.role == "manager" or current_user.role == "admin": 
            return f(*args, **kwargs)
        else:
            return jsonify(error="Unauthorized")
    return decorated_function


def employee_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        current_user_id = get_jwt_identity()
        current_user = User.get(current_user_id)
        if current_user.role == "employee"or current_user.role == "admin":
            return f(*args, **kwargs)
        else:
            return jsonify(error="Unauthorized")
    return decorated_function
