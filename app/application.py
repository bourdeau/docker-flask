from flask import Flask, jsonify
from importlib import import_module
from app.blueprints import all_blueprints
from app.extensions import cors
from app.commands import hello


def create_app():
    app = Flask(__name__)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_errorhandlers(app)

    return app


def register_extensions(app):
    cors.init_app(app)

    return None


def register_blueprints(app):

    # There is only one module
    import_module(all_blueprints.import_name)
    app.register_blueprint(all_blueprints)

    # for module in all_blueprints:
    #     import_module(module.import_name)
    #     app.register_blueprint(module)

    return None

def register_commands(app):
    """ Register Commands """
    app.cli.add_command(hello)


def register_errorhandlers(app):
    @app.errorhandler(404)
    def not_found_404(error):
        return jsonify(error=404, text=str(error)), 404

    @app.errorhandler(500)
    def not_found_500(error):
        return jsonify(error=500, text=str(error)), 500
