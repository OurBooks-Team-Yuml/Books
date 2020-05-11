import graphene # type: ignore
import inject # type: ignore

from books.schemas.types import AuthorType, BookType
from books.use_cases import *
from books.use_cases.repositories import BaseAuthorRepository


class AllAuthors(object):
    authors = graphene.List(AuthorType)

    @inject.autoparams()
    def resolve_authors(self, info, repository: BaseAuthorRepository):
        return get_all_authors(repository)
