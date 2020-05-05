import inject # type: ignore

from .repository import BaseBookRepository, BookRepository


def my_config(binder):
    binder.bind(BaseBookRepository, BookRepository())


inject.configure(my_config)
