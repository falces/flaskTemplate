from flask import Flask
from config.routes.routesv1 import routesv1

app = Flask(__name__)
app.register_blueprint(routesv1, url_prefix='/v1')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)