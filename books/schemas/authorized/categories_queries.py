import graphene # type: ignore
from graphql import GraphQLError # type: ignore

import inject # type: ignore

from books.schemas.types import CategoryType
from books.use_cases import *
from books.use_cases.exceptions import *
from books.use_cases.repositories import BaseCategoryRepository


class AllCategories(object):
    categories = graphene.List(CategoryType)

    @inject.autoparams()
    def resolve_categories(self, info, repository: BaseCategoryRepository):
        return get_all_categories(repository)
