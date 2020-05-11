import os

from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='books')

    from . import database

    ### TODO
    # from .schema import schema

    # app.add_url_rule('/books', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

    CORS(app)

    return app
