from typing import Iterator, Optional

from books.entities import *

from .exceptions import *
from .repositories import BaseAuthorRepository, BaseBookRepository


def get_all_authors(repository: BaseAuthorRepository) -> Iterator[Author]:
    return repository.get_authors()


def get_all_books(repository: BaseBookRepository) -> Iterator[Book]:
    return repository.get_books()


def get_single_book(id: int, repository: BaseBookRepository) -> Optional[Book]:
    book = repository.get_book(id)

    if not book:
        raise BookNotFound

    return book
