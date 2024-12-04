from flask import Blueprint, request
import controllers.users_controller as controller

users_bp = Blueprint('users', __name__)

@users_bp.route('/', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'GET':
        return controller.get_all_users()

    if request.method == 'POST':
        return controller.create_new_user()

@users_bp.route('/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_user(user_id):
    if request.method == 'GET':
        return controller.get_user(user_id)

    if request.method == 'PUT':
        return controller.update_user(user_id)

    if request.method == 'DELETE':
        return controller.delete_user(user_id)
