from .database import Author as AuthorDB, Book as BookDB
from .entities import Author, Book


class BaseBookRepository(object):
    pass


class BookRepository(BaseBookRepository):
    pass
