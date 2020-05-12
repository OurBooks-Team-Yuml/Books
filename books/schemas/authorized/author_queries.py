import graphene # type: ignore
from graphql import GraphQLError # type: ignore

import inject # type: ignore

from books.schemas.types import AuthorType
from books.use_cases import *
from books.use_cases.exceptions import *
from books.use_cases.repositories import BaseAuthorRepository


class AllAuthors(object):
    authors = graphene.List(AuthorType)

    @inject.autoparams()
    def resolve_authors(self, info, repository: BaseAuthorRepository):
        return get_all_authors(repository)


class GetAuthor(object):
    author_by_pk = graphene.Field(AuthorType, id=graphene.ID())

    @inject.autoparams()
    def resolve_author_by_pk(self, info, id: int, repository: BaseAuthorRepository):
        try:
            return get_single_author(id, repository)
        except AuthorNotFound:
            raise GraphQLError("Author not found")
