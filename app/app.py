from flask import Flask
from app.Shared.Infrastructure.routes import routes
from flasgger import Swagger
import os
from dotenv import load_dotenv
import traceback
import json

app = Flask(__name__)
swagger = Swagger(app, template={
    "info": {
        "title": "My Flask API",
        "description": "An example API using Flask and Swagger",
        "version": "1.0.0"
    }
})

@app.errorhandler(Exception)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
        "traceback": traceback.format_exc()
    })
    response.content_type = "application/json"
    return response.json, response.status_code
    
load_dotenv()
app.config.update(
    HOST=os.getenv('HOST'),
    API_KEY=os.getenv('API_KEY'),
)

app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)