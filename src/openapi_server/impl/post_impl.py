# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.post_create import PostCreate
from openapi_server.models.post_list_paginated import PostListPaginated
from openapi_server.models.post_patch import PostPatch
from openapi_server.models.post_response import PostResponse
from openapi_server.models.post_update import PostUpdate

from openapi_server.service.post_service import PostService
from openapi_server.apis.post_api_base import BasePostApi

class PostApi(BasePostApi):
    def __init__(self):
        self.post_service = PostService()
    async def posts_get(
        self,
        title: str,
        author: str,
        visibility: str,
        limit: int,
        offset: int,
    ) -> PostListPaginated:
        return self.post_service.search_post(offset=offset, limit=limit, title=title, author=author, visibility=visibility)