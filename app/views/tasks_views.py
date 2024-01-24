from flask import Blueprint, jsonify, request
from ..db_services.tasks_service import get_all_tasks, create_task, get_task_by_id, update_task, delete_task
from ..route.tasks import tasks_blueprint

@tasks_blueprint.route('/api', methods=["GET", "POST"])
def manage_tasks():
    if request.method == "GET":
        tasks_list = get_all_tasks()
        return jsonify(tasks_list=tasks_list)
    elif request.method == "POST":
        try:
            data = request.get_json()
            result = create_task(title=data['title'], description=data['description'])
            return jsonify(result)
        except Exception as e:
            return jsonify(error=f"Error creating task: {e}")

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
