from flask import request

import graphene # type: ignore
from graphql import GraphQLError # type: ignore

import inject # type: ignore

from books.schemas.types import AuthorType, Upload
from books.use_cases import *
from books.use_cases.exceptions import *
from books.use_cases.repositories import *


@inject.autoparams()
def get_repositories(
    repository: BaseAuthorRepository, s3: BaseS3Repository, elastic: BaseElasticRepository):
    return repository, s3, elastic


class CreateAuthor(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)

        birthday_date = graphene.Date()
        biography = graphene.String()

        image_path = Upload()

    Output = AuthorType

    @staticmethod
    def mutate(root, info, **args):
        return new_author(args, request.files.get('image_path', None), *get_repositories())
