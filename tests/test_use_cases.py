from hypothesis import given, strategies as st

import pytest

from books.use_cases import *
from books.use_cases.exceptions import *
from books.use_cases.repositories import BaseAuthorRepository

from .generators import *


@given(st.lists(author()))
def test_get_all_authors_returns_correct_list(authors):
    class SuccessListRepository(BaseAuthorRepository):
        def get_authors(*args, **kwargs):
            return authors

    result = list(get_all_authors(SuccessListRepository()))
    assert len(result) == len(authors)


@given(st.lists(book()))
def test_get_all_books_returns_correct_list(books):
    class SuccessListRepository(BaseAuthorRepository):
        def get_books(*args, **kwargs):
            return books

    result = list(get_all_books(SuccessListRepository()))
    assert len(result) == len(books)


def test_get_single_book_raises_error_when_book_is_not_found():
    class FailureBookRepository(BaseBookRepository):
        def get_book(*args, **kwargs):
            return None

    with pytest.raises(BookNotFound):
        result = get_single_book(None, FailureBookRepository())


@given(book())
def test_get_single_book_correctly_returns_book_for_given_id(book):
    class SuccessBookRepository(BaseBookRepository):
        def get_book(*args, **kwargs):
            return book

    result = get_single_book(book.id, SuccessBookRepository())
    assert book == result
