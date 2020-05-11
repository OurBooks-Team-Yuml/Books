from hypothesis import given, strategies as st

from books.use_cases import *
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
