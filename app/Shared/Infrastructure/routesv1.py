from flask import Blueprint
from Infrastructure.Users.UsersController import usersController

routesv1 = Blueprint('v1', __name__)

routesv1.register_blueprint(usersController, url_prefix='/users')