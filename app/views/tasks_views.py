from flask import Blueprint, jsonify, request
from ..db_services.tasks_service import get_all_tasks, create_task, get_task_by_id, update_task, delete_task,get_user_tasks
from ..route.tasks import tasks_blueprint
from flask_login import current_user


@tasks_blueprint.route('/api', methods=["GET", "POST"])
def manage_tasks():
    if request.method == "GET":
        tasks_list = get_all_tasks()
        return jsonify(tasks_list=tasks_list)
    elif request.method == "POST":        
        try:          
            data = request.get_json()           
            user_id = data.get('user_id')          
            result = create_task(title=data['title'], description=data['description'], user_id = current_user.id)
            return jsonify(result)
        except Exception as e:
            print(str(e))
            return jsonify(error="give data in JSON format in 'in raw'")

@tasks_blueprint.route('/api/<string:task_id>', methods=["GET", "PUT", "DELETE"])
def manage_task(task_id):
    if request.method == "GET":
        task = get_task_by_id(task_id)
        if task:
            return jsonify(task=task)
        else:
            return jsonify(error=f"No task found with id {task_id}.")

    elif request.method == "PUT":
        try:
            data = request.get_json()
            result = update_task(task_id, description=data.get('description'))
            return jsonify(result)
        except Exception as e:
            return jsonify(error=f"Error updating task: {e}")
        
    elif request.method == "DELETE":
        result = delete_task(task_id)
        return jsonify(result)

@tasks_blueprint.route('/api/user/<string:user_id>/tasks', methods=["GET"])
def get_user_tasks_endpoint(user_id):
    tasks_list = get_user_tasks(user_id)
    print(tasks_list)
    return jsonify(tasks_list=tasks_list)
