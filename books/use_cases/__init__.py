import uuid

from typing import Iterator, Optional

from books.entities import *

from .exceptions import *
from .repositories import *


def get_all_authors(repository: BaseAuthorRepository) -> Iterator[Author]:
    return repository.get_authors()


def get_all_books(repository: BaseBookRepository) -> Iterator[Book]:
    return repository.get_books()


def get_single_book(id: int, repository: BaseBookRepository) -> Optional[Book]:
    book = repository.get_book(id)

    if not book:
        raise BookNotFound

    return book


def get_single_author(id: int, repository: BaseAuthorRepository) -> Optional[Author]:
    author = repository.get_author(id)

    if not author:
        raise AuthorNotFound

    return author


def new_author(data: dict, image: bytes,
    repository: BaseAuthorRepository, s3: BaseS3Repository, elastic: BaseElasticRepository) -> Author:
    path = None

    if image:
        key = f"{data['first_name']}-{data['last_name']}-{uuid.uuid4()}.{image.filename.split('.')[-1]}"
        path = s3.save_author_image(image, key)

    author = repository.create({**data, 'image_path': path})
    elastic.add_author(author)
    return author


def new_book(data: dict, image: bytes,
    repository: BaseBookRepository, s3: BaseS3Repository, elastic: BaseElasticRepository) -> Book:
    path = None

    if image:
        key = f"{data['name']}-{uuid.uuid4()}.{image.filename.split('.')[-1]}"
        path = s3.save_book_image(image, key)

    book = repository.create({**data, 'image_path': path})
    elastic.add_book(book)
    return book
