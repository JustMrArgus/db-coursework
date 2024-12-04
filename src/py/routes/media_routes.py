from flask import Blueprint, request
import controllers.media_controller as controller

media_bp = Blueprint('media', __name__)

@media_bp.route('/', methods=['GET', 'POST'])
def handle_media():
    if request.method == 'GET':
        return controller.get_all_media()

    if request.method == 'POST':
        return controller.create_media()

@media_bp.route('/<int:media_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_media_item(media_id):
    if request.method == 'GET':
        return controller.get_media(media_id)

    if request.method == 'PUT':
        return controller.update_media(media_id)

    if request.method == 'DELETE':
        return controller.delete_media(media_id)