import inject # type: ignore

from books.repositories.authors import AuthorRepository
from books.repositories.books import BookRepository
from books.repositories.categories import CategoryRepository
from books.repositories.s3 import S3Repository
from books.use_cases.repositories import *


def my_config(binder):
    binder.bind(BaseBookRepository, BookRepository())
    binder.bind(BaseAuthorRepository, AuthorRepository())
    binder.bind(BaseS3Repository, S3Repository())
    binder.bind(BaseCategoryRepository, CategoryRepository())

inject.configure(my_config)
