from bson import ObjectId
from ..schema.schema import Task
from .. import mongo

def get_all_tasks():
    tasks = mongo.db.tasks.find()
    task_list = [Task(str(task['_id']), task['title'], task['description']).to_dict() for task in tasks]
    return task_list

def create_task(title, description):
    try:
        new_task = Task(task_id=None, title=title, description=description)
        new_task.save_to_db()
        return {"message": "Task created successfully."}
    except Exception as e:
        return {"error": f"Error creating task: {e}"}

def get_task_by_id(task_id):
    task_data = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    if task_data:
        return Task(str(task_data['_id']), task_data['title'], task_data['description']).to_dict()
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
