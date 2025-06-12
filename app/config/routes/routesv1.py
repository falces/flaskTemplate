from flask import Blueprint
from modules.Countries.routes import countriesRoutes
from modules.Users.routes import usersRoutes
from modules.HarmonisedCodes.routes import harmonisedCodesRoutes

routesv1 = Blueprint('v1', __name__)

routesv1.register_blueprint(usersRoutes, url_prefix='/users')
routesv1.register_blueprint(countriesRoutes, url_prefix='/countries')
routesv1.register_blueprint(harmonisedCodesRoutes, url_prefix='/harmonisedCodes')