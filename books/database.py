import os

from elasticsearch import Elasticsearch

from sqlalchemy import (create_engine, Column, Date, ForeignKey,
    Integer, MetaData, String, Table, Text)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

from .fixtures.dev import authors, books, categories

engine = create_engine(os.environ['DATABASE_URI'])
metadata = MetaData(engine)
Base = declarative_base()


joined_table = Table("authors_books", Base.metadata,
    Column("author_id", Integer, ForeignKey("authors.id"), primary_key=True),
    Column("book_id", Integer, ForeignKey("books.id"), primary_key=True))


joined_categories_table = Table("books_categories", Base.metadata,
    Column("category_id", Integer, ForeignKey("categories.id"), primary_key=True),
    Column("book_id", Integer, ForeignKey("books.id"), primary_key=True))


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)

    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)

    birthday_date = Column(Date())
    biography = Column(Text())

    image_path = Column(String(1000))


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(300), nullable=False, unique=True)


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)

    name = Column(String(300), nullable=False)
    description = Column(Text(), nullable=False)

    image_path = Column(String(1000))

    authors_id = relationship(Author, secondary=joined_table, backref="books")
    categories = relationship("Category", secondary=joined_categories_table, backref="books")

    related_book_id = Column(Integer, ForeignKey('books.id'))
    related_book = relationship("Book")

    isbn = Column(String(50), unique=True)
    publishing_house = Column(String(200))

    published_date = Column(Date())


if not engine.dialect.has_table(engine, 'authors'):
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    es_url = os.environ.get('ES_URL', None)

    for book in books.books:
        session.add(Book(**book))
        session.commit()
        session.flush()

        if es_url:
            es = Elasticsearch(es_url)
            es.index(index=os.environ['ES_BOOKS_INDEX'], id=book.id, body=book)

    for category in categories.categories:
        session.add(Category(**category))
        session.commit()
        session.flush()

    for author in authors.authors:
        session.add(Author(**author))
        session.commit()
        session.flush()

        if es_url:
            es = Elasticsearch(es_url)
            es.index(index=os.environ['ES_AUTHORS_INDEX'], id=author.id, body=author)

    engine.execute(joined_table.insert({'author_id': 1, 'book_id': 1}))
    engine.execute(joined_table.insert({'author_id': 1, 'book_id': 2}))

    engine.execute(joined_categories_table.insert({'category_id': 1, 'book_id': 1}))
    engine.execute(joined_categories_table.insert({'category_id': 2, 'book_id': 2}))


def get_session():
    Session = sessionmaker(bind=engine)
    return Session()
