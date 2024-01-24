from ..schema.schema import User
from .. import mongo
from bson import ObjectId

def get_all_users():
     

    users = mongo.db.users.find()
    user_list = [User(user['username'], user['email']).to_dict() for user in users]
    return user_list

def create_user(username, email):
    try:
        new_user = User(username=username, email=email)
        new_user.save_to_db()
        return {"message": "User created successfully."}
    except Exception as e:
        return {"error": f"Error creating user: {e}"}

def get_user_by_id(user_id):
    user_data = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if user_data:
        return User(user_data['username'], user_data['email']).to_dict()
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
