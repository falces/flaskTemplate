from flask import Blueprint, jsonify, Flask
from modules.users.routes import usersRoutes

routesv1 = Blueprint('routesv1', __name__)

routesv1.register_blueprint(usersRoutes, url_prefix='/users')