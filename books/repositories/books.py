from typing import Iterator, Optional

from books.database import Author as AuthorDB, Book as BookDB, Category, get_session
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

    def create(self, data: dict) -> Book:
        session = get_session()

        authors_id = data.pop('authors', None)
        categories = data.pop('categories', None)

        book = BookDB(**data)

        ### TODO find better way to do it.
        book.authors_id = session.query(AuthorDB).filter(AuthorDB.id.in_(authors_id)).all()
        book.categories = session.query(Category).filter(Category.id.in_(categories)).all()

        session.add(book)
        session.commit()
        session.flush()

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
