from flask import Blueprint, request
import controllers.roles_controller as controller

roles_bp = Blueprint('roles', __name__)

@roles_bp.route('/', methods=['GET', 'POST'])
def handle_roles():
    if request.method == 'GET':
        return controller.get_all_roles()

    if request.method == 'POST':
        return controller.create_role()

@roles_bp.route('/<int:role_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_role(role_id):
    if request.method == 'GET':
        return controller.get_role(role_id)

    if request.method == 'PUT':
        return controller.update_role(role_id)

    if request.method == 'DELETE':
        return controller.delete_role(role_id)