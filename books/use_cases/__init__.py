from typing import Iterator

from books.entities import *

from .repositories import BaseAuthorRepository, BaseBookRepository


def get_all_authors(repository: BaseAuthorRepository) -> Iterator[Author]:
    return repository.get_authors()


def get_all_books(repository: BaseBookRepository) -> Iterator[Book]:
    return repository.get_books()
