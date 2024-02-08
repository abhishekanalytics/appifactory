from flask import Blueprint, jsonify, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from ..db_services.user_service import get_all_users, create_user, get_user_by_id, update_user, delete_user, authenticate_user,get_user_tasks
from ..route.tasks import user_blueprint
from flask_jwt_extended import create_access_token

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
@login_required
def logout():
    logout_user()
    flash('Logout successful', 'success')
    return jsonify(message='Logout successful')

@user_blueprint.route('/apis', methods=["GET", "POST"])
def manage_users():
    if request.method == "GET":
        users_list = get_all_users()
        return jsonify(users_list=users_list)
    elif request.method == "POST":
        try:
            data = request.get_json()
            result = create_user(
                username=data['username'],
                email=data['email'],
                password=data['password'],  
                firstname=data['firstname'],
                lastname=data['lastname'],
                mobileno=data['mobileno']
            )
            return jsonify(result)
        except Exception as e:
            return jsonify(error=f"Error creating user: {e}")

@user_blueprint.route('/apis/<string:user_id>', methods=["GET", "PUT", "DELETE"])
def manage_user(user_id):
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

