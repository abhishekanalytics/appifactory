from flask_jwt_extended import create_access_token
from ..schema.schema import User
from .. import mongo
from bson import ObjectId
from pymongo.errors import DuplicateKeyError
from flask_login import logout_user
from werkzeug.security import generate_password_hash



def get_all_users():
    users = mongo.db.users.find()
    user_list = [
        {
            'username': user['username'],
            'email': user['email'],
            'firstname': user['firstname'],
            'lastname': user['lastname'],
            'mobileno': user['mobileno'],
        }
        for user in users
    ]
    return user_list
def create_user(username, email, firstname, lastname, mobileno,password,role):
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
        user=User(
            str(user_data['_id']),
            user_data['username'],
            user_data['email'], 
            user_data['firstname'],
            user_data['lastname'],
            user_data['mobileno']
            )
        return user.to_dict()
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
def login(email, password):
    user = authenticate_user(email, password)
    if user:
        access_token = create_access_token(identity=str(user.id))
        return {"message": "Login successful.", "access_token": access_token}
    else:
        return {"error": "Invalid user or password."}
def logout():
    logout_user()
    return {"message": "Logout successful."}









