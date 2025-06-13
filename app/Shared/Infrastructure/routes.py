from flask import Blueprint
# from flask import redirect
from app.Shared.Infrastructure.routesv1 import routesv1

routes = Blueprint('routes', __name__)

routes.register_blueprint(routesv1, url_prefix='/v1')

routes.route('/', methods=['GET'], defaults={'status': 'ok'})

# @routes.route('/', methods=['GET'])
# def index():
#     """
#     This is an example endpoint that returns 'Hello, World!'
#     ---
#     responses:
#         200:
#             description: A successful response
#             examples:
#                 application/json: "Hello, World!"
#     """
    # return redirect("http://localhost:8001/v1/users/2?name=Javi", code=302)