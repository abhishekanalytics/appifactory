from .. import mongo
import json
from pymongo.errors import DuplicateKeyError

class User:
    def __init__(self,username,email,firstname,lastname,mobileno):
        self.username=username
        self.email=email
        self.firstname=firstname
        self.lastname=lastname
        self.mobileno=mobileno
    def to_dict(self):
        return {'username': self.username, 'email': self.email}
    
    def save_to_db(self):                         
        # Here I am Accessing MongoDB using mongo object
            collection = mongo.db.users
            user_data = {
                "username": self.username,
                "email":self.email,
                "firstname": self.firstname,
                "lastname": self.lastname,
                "mobileno": self.mobileno
            }
            result = collection.insert_one(user_data)

class Task:
    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description

    def to_dict(self):
        return {'task_id': str(self.task_id), 'title': self.title, 'description': self.description}
    def save_to_db(self):
        try:
            # Here I am Accessing  MongoDB using mongo object
            collection = mongo.db.tasks
            task_data = {
                "title": self.title,
                "description": self.description
            }
            result = collection.insert_one(task_data)
            self.task_id = result.inserted_id  
            return str(self.task_id)
        except Exception as e:
            return("Error saving to the database :{e}")
