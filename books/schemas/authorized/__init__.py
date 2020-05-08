import graphene # type: ignore

from .queries import *


class Query(AllAuthors, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
