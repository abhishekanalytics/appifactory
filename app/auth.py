from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from app.schema.schema import User

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        current_user_id = get_jwt_identity()
        current_user = User.get(current_user_id)
        print("mmmmmmmmmmmmmmmmmmmmmmmmmmmm",current_user)
        print("sirji.......................",current_user.role)
        if current_user.role == "admin":
            print("excellence.......................",current_user.role)

            return f(*args, **kwargs)
        else:
            return jsonify(error="Unauthorized")
    return decorated_function

def manager_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        current_user_id = get_jwt_identity()
        current_user = User.get(current_user_id)
        print("bbbbbbbbbbbbbbbbbbbbbbbb",current_user.role)
        print("ccccccccccccc",current_user)
        if current_user.role == "manager":
            print("qqqqqqqqqqqqqqqqqqqqq",current_user.role)
            print("qqqqqqqqqqqqqqqqqqqqq",current_user.id)
            return f(*args, **kwargs)
        else:
            return jsonify(error="Unauthorized")
    return decorated_function


def empolyee_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        current_user_id = get_jwt_identity()
        current_user = User.get(current_user_id)
        print("bbbbbbbbbbbbbbbbbbbbbbbb",current_user.role)
        if current_user.role == "manager":
            print("qqqqqqqqqqqqqqqqqqqqq",current_user.role)
            return f(*args, **kwargs)
        else:
            return jsonify(error="Unauthorized")
    return decorated_function