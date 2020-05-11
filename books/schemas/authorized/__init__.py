import graphene # type: ignore

from .author_queries import *
from .books_queries import *


class Query(AllAuthors, AllBooks, GetAuthor, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
