from typing import Optional

import graphene # type: ignore
from graphene.types.datetime import Date # type: ignore

from books.entities import Author, Book


class Upload(graphene.Scalar):
    @staticmethod
    def serialize(value):
        return value

    @staticmethod
    def parse_literal(node):
        return node

    @staticmethod
    def parse_value(value):
        return value


class BookAuthorType(graphene.ObjectType):
    id = graphene.ID()

    first_name = graphene.String()
    last_name = graphene.String()
    full_name = graphene.String()

    def resolve_full_name(author: Author, info) -> str:
        return f"{author.first_name} {author.last_name}"


class CategoryType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()


class RelatedBookType(graphene.ObjectType):
    id = graphene.ID()

    name = graphene.String()
    description = graphene.String()

    image_path = Upload()

    authors_id = graphene.List(BookAuthorType)

    isbn = graphene.String()
    publishing_house = graphene.String()

    published_date = Date()

    categories = graphene.List(CategoryType)


class BookType(RelatedBookType):
    related_book = graphene.Field(RelatedBookType)

    def resolve_related_book(book: Book, info) -> Optional[Book]:
        if book.related_book:
            return book.related_book[0]


class AuthorType(BookAuthorType):
    birthday_date = graphene.String()
    biography = graphene.String()

    image_path = Upload()

    books = graphene.List(BookType)
