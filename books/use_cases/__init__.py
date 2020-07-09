import itertools
import uuid
import os

from typing import Iterator, Optional

from books.entities import *

from .exceptions import *
from .repositories import *


ITEMS_ON_PAGE = 20

def _paginate(page: int, objects: Iterator) -> Iterator:
    for obj in itertools.islice(objects, (page - 1) * ITEMS_ON_PAGE, page * ITEMS_ON_PAGE):
        yield obj


def get_all_authors(page: int, repository: BaseAuthorRepository) -> Iterator[Author]:
    all_authors = repository.get_authors()
    return _paginate(page, all_authors)


def get_all_books(page: int, repository: BaseBookRepository) -> Iterator[Book]:
    all_books = repository.get_books()
    return _paginate(page, all_books)


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
        path = (
            f"http://localhost:4566/"
            f"{os.environ['AWS_AUTHORS_BUCKET_NAME']}"
            f"{s3.save_book_image(image, key)}"
        )

    author = repository.create({**data, 'image_path': path})
    elastic.add_author(author)
    return author


def new_book(data: dict, image: bytes,
    repository: BaseBookRepository, s3: BaseS3Repository, elastic: BaseElasticRepository) -> Book:
    path = None

    if image:
        key = f"{data['name']}-{uuid.uuid4()}.{image.filename.split('.')[-1]}"
        path = (
            f"http://localhost:4566/"
            f"{os.environ['AWS_BOOKS_BUCKET_NAME']}/"
            f"{s3.save_book_image(image, key)}"
        )

    book = repository.create({**data, 'image_path': path})
    elastic.add_book(book)
    return book


def new_category(data: dict, repository: BaseCategoryRepository) -> Optional[Category]:
    category = repository.get_by_name(data['name'])

    if category:
        raise CategoryAlreadyExists

    return repository.add(data)


def update_category(data: dict, repository: BaseCategoryRepository) -> Optional[Category]:
    id = data.pop('id', None)
    category = repository.get_by_id(id)

    if not category:
        raise CategoryDoesNotExists

    category = repository.get_by_name(data['name'])

    if category:
        raise CategoryAlreadyExists

    return repository.update(id, data)


def get_all_categories(repository: BaseCategoryRepository) -> Iterator[Category]:
    return repository.get_categories()
