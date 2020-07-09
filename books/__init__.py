import os

from flask import Flask, request
from flask_cors import CORS
from flask_graphql import GraphQLView
from graphene_file_upload.flask import FileUploadGraphQLView

from .database import get_session


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='books')

    CORS(app, resources={r"/*": {"origins": "*"}})

    from . import database
    from .schemas import authorized
    from .schemas import secured

    app.add_url_rule(
        '/books/authorized/',
        view_func=GraphQLView.as_view('authorized', schema=authorized.schema, graphiql=True, batch=True))

    app.add_url_rule(
        '/books/secured/',
        view_func=FileUploadGraphQLView.as_view('secured', schema=secured.schema, graphiql=True, batch=True))

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        get_session().remove()

    return app
