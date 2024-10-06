# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.category_api_base import BaseCategoryApi
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
from openapi_server.models.category import Category
from openapi_server.models.category_create import CategoryCreate
from openapi_server.models.category_update import CategoryUpdate
from openapi_server.models.error_response import ErrorResponse


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.delete(
    "/categories/{categoryId}",
    responses={
        204: {"description": "Category deleted"},
        401: {"model": ErrorResponse, "description": "Unauthorized. The client must authenticate itself to get the requested response."},
        403: {"model": ErrorResponse, "description": "Forbidden. The client does not have access rights to the content."},
        404: {"model": ErrorResponse, "description": "Not Found. The server can not find the requested resource."},
        500: {"model": ErrorResponse, "description": "Internal Server Error. The server has encountered a situation it doesn&#39;t know how to handle."},
    },
    tags=["Category"],
    summary="Delete a category",
    response_model_by_alias=True,
)
async def categories_category_id_delete(
    categoryId: str = Path(..., description=""),
) -> None:
    if not BaseCategoryApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCategoryApi.subclasses[0]().categories_category_id_delete(categoryId)


@router.get(
    "/categories/{categoryId}",
    responses={
        200: {"model": Category, "description": "Category retrieved successfully"},
        401: {"model": ErrorResponse, "description": "Unauthorized. The client must authenticate itself to get the requested response."},
        403: {"model": ErrorResponse, "description": "Forbidden. The client does not have access rights to the content."},
        404: {"model": ErrorResponse, "description": "Not Found. The server can not find the requested resource."},
        500: {"model": ErrorResponse, "description": "Internal Server Error. The server has encountered a situation it doesn&#39;t know how to handle."},
    },
    tags=["Category"],
    summary="Get a single category",
    response_model_by_alias=True,
)
async def categories_category_id_get(
    categoryId: str = Path(..., description=""),
) -> Category:
    if not BaseCategoryApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCategoryApi.subclasses[0]().categories_category_id_get(categoryId)


@router.put(
    "/categories/{categoryId}",
    responses={
        200: {"model": Category, "description": "Category updated successfully"},
        401: {"model": ErrorResponse, "description": "Unauthorized. The client must authenticate itself to get the requested response."},
        403: {"model": ErrorResponse, "description": "Forbidden. The client does not have access rights to the content."},
        404: {"model": ErrorResponse, "description": "Not Found. The server can not find the requested resource."},
        500: {"model": ErrorResponse, "description": "Internal Server Error. The server has encountered a situation it doesn&#39;t know how to handle."},
    },
    tags=["Category"],
    summary="Update a category",
    response_model_by_alias=True,
)
async def categories_category_id_put(
    categoryId: str = Path(..., description=""),
    category_update: CategoryUpdate = Body(None, description=""),
) -> Category:
    if not BaseCategoryApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCategoryApi.subclasses[0]().categories_category_id_put(categoryId, category_update)


@router.get(
    "/categories",
    responses={
        200: {"model": List[Category], "description": "List of categories retrieved successfully"},
        401: {"model": ErrorResponse, "description": "Unauthorized. The client must authenticate itself to get the requested response."},
        403: {"model": ErrorResponse, "description": "Forbidden. The client does not have access rights to the content."},
        500: {"model": ErrorResponse, "description": "Internal Server Error. The server has encountered a situation it doesn&#39;t know how to handle."},
    },
    tags=["Category"],
    summary="Get all categories",
    response_model_by_alias=True,
)
async def categories_get(
) -> List[Category]:
    if not BaseCategoryApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCategoryApi.subclasses[0]().categories_get()


@router.post(
    "/categories",
    responses={
        201: {"model": Category, "description": "Category created successfully"},
        401: {"model": ErrorResponse, "description": "Unauthorized. The client must authenticate itself to get the requested response."},
        403: {"model": ErrorResponse, "description": "Forbidden. The client does not have access rights to the content."},
        500: {"model": ErrorResponse, "description": "Internal Server Error. The server has encountered a situation it doesn&#39;t know how to handle."},
    },
    tags=["Category"],
    summary="Create a new category",
    response_model_by_alias=True,
)
async def categories_post(
    category_create: CategoryCreate = Body(None, description=""),
) -> Category:
    if not BaseCategoryApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCategoryApi.subclasses[0]().categories_post(category_create)
