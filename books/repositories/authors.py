from typing import Iterator, Optional

from books.database import Author as AuthorDB
from books.entities import Author
from books.use_cases.repositories import BaseAuthorRepository


class AuthorRepository(BaseAuthorRepository):
    pass
