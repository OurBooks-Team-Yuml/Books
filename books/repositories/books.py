from typing import Iterator, Optional

from books.database import Book as BookDB, get_session
from books.entities import Book
from books.use_cases.repositories import BaseBookRepository


class BookRepository(BaseBookRepository):
    def get_books(self) -> Iterator[Book]:
        session = get_session()

        for book in session.query(BookDB).order_by(BookDB.id.asc()).all():
            yield self._create_book(book)

    def get_book(self, id: int) -> Optional[Book]:
        session = get_session()
        book = session.query(BookDB).filter(BookDB.id == id).first()

        if not book:
            return None

        return self._create_book(book)

    def _create_book(self, book: BookDB) -> Book:
        return Book(
            book.id,
            book.authors_id,
            book.name,
            book.description,
            book.related_book,
            book.image_path,
            book.isbn,
            book.publishing_house,
            book.published_date,
            book.categories,
        )
