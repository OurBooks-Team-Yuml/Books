import graphene # type: ignore
import inject # type: ignore

from books.schemas.types import AuthorType, BookType
from books.schemas.authorized import Query

from .author_mutations import *
from .book_mutations import *
from .category_mutations import *


class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()
    create_book = CreateBook.Field()
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
