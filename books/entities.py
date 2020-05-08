from dataclasses import dataclass

@dataclass
class Book:
    id: int
    authors_id: list
    name: str
    description: str
    related_book: int
    image_path: str


@dataclass
class Author:
    id: int
    first_name: str
    last_name: str
    birthday_date: str
    biography: str
    image_path: str
    books: list
