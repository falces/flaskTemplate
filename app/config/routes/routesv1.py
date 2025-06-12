from flask import Blueprint, jsonify
from modules.Countries.routes import countriesRoutes

routesv1 = Blueprint('v1', __name__)

routesv1.register_blueprint(countriesRoutes, url_prefix='/countries')