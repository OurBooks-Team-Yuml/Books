import os

from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='books')

    from . import database
    from .schemas import authorized

    app.add_url_rule(
        '/books/authorized/',
        view_func=GraphQLView.as_view('graphql', schema=authorized.schema, graphiql=True))

    CORS(app)

    return app
