from flask import Blueprint, jsonify, request
from flask_login import login_user, logout_user,current_user
from flask_jwt_extended import create_access_token,jwt_required,get_jwt_identity
from ..db_services.user_service import get_all_users, create_user, get_user_by_id, update_user, delete_user, authenticate_user
from ..route.tasks import user_blueprint
from app.decorators import admin_required,manager_required,employee_required

@user_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')  
    user = authenticate_user(email, password)
    if user:
        login_user(user)
        access_token = create_access_token(identity=str(user.id))
        return jsonify(message='Login successful', access_token=access_token)
    else:
        return jsonify(error='Invalid email or password')
    

@user_blueprint.route('/logout')
@admin_required
@jwt_required()
def logout():
    logout_user()
    return jsonify(message='Logout successful')


@user_blueprint.route('/all', methods=["GET"])
@jwt_required()
def manage_users():
        current_user_id = get_jwt_identity()
        users_list = get_all_users()
        return jsonify(users_list=users_list)


@user_blueprint.route('/create', methods=["POST"])
def create_users():
        try:
            data = request.get_json()
            result = create_user(
                username=data['username'],
                email=data['email'],
                password=data['password'],  
                firstname=data['firstname'],
                lastname=data['lastname'],
                mobileno=data['mobileno'],
                role=data['role']
            )
            return jsonify(result)
        except Exception as e:
            return jsonify(error=f"Error creating user: {e}")
        

@user_blueprint.route('user/<string:user_id>', methods=["GET", "PUT", "DELETE"])
@jwt_required()
@admin_required
def manage_user(user_id):
    current_user_id = get_jwt_identity()
    if current_user_id:
        if request.method == "GET":

            user = get_user_by_id(user_id)
            if user:
                return jsonify(user=user)
            else:
                return jsonify(error=f"No user found with id {user_id}.")
        elif request.method == "PUT":
            try:
                data = request.get_json()
                result = update_user(user_id, email=data.get('email'))
                return jsonify(result)
            except Exception as e:
                return jsonify(error=f"Error updating user: {e}")
        elif request.method == "DELETE":
            result = delete_user(user_id)
            return jsonify(result)
