from flask import Flask
from config.routes.routes import routes
from flasgger import Swagger
import os
from dotenv import load_dotenv

app = Flask(__name__)
swagger = Swagger(app, template={
    "info": {
        "title": "My Flask API",
        "description": "An example API using Flask and Swagger",
        "version": "1.0.0"
    }
})

load_dotenv()
app.config.update(
    HOST=os.getenv('HOST'),
    API_KEY=os.getenv('API_KEY'),
)

app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)