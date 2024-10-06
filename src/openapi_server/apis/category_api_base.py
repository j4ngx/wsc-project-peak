# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.category import Category
from openapi_server.models.category_create import CategoryCreate
from openapi_server.models.category_update import CategoryUpdate
from openapi_server.models.error_response import ErrorResponse


class BaseCategoryApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseCategoryApi.subclasses = BaseCategoryApi.subclasses + (cls,)
    async def categories_category_id_delete(
        self,
        categoryId: str,
    ) -> None:
        ...


    async def categories_category_id_get(
        self,
        categoryId: str,
    ) -> Category:
        ...


    async def categories_category_id_put(
        self,
        categoryId: str,
        category_update: CategoryUpdate,
    ) -> Category:
        ...


    async def categories_get(
        self,
    ) -> List[Category]:
        ...


    async def categories_post(
        self,
        category_create: CategoryCreate,
    ) -> Category:
        ...
