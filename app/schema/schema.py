
from flask_login import UserMixin
from werkzeug.security import check_password_hash
from .. import mongo
from bson import ObjectId
from .. import app
from flask_login import LoginManager
from pymongo import IndexModel, ASCENDING

class User(UserMixin):
    def __init__(self, username, email, firstname, lastname, mobileno ,password,user_id=None):
        
        self.id = str(user_id)
        self.username = username
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.mobileno = mobileno
        self.password=password
    
    def check_password(self, pwd):
        return check_password_hash(self.password, pwd)

    def to_dict(self):
        return {'username': self.username, 'email': self.email,"mobileno":self.mobileno,"firstname":self.firstname,"lastname":self.lastname}
    
    @staticmethod
    def create_indexes():
        collection = mongo.db.users
        indexes = [
            
            IndexModel([("email", ASCENDING)], unique=True),
            IndexModel([("username", ASCENDING)], unique=True),
        ]
        collection.create_indexes(indexes)

    def save_to_db(self):
        collection = mongo.db.users
        
        user_data = {
            "username": self.username,
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "mobileno": self.mobileno,
            "password":self.password,
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
                password=user_data["password"]
                 
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
                password=user_data['password'] 
            )
        return None

    login_manager = LoginManager(app)
    @login_manager.user_loader
    def load_user(user_id):
        return User.load_user(user_id)
    login_manager.login_view = 'user.login'

    @staticmethod
    def load_user(user_id):
        return User.get(user_id)
User.create_indexes()


class Task:
    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description

    def to_dict(self):
        return {'task_id': str(self.task_id), 'title': self.title, 'description': self.description}
    def save_to_db(self):
            collection = mongo.db.tasks
            task_data = {
                
                "task_id":self.task_id,
                "description": self.description
            }