import graphene # type: ignore
import inject # type: ignore

from books.schemas.types import BookType
from books.use_cases import *
from books.use_cases.repositories import BaseBookRepository


class AllBooks(object):
    books = graphene.List(BookType)

    @inject.autoparams()
    def resolve_books(self, info, repository: BaseBookRepository):
        return get_all_books(repository)
