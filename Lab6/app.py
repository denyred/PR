from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.database import db
from models.electro_scooter import ElectroScooter
from flask_swagger_ui import get_swaggerui_blueprint
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='static/.env')
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    db.init_app(app)


    swagger_ui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': 'Access API'
        }
    )
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    return app

if __name__ == "__main__":
    app = create_app()
    import routes
    app.run()