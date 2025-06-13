from flask import Blueprint, request, jsonify
from app.Domain.Users.Users import Users
from flasgger import swag_from

usersRoutes = Blueprint('users', __name__)

@usersRoutes.route('/', methods=['GET'])
def getUsers():
    # name = request.args.get('name')
    # users = Users()
    return jsonify(
        Users.getUsers()
    )
    
@usersRoutes.route('/<str:userId>', methods=['GET'])
def getUser(userId):
    return jsonify(
        Users.getUser(userId)
    )

@usersRoutes.route('/<id>', methods=['GET'])
@swag_from('user.yaml')
def profile(id):
    return jsonify(
        Users.getUser(id)
    )