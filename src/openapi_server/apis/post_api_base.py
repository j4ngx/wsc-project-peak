# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.post_create import PostCreate
from openapi_server.models.post_list_paginated import PostListPaginated
from openapi_server.models.post_patch import PostPatch
from openapi_server.models.post_response import PostResponse
from openapi_server.models.post_update import PostUpdate


class BasePostApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BasePostApi.subclasses = BasePostApi.subclasses + (cls,)
    async def posts_get(
        self,
        title: str,
        author: str,
        visibility: str,
        limit: int,
        offset: int,
    ) -> PostListPaginated:
        """Retrieve a list of posts or search posts by title, author, or visibility"""
        ...


    async def posts_post(
        self,
        post_create: PostCreate,
    ) -> PostResponse:
        ...


    async def posts_post_id_delete(
        self,
        postId: str,
    ) -> None:
        ...


    async def posts_post_id_get(
        self,
        postId: str,
    ) -> PostResponse:
        ...


    async def posts_post_id_patch(
        self,
        postId: str,
        post_patch: PostPatch,
    ) -> PostResponse:
        ...


    async def posts_post_id_put(
        self,
        postId: str,
        post_update: PostUpdate,
    ) -> PostResponse:
        ...
