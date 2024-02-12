from bson import ObjectId
from pymongo.errors import DuplicateKeyError
from werkzeug.security import generate_password_hash
from ..schema.schema import User
from .. import mongo
from ..db_services.tasks_service import get_user_tasks

def get_all_users():
    users = mongo.db.users.find()
    user_list = [
        {    'role': user['role'],
            'username': user['username'],
            'email': user['email'],
            'firstname': user['firstname'],
            'lastname': user['lastname'],
            'mobileno': user['mobileno'],
            '_id':str(user['_id']),
            'tasks': get_user_tasks(str(user['_id']))
        }
        for user in users
    ]
    return user_list

def create_user(username, email, firstname, lastname, mobileno, password,role):
    try:
        hash_pwd = generate_password_hash(password)
        new_user = User(
            username=username,
            email=email,
            firstname=firstname,
            lastname=lastname,
            mobileno=mobileno,
            password=hash_pwd,
            role=role
        )
        new_user.save_to_db()
        return {"message": "user created successfully."}
    except DuplicateKeyError:
        return {"error": "username or email already exists"}

def get_user_by_id(user_id):
    user_data = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if user_data:
        user = User(
            str(user_data['_id']),
            user_data['username'],
            user_data['email'],
            user_data['firstname'],
            user_data['lastname'],
            user_data['mobileno'],
            user_data['role']

        )
        user_dict = user.to_dict()
        user_dict['tasks'] = get_user_tasks(user_id)
        return user_dict
    else:
        return None

def update_user(user_id, email):
    try:
        updated_data = {"$set": {"email": email}}
        result = mongo.db.users.update_one({"_id": ObjectId(user_id)}, updated_data)
        if result.modified_count > 0:
            return {"message": f"User with id {user_id} updated successfully."}
        else:
            return {"message": f"No user found with id {user_id}."}
    except Exception as e:
        return {"error": f"Error updating user: {e}"}

def delete_user(user_id):
    try:
        result = mongo.db.users.delete_one({"_id": ObjectId(user_id)})
        if result.deleted_count > 0:
            return {"message": f"User with id {user_id} deleted."}
        else:
            return {"message": f"No user found with id {user_id}."}
    except Exception as e:
        return {"error": f"Error deleting user: {e}"}

def authenticate_user(email, password):
    user = User.find_by_email(email)
    if user and user.check_password(password):
        return user
    return None



