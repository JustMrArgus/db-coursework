from models import Media
from extensions import db
from sqlalchemy.exc import IntegrityError
from flask import jsonify, request

def get_all_media():
    media_items = Media.query.all()
    return jsonify([{
        'id': media.id,
        'title': media.title,
        'keywords': media.keywords,
        'createdAt': media.createdAt.isoformat(),
        'updatedAt': media.updatedAt.isoformat(),
        'userId': media.userId
    } for media in media_items])

def create_media():
    data = request.json
    try:
        new_media = Media(
            title=data['title'],
            keywords=data['keywords'],
            createdAt=data['createdAt'],
            updatedAt=data['updatedAt'],
            userId=data['userId']
        )
        db.session.add(new_media)
        db.session.commit()
        return jsonify({'message': 'Media item created successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Invalid data or user does not exist'}), 400

def get_media(media_id):
    media = Media.query.get(media_id)
    if not media:
        return jsonify({'error': 'Media item not found'}), 404
    return jsonify({
        'id': media.id,
        'title': media.title,
        'keywords': media.keywords,
        'createdAt': media.createdAt.isoformat(),
        'updatedAt': media.updatedAt.isoformat(),
        'userId': media.userId
    })

def update_media(media_id):
    media = Media.query.get(media_id)
    if not media:
        return jsonify({'error': 'Media item not found'}), 404
    data = request.json
    media.title = data.get('title', media.title)
    media.keywords = data.get('keywords', media.keywords)
    media.createdAt = data.get('createdAt', media.createdAt)
    media.updatedAt = data.get('updatedAt', media.updatedAt)
    media.userId = data.get('userId', media.userId)
    db.session.commit()
    return jsonify({'message': 'Media item updated successfully'})

def delete_media(media_id):
    media = Media.query.get(media_id)
    if not media:
        return jsonify({'error': 'Media item not found'}), 404
    db.session.delete(media)
    db.session.commit()
    return jsonify({'message': 'Media item deleted successfully'})