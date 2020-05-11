import graphene # type: ignore


### TODO
class BookType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()


class AuthorType(graphene.ObjectType):
    id = graphene.ID()

    first_name = graphene.String()
    last_name = graphene.String()

    birthday_date = graphene.String()
    biography = graphene.String()

    image_path = graphene.String()

    books = graphene.List(BookType)
