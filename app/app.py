from flask import Flask
from config.routes.routes import routes
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app, template={
    "info": {
        "title": "My Flask API",
        "description": "An example API using Flask and Swagger",
        "version": "1.0.0"
    }
})

app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)