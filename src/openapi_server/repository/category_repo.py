from openapi_server.repository.mongodb.connection_db import ConnectionDB

import logging

logger = logging.getLogger(__name__)


class CategoryDBRepository:
    def __init__(self):
        self.category_collection = ConnectionDB().get_collection("Category")

    def get_category_by_id(self, category_id: str):
        return self.category_collection.find_one({"_id": category_id})

    def create_category(self, category: dict):
        return self.category_collection.insert_one(category)

    def update_category(self, category_id: str, category: dict):
        return self.category_collection.update_one(
            {"_id": category_id}, {"$set": category}
        )

    def delete_category(self, category_id: str):
        return self.category_collection.delete_one({"_id": category_id})

    def search_category(
        self,
        offset: int,
        limit: int,
        name: str = None,
    ):
        filters = {}

        if name is not None:
            filters["name"] = name

        return list(self.category_collection.find(filters).skip(offset).limit(limit)), self.category_collection.count_documents(filters)
