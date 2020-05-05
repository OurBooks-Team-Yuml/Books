import graphene # type: ignore
import inject # type: ignore


class Book(graphene.ObjectType):
    _id = graphene.String()
    name = graphene.String()
    description = graphene.String()
    author_id = graphene.String()


class Query(graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
