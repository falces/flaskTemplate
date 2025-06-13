from flask import Blueprint
from app.Infrastructure.User.routes import usersRoutes

routesv1 = Blueprint('v1', __name__)

routesv1.register_blueprint(usersRoutes, url_prefix='/users')