import graphene # type: ignore
from graphql import GraphQLError # type: ignore

import inject # type: ignore

from books.schemas.types import BookType
from books.use_cases import *
from books.use_cases.exceptions import *
from books.use_cases.repositories import BaseBookRepository


class AllBooks(object):
    books = graphene.List(BookType)

    @inject.autoparams()
    def resolve_books(self, info, repository: BaseBookRepository):
        return get_all_books(repository)


class GetBook(object):
    book_by_pk = graphene.Field(BookType, id=graphene.ID())

    @inject.autoparams()
    def resolve_book_by_pk(self, info, id: int, repository: BaseBookRepository):
        try:
            return get_single_book(id, repository)
        except BookNotFound:
            raise GraphQLError("Book not found")
