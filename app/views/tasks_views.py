from flask import Blueprint, jsonify, request
from ..db_services.tasks_service import get_all_tasks, create_task, get_task_by_id, update_task, delete_task
from ..route.tasks import tasks_blueprint
from flask_login import current_user
from flask_jwt_extended import jwt_required,get_jwt_identity


@tasks_blueprint.route('/alls', methods=["GET"])
@jwt_required()
def manage_tasks():
        current_user_id = get_jwt_identity()
        if current_user_id:
            tasks_list = get_all_tasks()
            return jsonify(tasks_list=tasks_list)

@tasks_blueprint.route('/creates', methods=["POST"])
@jwt_required()
def creats_tasks():
        try:
            data = request.get_json()           
            user_id = data.get('user_id')   

            result = create_task(title=data['title'], description=data['description'], user_id = current_user.id)
            return jsonify(result)
        except Exception as e:
            print(str(e))
            return jsonify(error="give data in JSON format in 'in raw'")

@tasks_blueprint.route('task/<string:task_id>', methods=["GET", "PUT", "DELETE"])
@jwt_required()
def manage_task(task_id):
    current_user_id = get_jwt_identity()
    if current_user_id:
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
