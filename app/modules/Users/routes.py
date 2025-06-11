from flask import Blueprint, request, jsonify
from .Users import Users

usersRoutes = Blueprint('users', __name__)

@usersRoutes.route('/<id>', methods=['GET'])
def profile(id):
    name = request.args.get('name')
    users = Users()
    return jsonify(
        users.get_user(name, id)
    )