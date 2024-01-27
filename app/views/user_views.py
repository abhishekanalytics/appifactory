from flask import Blueprint, jsonify, request
from ..db_services.user_service import get_all_users, create_user, get_user_by_id, update_user, delete_user
from ..route.tasks import user_blueprint

@user_blueprint.route('/123', methods=["GET", "POST"])
def manage_users():
    if request.method == "GET":
        users_list = get_all_users()
        return jsonify(users_list=users_list)
        
    elif request.method == "POST":
        try:
            print("views")
            data = request.get_json()
            print("bbbbc")    
            result = create_user(username=data['username'],email=data['email'],firstname=data['firstname'],lastname=data['lastname'],mobileno=data['mobileno'])
            return jsonify(result)
        except Exception as e:
            return jsonify(error=f"Error creating user: {e}")

@user_blueprint.route('/123/<string:user_id>', methods=["GET", "PUT", "DELETE"])
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
