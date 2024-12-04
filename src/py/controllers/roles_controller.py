from extensions import db
from models import Role
from sqlalchemy.exc import IntegrityError
from flask import request, jsonify

def get_all_roles():
    roles = Role.query.all()
    return jsonify([{
        'id': role.id,
        'roleName': role.roleName,
        'permission': role.permission
    } for role in roles])

def create_role():
    data = request.json
    try:
        new_role = Role(
            roleName=data['roleName'],
            permission=data['permission']
        )
        db.session.add(new_role)
        db.session.commit()
        return jsonify({'message': 'Role created successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Role creation failed. Integrity error'}), 400

def get_role(role_id):
    role = Role.query.get(role_id)
    if not role:
        return jsonify({'error': 'Role not found'}), 404
    return jsonify({
        'id': role.id,
        'roleName': role.roleName,
        'permission': role.permission
    })

def update_role(role_id):
    role = Role.query.get(role_id)
    if not role:
        return jsonify({'error': 'Role not found'}), 404
    data = request.json
    role.roleName = data.get('roleName', role.roleName)
    role.permission = data.get('permission', role.permission)
    db.session.commit()
    return jsonify({'message': 'Role updated successfully'})

def delete_role(role_id):
    role = Role.query.get(role_id)
    if not role:
        return jsonify({'error': 'Role not found'}), 404
    db.session.delete(role)
    db.session.commit()
    return jsonify({'message': 'Role deleted successfully'})