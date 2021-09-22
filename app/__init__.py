from flask import Flask
from app.routes import anime_blueprints

def create_app():
    app = Flask(__name__)

    app.register_blueprint(anime_blueprints.bp_animes)

    return app