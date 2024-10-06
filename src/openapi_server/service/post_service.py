from openapi_server.repository.post_repo import PostDBRepository
import logging

logger = logging.getLogger(__name__)

from openapi_server.models.post import Post
from openapi_server.models.post_create import PostCreate
from openapi_server.models.post_update import PostUpdate
from openapi_server.models.post_list_paginated import PostListPaginated
from openapi_server.models.pagination import Pagination

from openapi_server.exception import NotFoundException

class PostService:
    
    def __init__(self):
        self.post_repo = PostDBRepository()
    
    def search_post(
        self,
        offset: int = 0,
        limit: int = 10,
        title: str = None,
        author: str = None,
        visibility: str = None,
    ):
        print(offset, limit, title, author, visibility)
        posts, total_posts = self.post_repo.search_post(offset=offset, limit=limit, title=title, author=author, visibility=visibility)
        
        return PostListPaginated(
            pagination=Pagination(offset=offset, limit=limit, total=total_posts),
            data=[Post(**post) for post in posts]
        )
        
    def get_post_by_id(self, post_id: str):
        post = self.post_repo.get_post_by_id(post_id)
        
        if not post:
            raise NotFoundException("Post not found")
        
        return Post(**post)
    
    def create_post(self, post_create: PostCreate):
        post = self.post_repo.create_post(post_create.dict())
        
        return Post(**post)
    
    def update_post(self, post_id: str, post_update: PostUpdate):
        post = self.post_repo.update_post(post_id, post_update.dict())
        
        if not post:
            raise NotFoundException("Post not found")
        
        return Post(**post) 
    
    def delete_post(self, post_id: str):
        post = self.post_repo.delete_post(post_id)
        
        if not post:
            raise NotFoundException("Post not found")
        
        return None
    
    