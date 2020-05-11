from hypothesis import strategies as st

from books.entities import Author, Book


def draw_string(draw):
    return draw(st.text(min_size=1, alphabet=st.characters(whitelist_categories=('Ll', 'Lu'))))


@st.composite
def author(draw):
    id = draw(st.integers(min_value=1))
    first_name = draw_string(draw)
    last_name = draw_string(draw)
    data = draw(st.dates())
    biography = draw_string(draw)
    image_path = draw_string(draw)

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
    name = draw_string(draw)
    description = draw_string(draw)

    image_path = draw_string(draw)

    isbn = draw_string(draw)
    publishing_house = draw_string(draw)

    date = draw(st.dates())

    category = draw_string(draw)

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
