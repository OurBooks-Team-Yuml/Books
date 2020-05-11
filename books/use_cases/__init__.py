from typing import Iterator

from books.entities import *

from .repositories import BaseAuthorRepository


def get_all_authors(repository: BaseAuthorRepository) -> Iterator[Author]:
    return repository.get_authors()
