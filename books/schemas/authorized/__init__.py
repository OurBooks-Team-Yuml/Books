import graphene # type: ignore

from .author_queries import *
from .books_queries import *
from .categories_queries import *


class Query(AllAuthors, AllBooks, AllCategories, GetAuthor, GetBook, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
