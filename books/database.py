import os

from sqlalchemy import (create_engine, Column, Date, ForeignKey,
    Integer, MetaData, String, Table, Text)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


engine = create_engine(os.environ['DATABASE_URI'])
metadata = MetaData(engine)
Base = declarative_base()


joined_table = Table("authors_books", Base.metadata,
    Column("author_id", Integer, ForeignKey("authors.id"), primary_key=True),
    Column("book_id", Integer, ForeignKey("books.id"), primary_key=True))


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)

    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)

    birthday_date = Column(Date())
    biography = Column(Text())

    image_path = Column(String(1000))


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)

    name = Column(String(300), nullable=False)
    description = Column(Text(), nullable=False)

    image_path = Column(String(1000))

    authors_id = relationship(Author, secondary=joined_table, backref="books")
    related_book = Column(Integer, ForeignKey('books.id'))


if not engine.dialect.has_table(engine, 'authors'):
    Base.metadata.create_all(engine)
