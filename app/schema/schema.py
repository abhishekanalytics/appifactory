from flask_pymongo import ObjectId
from .. import mongo

class User:
    
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def to_dict(self):
        return {'username': self.username, 'email': self.email}
    def save_to_db(self):
        try:                             
        # Access MongoDB using mongo object
            collection = mongo.db.users
            user_data = {
                "username": self.username,
                "email": self.email
            }
            result = collection.insert_one(user_data)
            return str(result.inserted_id)
        except Exception as e:
            print(f"Error saving to the database: {e}")
            return None
        
class Task:
    
    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description

    def to_dict(self):
        return {'task_id': str(self.task_id), 'title': self.title, 'description': self.description}

    def save_to_db(self):
        try:
            # Access MongoDB using mongo object
            collection = mongo.db.tasks
            task_data = {
                "title": self.title,
                "description": self.description
            }
            result = collection.insert_one(task_data)
            self.task_id = result.inserted_id  # Update task_id after insertion
            return str(self.task_id)
        except Exception as e:
            print(f"Error saving to the database: {e}")
            return None
