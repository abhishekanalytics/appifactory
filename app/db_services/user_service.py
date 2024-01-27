from ..schema.schema import User
from .. import mongo
from bson import ObjectId
from pymongo.errors import DuplicateKeyError

def get_all_users():
     
    users = mongo.db.users.find()
    user_list = [User(user['username'], user['email'],user['firstname'],user['lastname'],user['mobileno']).to_dict() for user in users]
    return user_list

def create_user(username, email,firstname,lastname,mobileno):
    try:
        print("in")
        new_user = User(username=username,email=email,firstname=firstname,lastname=lastname,mobileno=mobileno)
        new_user.save_to_db()
        print(new_user)
        return {"message": "user created successfully."}
    except Exception as e:
        return {"error": f"Error creating user: {'E11000 duplicate key error collection: userdata.users index: unique_email_index dup key'}"}

def get_user_by_id(user_id):
    user_data = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if user_data:
        return User(user_data['username'], user_data['email'],user_data['firstname'],user_data['lastname'],user_data['mobileno']).to_dict()
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
