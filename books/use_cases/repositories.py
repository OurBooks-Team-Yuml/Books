from typing import Iterator, Optional

from books.database import Author as AuthorDB, Book as BookDB
from books.entities import Author, Book, Category


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


class BaseCategoryRepository(object):
    def get_categories(self) -> Iterator[Category]:
        raise NotImplementedError

    def get_by_name(self, name: str) -> Optional[Category]:
        raise NotImplementedError

    def get_by_id(self, id: int) -> Optional[Category]:
        raise NotImplementedError

    def add(self, data: dict) -> Category:
        raise NotImplementedError

    def update(self, id: int, data: dict) -> Category:
        raise NotImplementedError


class BaseElasticRepository(object):
    def add_book(self, book: Book) -> None:
        raise NotImplementedError

    def add_author(self, author: Author) -> None:
        raise NotImplementedError
