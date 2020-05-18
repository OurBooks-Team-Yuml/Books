from hypothesis import strategies as st

from books.entities import Author, Book, Category


@st.composite
def draw_string(draw):
    return draw(st.text(min_size=1, alphabet=st.characters(whitelist_categories=('Ll', 'Lu'))))


@st.composite
def author(draw):
    id = draw(st.integers(min_value=1))
    first_name = draw(draw_string())
    last_name = draw(draw_string())
    data = draw(st.dates())
    biography = draw(draw_string())
    image_path = draw(draw_string())

    return Author(
        id,
        first_name,
        last_name,
        data,
        biography,
        image_path,
        []
    )


@st.composite
def book(draw):
    author_of_book = draw(author()).id

    id = draw(st.integers(min_value=1))
    name = draw(draw_string())
    description = draw(draw_string())

    image_path = draw(draw_string())

    isbn = draw(draw_string())
    publishing_house = draw(draw_string())

    date = draw(st.dates())

    category = draw(draw_string())

    related_book = None ### TODO

    return Book(
        id,
        [author_of_book],
        name,
        description,
        related_book,
        image_path,
        isbn,
        publishing_house,
        date,
        [category]
    )


@st.composite
def category(draw):
    id = draw(st.integers(min_value=1))
    name = draw(draw_string())

    return Category(id, name)
