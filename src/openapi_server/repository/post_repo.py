from openapi_server.repository.mongodb.connection_db import ConnectionDB

import logging

logger = logging.getLogger(__name__)

class PostDBRepository:

    def __init__(self):
        self.post_collection = ConnectionDB().get_collection("Post")

    def search_post(
        self,
        offset: int = 0,
        limit: int = 10,
        author: str = None,
        title: str = None,
        content: str = None,
        visibility: str = None,
    ):
        filters = {}

        if author is not None:
            filters["author"] = author

        if title is not None:
            filters["title"] = title

        if content is not None:
            filters["content"] = content
        
        total_count = self.post_collection.count_documents(filters)
        posts_cursor = self.post_collection.find(filters).skip(int(offset)).limit(int(limit))

        posts = list(posts_cursor)

        return posts, total_count
    
    def get_post_by_id(self, post_id: str):
        return self.post_collection.find_one({"_id": post_id})
    
    def create_post(self, post: dict):
        return self.post_collection.insert_one(post)
    
    def update_post(self, post_id: str, post: dict):
        return self.post_collection.update_one({"_id": post}, {"$set": post})
    
    def delete_post(self, post_id: str):
        return self.post_collection.delete_one({"_id": post_id})
    