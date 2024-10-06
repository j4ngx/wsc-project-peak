# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.post_api_base import BasePostApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.post_create import PostCreate
from openapi_server.models.post_list_paginated import PostListPaginated
from openapi_server.models.post_patch import PostPatch
from openapi_server.models.post_response import PostResponse
from openapi_server.models.post_update import PostUpdate


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/posts",
    responses={
        200: {"model": PostListPaginated, "description": "List of posts retrieved successfully"},
        401: {"model": ErrorResponse, "description": "Unauthorized. The client must authenticate itself to get the requested response."},
        403: {"model": ErrorResponse, "description": "Forbidden. The client does not have access rights to the content."},
        500: {"model": ErrorResponse, "description": "Internal Server Error. The server has encountered a situation it doesn&#39;t know how to handle."},
    },
    tags=["Post"],
    summary="Get all posts or search for posts",
    response_model_by_alias=True,
)
async def posts_get(
    title: str = Query(None, description="Search posts by title", alias="title"),
    author: str = Query(None, description="Search posts by author", alias="author"),
    visibility: str = Query(None, description="Filter posts by visibility status (draft, review, public)", alias="visibility"),
    limit: int = Query(10, description="Limit the number of posts returned", alias="limit"),
    offset: int = Query(0, description="The number of posts to skip before starting to collect the result set", alias="offset"),
) -> PostListPaginated:
    """Retrieve a list of posts or search posts by title, author, or visibility"""
    if not BasePostApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePostApi.subclasses[0]().posts_get(title, author, visibility, limit, offset)


@router.post(
    "/posts",
    responses={
        201: {"model": PostResponse, "description": "Post created successfully"},
        401: {"model": ErrorResponse, "description": "Unauthorized. The client must authenticate itself to get the requested response."},
        403: {"model": ErrorResponse, "description": "Forbidden. The client does not have access rights to the content."},
        500: {"model": ErrorResponse, "description": "Internal Server Error. The server has encountered a situation it doesn&#39;t know how to handle."},
    },
    tags=["Post"],
    summary="Create a new post",
    response_model_by_alias=True,
)
async def posts_post(
    post_create: PostCreate = Body(None, description=""),
) -> PostResponse:
    if not BasePostApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePostApi.subclasses[0]().posts_post(post_create)


@router.delete(
    "/posts/{postId}",
    responses={
        204: {"description": "Post deleted"},
        401: {"model": ErrorResponse, "description": "Unauthorized. The client must authenticate itself to get the requested response."},
        403: {"model": ErrorResponse, "description": "Forbidden. The client does not have access rights to the content."},
        404: {"model": ErrorResponse, "description": "Not Found. The server can not find the requested resource."},
        500: {"model": ErrorResponse, "description": "Internal Server Error. The server has encountered a situation it doesn&#39;t know how to handle."},
    },
    tags=["Post"],
    summary="Delete a post",
    response_model_by_alias=True,
)
async def posts_post_id_delete(
    postId: str = Path(..., description=""),
) -> None:
    if not BasePostApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePostApi.subclasses[0]().posts_post_id_delete(postId)


@router.get(
    "/posts/{postId}",
    responses={
        200: {"model": PostResponse, "description": "Post created successfully"},
        401: {"model": ErrorResponse, "description": "Unauthorized. The client must authenticate itself to get the requested response."},
        403: {"model": ErrorResponse, "description": "Forbidden. The client does not have access rights to the content."},
        404: {"model": ErrorResponse, "description": "Not Found. The server can not find the requested resource."},
        500: {"model": ErrorResponse, "description": "Internal Server Error. The server has encountered a situation it doesn&#39;t know how to handle."},
    },
    tags=["Post"],
    summary="Get a single post",
    response_model_by_alias=True,
)
async def posts_post_id_get(
    postId: str = Path(..., description=""),
) -> PostResponse:
    if not BasePostApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePostApi.subclasses[0]().posts_post_id_get(postId)


@router.patch(
    "/posts/{postId}",
    responses={
        200: {"model": PostResponse, "description": "Post created successfully"},
        401: {"model": ErrorResponse, "description": "Unauthorized. The client must authenticate itself to get the requested response."},
        403: {"model": ErrorResponse, "description": "Forbidden. The client does not have access rights to the content."},
        404: {"model": ErrorResponse, "description": "Not Found. The server can not find the requested resource."},
        500: {"model": ErrorResponse, "description": "Internal Server Error. The server has encountered a situation it doesn&#39;t know how to handle."},
    },
    tags=["Post"],
    summary="Partially update a post",
    response_model_by_alias=True,
)
async def posts_post_id_patch(
    postId: str = Path(..., description=""),
    post_patch: PostPatch = Body(None, description=""),
) -> PostResponse:
    if not BasePostApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePostApi.subclasses[0]().posts_post_id_patch(postId, post_patch)


@router.put(
    "/posts/{postId}",
    responses={
        200: {"model": PostResponse, "description": "Post created successfully"},
        401: {"model": ErrorResponse, "description": "Unauthorized. The client must authenticate itself to get the requested response."},
        403: {"model": ErrorResponse, "description": "Forbidden. The client does not have access rights to the content."},
        404: {"model": ErrorResponse, "description": "Not Found. The server can not find the requested resource."},
        500: {"model": ErrorResponse, "description": "Internal Server Error. The server has encountered a situation it doesn&#39;t know how to handle."},
    },
    tags=["Post"],
    summary="Update a post",
    response_model_by_alias=True,
)
async def posts_post_id_put(
    postId: str = Path(..., description=""),
    post_update: PostUpdate = Body(None, description=""),
) -> PostResponse:
    if not BasePostApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BasePostApi.subclasses[0]().posts_post_id_put(postId, post_update)
