from typing import Any
from flask import Flask
from application import views



def create_app(config_object="application.settings"):
	app = Flask(__name__)
	app.config.from_object(config_object)
	register_blueprints(app)
	return app


def register_blueprints(app):

	app.register_blueprint(views.views.blueprint)
	return None
