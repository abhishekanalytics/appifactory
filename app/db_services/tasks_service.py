from bson import ObjectId
from ..schema.schema import Task
from .. import mongo

def get_all_tasks():
    tasks = mongo.db.tasks.find()
    task_list = [
        {
            'title': task['title'],
            'description': task['description'],
            'user_id': str(task['user_id']),
            '_id':str(task['_id']),
        }
        for task in tasks
    ]
    return task_list

def create_task(title, description, user_id):
    print(user_id)
    try:
        new_task = Task(title=title, description=description, user_id=user_id)
        new_task.save_to_db()
        return {"message": "Task created successfully."}
    except Exception as e:
        return {"error": f"Error creating task: {e}"}

def get_task_by_id(task_id):
    task_data = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    if task_data:
        task = Task(
            title=task_data['title'],
            description=task_data['description'],
            user_id=str(task_data['user_id'])
        )
        return task.to_dict()
    else:
        return None

def update_task(task_id, description):
    try:
        updated_data = {"$set": {"description": description}}
        result = mongo.db.tasks.update_one({"_id": ObjectId(task_id)}, updated_data)
        if result.modified_count > 0:
            return {"message": f"Task with id {task_id} updated successfully."}
        else:
            return {"message": f"No task found with id {task_id}."}
    except Exception as e:
        return {"error": f"Error updating task: {e}"}

def delete_task(task_id):
    try:
        result = mongo.db.tasks.delete_one({"_id": ObjectId(task_id)})
        if result.deleted_count > 0:
            return {"message": f"Task with id {task_id} deleted."}
        else:
            return {"message": f"No task found with id {task_id}."}
    except Exception as e:
        return {"error": f"Error deleting task: {e}"}
    

def get_user_tasks(user_id):
    tasks_data = mongo.db.tasks.find({"user_id": ObjectId(user_id)})
    tasks = [
        {
            'task_id': str(task['_id']),
            'title': task['title'],
            'description': task['description']
        }
        for task in tasks_data
    ]
    return tasks