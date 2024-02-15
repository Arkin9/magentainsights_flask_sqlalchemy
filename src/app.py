from flask import Flask,render_template
from config import Config
from extentions import db
from flask_migrate import Migrate
from routes import main


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_resources(app)
    register_extentions(app)
    return app

def register_extentions(app):
    db.init_app(app)
    migrate = Migrate(app,db)

def register_resources(app):
    app.register_blueprint(main)    

if __name__ == '__main__':
    app = create_app()
    app.run('127.0.0.1',5000)