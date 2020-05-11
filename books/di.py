import inject # type: ignore

from books.repositories.authors import AuthorRepository
from books.repositories.books import BookRepository
from books.use_cases.repositories import BaseAuthorRepository, BaseBookRepository

def my_config(binder):
    binder.bind(BaseBookRepository, BookRepository())
    binder.bind(BaseAuthorRepository, AuthorRepository())


inject.configure(my_config)
