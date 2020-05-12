from hypothesis import given, strategies as st

import pytest

from books.use_cases import *
from books.use_cases.exceptions import *
from books.use_cases.repositories import BaseAuthorRepository, BaseBookRepository

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
    class SuccessListRepository(BaseBookRepository):
        def get_books(*args, **kwargs):
            return books

    result = list(get_all_books(SuccessListRepository()))
    assert len(result) == len(books)


def test_get_single_author_raises_error_when_author_is_not_found():
    class FailureAuthorRepository(BaseAuthorRepository):
        def get_author(*args, **kwargs):
            return None

    with pytest.raises(AuthorNotFound):
        result = get_single_author(None, FailureAuthorRepository())


@given(author())
def test_get_single_author_correctly_returns_author_for_given_id(author):
    class SuccessAuthorRepository(BaseAuthorRepository):
        def get_author(*args, **kwargs):
            return author

    result = get_single_author(author.id, SuccessAuthorRepository())
    assert author == result
