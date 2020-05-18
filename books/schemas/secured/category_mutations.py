from flask import request

import graphene # type: ignore
from graphql import GraphQLError # type: ignore

import inject # type: ignore

from books.schemas.types import CategoryType
from books.use_cases import *
from books.use_cases.exceptions import *
from books.use_cases.repositories import BaseCategoryRepository


@inject.autoparams()
def get_repositories(repository: BaseCategoryRepository):
    return repository


class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    Output = CategoryType

    @staticmethod
    def mutate(root, info, **args):
        try:
            return new_category(args, get_repositories())
        except CategoryAlreadyExists:
            raise GraphQLError("Category already exists") 


class UpdateCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)

    Output = CategoryType

    @staticmethod
    def mutate(root, info, **args):
        try:
            return update_category(args, get_repositories())
        except CategoryDoesNotExists:
            raise GraphQLError("Category does not exists")
        except CategoryAlreadyExists:
            raise GraphQLError("Category already exists with passed name")
