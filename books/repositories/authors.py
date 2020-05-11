from typing import Iterator, Optional

from books.database import Author as AuthorDB, get_session
from books.entities import Author
from books.use_cases.repositories import BaseAuthorRepository


class AuthorRepository(BaseAuthorRepository):
    def get_authors(self) -> Iterator[Author]:
        session = get_session()

        for author in session.query(AuthorDB).all():
            yield self._create_author(author)

    def _create_author(self, author: AuthorDB) -> Author:
        return Author(
            author.id,
            author.first_name,
            author.last_name,
            author.birthday_date,
            author.biography,
            author.image_path,
            author.books,
        )
