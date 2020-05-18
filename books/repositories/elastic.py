from dataclasses import asdict
import os

from elasticsearch import Elasticsearch

from books.entities import Author, Book
from books.use_cases.repositories import BaseElasticRepository


class ElasticRepository(BaseElasticRepository):
    def add_book(self, book: Book) -> None:
        es = self._get_elastic()
        es.index(index=os.environ['ES_BOOKS_INDEX'], id=book.id, body=asdict(book))

    def add_author(self, author: Author) -> None:
        es = self._get_elastic()
        es.index(index=os.environ['ES_AUTHORS_INDEX'], id=author.id, body=asdict(author))

    def _get_elastic(self) -> Elasticsearch:
        return Elasticsearch(os.environ['ES_URL'])
