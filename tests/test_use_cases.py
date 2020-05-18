from hypothesis import assume, given, strategies as st

import pytest

from books.use_cases import *
from books.use_cases.exceptions import *
from books.use_cases.repositories import *

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


@given(st.lists(category()))
def test_get_all_categories_returns_all_categories_in_list(categories):
    class SuccessListRepository(BaseCategoryRepository):
        def get_categories(*args, **kwargs):
            return categories

    result = list(get_all_categories(SuccessListRepository()))
    assert len(result) == len(categories)


@given(category())
def test_create_new_category_returns_category(category):
    class SuccessCreateRepository(BaseCategoryRepository):
        def get_by_name(*args, **kwargs):
            return None

        def add(*args, **kwargs):
            return category

    result = new_category({'name': category.name}, SuccessCreateRepository())
    assert result == category


@given(category())
def test_create_new_category_raises_error_when_name_already_exists(category):
    class FailureCreateRepository(BaseCategoryRepository):
        def get_by_name(*args, **kwargs):
            return category

    with pytest.raises(CategoryAlreadyExists):
        result = new_category({'name': category.name}, FailureCreateRepository())


@given(category(), draw_string())
def test_update_category_returns_category_with_updated_data(category, name):
    assume(name != category.name)

    class SuccessUpdateRepository(BaseCategoryRepository):
        def get_by_name(*args, **kwargs):
            return None

        def get_by_id(*args, **kwargs):
            return category

        def update(*args, **kwargs):
            category.name = name
            return category

    result = update_category({'name': category.name}, SuccessUpdateRepository())
    assert result.name == name


@given(category())
def test_update_category_raises_error_when_name_already_exists(category):
    class FailureUpdateRepository(BaseCategoryRepository):
        def get_by_name(*args, **kwargs):
            return category

        def get_by_id(*args, **kwargs):
            return category

        def update(*args, **kwargs):
            category.name = name
            return category

    with pytest.raises(CategoryAlreadyExists):
        result = update_category({'name': category.name}, FailureUpdateRepository())


@given(category())
def test_update_category_raises_error_when_category_not_found_by_id(category):
    class FailureUpdateRepository(BaseCategoryRepository):
        def get_by_name(*args, **kwargs):
            return None

        def get_by_id(*args, **kwargs):
            return None

        def update(*args, **kwargs):
            category.name = name
            return category

    with pytest.raises(CategoryDoesNotExists):
        result = update_category({'name': category.name}, FailureUpdateRepository())
