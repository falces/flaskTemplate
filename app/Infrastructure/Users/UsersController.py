from flask import Blueprint, request, jsonify
from Application.UsersService import UsersService
from flasgger import swag_from

usersController = Blueprint('users', __name__)

# UsersService = UsersService()

@usersController.route('/', methods=['POST'])
def createUser():
    data = request.get_json()
    user = UsersService.createUser(data)
    return jsonify(user), 201

@usersController.route('/', methods=['GET'])
def getUsers():
    return jsonify(
        UsersService.getUsers()
    )

@usersController.route('/<uuid:userId>', methods=['GET'])
def getUser(userId):
    return jsonify(
        UsersService.getUsers(userId)
    )

@usersController.route('/<id>', methods=['GET'])
@swag_from('user.yaml')
def profile(id):
    return jsonify(
        UsersService.getUser(id)
    )