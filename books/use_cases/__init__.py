from typing import Iterator, Optional

from books.entities import *

from .exceptions import *
from .repositories import BaseAuthorRepository, BaseBookRepository


def get_all_authors(repository: BaseAuthorRepository) -> Iterator[Author]:
    return repository.get_authors()


def get_all_books(repository: BaseBookRepository) -> Iterator[Book]:
    return repository.get_books()


def get_single_author(id: int, repository: BaseAuthorRepository) -> Optional[Author]:
    author = repository.get_author(id)

    if not author:
        raise AuthorNotFound

    return author
