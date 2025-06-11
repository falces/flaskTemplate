from flask import Blueprint, jsonify
from modules.Users.routes import usersRoutes

routesv1 = Blueprint('v1', __name__)

routesv1.register_blueprint(usersRoutes, url_prefix='/users')