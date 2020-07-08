import os

from flask import Flask, request
from flask_cors import CORS
from flask_graphql import GraphQLView

from .database import get_session


class FileUploadGraphQLView(GraphQLView):
    def parse_body(self):
        content_type = request.mimetype

        if content_type == 'multipart/form-data':
            operations = load_json_body(request.form.get('operations', '{}'))
            files_map = load_json_body(request.form.get('map', '{}'))

            return place_files_in_operations(
                operations,
                files_map,
                request.files
            )

        return super(FileUploadGraphQLView, self).parse_body()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='books')

    from . import database
    from .schemas import authorized
    from .schemas import secured

    app.add_url_rule(
        '/books/authorized/',
        view_func=GraphQLView.as_view('authorized', schema=authorized.schema, graphiql=True, batch=True))

    app.add_url_rule(
        '/books/secured/',
        view_func=FileUploadGraphQLView.as_view('secured', schema=secured.schema, graphiql=True, batch=True))

    CORS(app)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        get_session().remove()

    return app
