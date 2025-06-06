from flask import Blueprint, request, jsonify
from .Users import Users

usersRoutes = Blueprint('user', __name__)

@usersRoutes.route('/user/<id>', methods=['GET'])
def profile(id):
    name = request.args.get('name')
    users = Users()
    return jsonify(users.get_user(name,id))