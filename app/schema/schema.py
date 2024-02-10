from flask_login import UserMixin
from werkzeug.security import check_password_hash
from .. import mongo
from bson import ObjectId
from pymongo import IndexModel, ASCENDING

class User(UserMixin):
    def __init__(self, username, email, firstname, lastname, mobileno, password,role,user_id=None):
        self.id = str(user_id)
        self.username = username
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.mobileno = mobileno
        self.password = password
        self.role=role

    def check_password(self, pwd):
        return check_password_hash(self.password, pwd)

    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            "mobileno": self.mobileno,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "role":self.role
        }

    @staticmethod
    def create_indexes():
        collection = mongo.db.users
        indexes = [
            IndexModel([("email", ASCENDING)], unique=True),
            IndexModel([("username", ASCENDING)], unique=True),
        ]
        collection.create_indexes(indexes)

    def save_to_db(self):
        if not self.role in ["admin","maneger","employee"]:
            return {"message":"Invalid role"}

        collection = mongo.db.users
        user_data = {
            "username": self.username,
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "mobileno": self.mobileno,
            "password": self.password,
            "role":self.role
        }
        result = collection.insert_one(user_data)
        return {"message": "User created successfully."}

    def get(user_id):
        user_data = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        if user_data:
            return User(
                user_id=str(user_data['_id']),
                username=user_data['username'],
                email=user_data['email'],
                firstname=user_data['firstname'],
                lastname=user_data['lastname'],
                mobileno=user_data['mobileno'],
                password=user_data["password"],
                role=user_data['role']
                
            )
        return None

    @staticmethod
    def find_by_email(email):
        collection = mongo.db.users
        user_data = collection.find_one({"email": email})
        if user_data:
            return User(
                user_id=str(user_data['_id']),
                username=user_data['username'],
                email=user_data['email'],
                firstname=user_data['firstname'],
                lastname=user_data['lastname'],
                mobileno=user_data['mobileno'],
                password=user_data['password'],
                role=user_data['role']
            )
User.create_indexes()

class Task:
    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.user_id = user_id  

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'user_id': str(self.user_id)  
        }

    def save_to_db(self):
        print(ObjectId(self.user_id))
        collection = mongo.db.tasks
        task_data = {
            "title": self.title,
            "description": self.description,
            "user_id": ObjectId(self.user_id) 
        }
        result = collection.insert_one(task_data)
        return {"message": "Task created successfully."}