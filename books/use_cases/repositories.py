from typing import Iterator, Optional

from books.database import Author as AuthorDB, Book as BookDB
from books.entities import Author, Book


class BaseAuthorRepository(object):
    def get_authors(self) -> Iterator[Author]:
        raise NotImplementedError

    def get_author(self, id: int) -> Optional[Author]:
        raise NotImplementedError

    def create(self, data: dict) -> Author:
        raise NotImplementedError

    def update(self, id: int, data: dict) -> Author:
        raise NotImplementedError


class BaseBookRepository(object):
    def get_books(self) -> Iterator[Book]:
        raise NotImplementedError

    def get_book(self, id: int) -> Optional[Book]:
        raise NotImplementedError

    def create(self, data: dict) -> Book:
        raise NotImplementedError

    def update(self, id: int, data: dict) -> Book:
        raise NotImplementedError


class BaseS3Repository(object):
    def save_author_image(self, image: bytes, key: str) -> str:
        raise NotImplementedError

    def save_book_image(self, image: bytes, key: str) -> str:
        raise NotImplementedError
