from typing import Iterator, Optional

from books.database import Category as CategoryDB, get_session
from books.entities import Category
from books.use_cases.repositories import BaseCategoryRepository


class CategoryRepository(BaseCategoryRepository):
    def get_categories(self) -> Iterator[Category]:
        session = get_session()
        categories = session.query(CategoryDB).order_by(CategoryDB.name.asc()).all()

        for category in categories:
            yield self._create_category(category)

    def get_by_name(self, name: str) -> Optional[Category]:
        session = get_session()
        category = session.query(CategoryDB).filter_by(name=name).first()

        if category is None:
            return None

        return self._create_category(category)

    def get_by_id(self, id: int) -> Optional[Category]:
        session = get_session()
        category = session.query(CategoryDB).filter_by(id=id).first()

        if category is None:
            return None

        return self._create_category(category)

    def add(self, data: dict) -> Category:
        session = get_session()
        category = CategoryDB(**data)

        session.add(category)
        session.commit()
        session.flush()

        return self._create_category(category)

    def update(self, id: int, data: dict) -> Category:
        ### TODO: Find a way to get object after update.
        session = get_session()

        session.query(CategoryDB).filter_by(
            id=id
        ).update(data)

        session.commit()
        session.flush()

        category = session.query(CategoryDB).filter_by(id=id).first()
        return self._create_category(category)

    def _create_category(self, category: CategoryDB) -> Category:
        return Category(category.id, category.name)
