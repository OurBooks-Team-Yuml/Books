from hypothesis import strategies as st

from books.entities import Author


@st.composite
def author(draw):
    id = draw(st.integers(min_value=1))
    first_name = draw(st.text(min_size=1, alphabet=st.characters(whitelist_categories=('Ll', 'Lu'))))
    last_name = draw(st.text(min_size=1, alphabet=st.characters(whitelist_categories=('Ll', 'Lu'))))
    data = draw(st.dates())
    biography = draw(st.text(min_size=1, alphabet=st.characters(whitelist_categories=('Ll', 'Lu'))))
    image_path = draw(st.text(min_size=1, alphabet=st.characters(whitelist_categories=('Ll', 'Lu'))))

    return Author(
        id,
        first_name,
        last_name,
        data,
        biography,
        image_path,
        []
    )
