import graphene # type: ignore
import inject # type: ignore

from books.schemas.types import AuthorType, BookType


class Query(graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
