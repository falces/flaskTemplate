from flask import Blueprint, redirect
from config.routes.routesv1 import routesv1

routes = Blueprint('routes', __name__)

routes.register_blueprint(routesv1, url_prefix='/v1')

@routes.route('/', methods=['GET'])
def index():
    return redirect("http://localhost:8001/v1/users/2?name=Javi", code=302)