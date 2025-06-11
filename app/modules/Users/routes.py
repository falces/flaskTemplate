from flask import Blueprint, request, jsonify
from .Users import Users
from flasgger import swag_from

usersRoutes = Blueprint('users', __name__)

@usersRoutes.route('/<id>', methods=['GET'])
@swag_from('user.yaml')
def profile(id):
    name = request.args.get('name')
    users = Users()
    return jsonify(
        users.get_user(name, id)
    )