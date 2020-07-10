from flask import request
import json

import graphene # type: ignore
from graphene.types.datetime import Date # type: ignore
from graphql import GraphQLError # type: ignore

import inject # type: ignore

from books.schemas.types import BookType, Upload
from books.use_cases import *
from books.use_cases.exceptions import *
from books.use_cases.repositories import *


@inject.autoparams()
def get_repositories(
    repository: BaseBookRepository, s3: BaseS3Repository, elastic: BaseElasticRepository):
    return repository, s3, elastic


class CreateBook(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

        name = graphene.String(required=True)
        description = graphene.String(required=True)

        image_path = Upload()

        authors = graphene.List(graphene.ID, required=True)

        isbn = graphene.String()
        publishing_house = graphene.String()

        published_date = Date()

        categories = graphene.List(graphene.ID)
        related_book_id = graphene.ID()

    Output = BookType

    @staticmethod
    def mutate(root, info, **args):
        ### TODO Validation
        ### TODO Authorization
        if request.files.get('1'):
            return new_book(args, request.files.get('1', None), *get_repositories())

        return new_book(args, request.files.get('image_path', None), *get_repositories())
