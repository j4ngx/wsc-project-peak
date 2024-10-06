# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.category import Category  # noqa: F401
from openapi_server.models.category_create import CategoryCreate  # noqa: F401
from openapi_server.models.category_update import CategoryUpdate  # noqa: F401
from openapi_server.models.error_response import ErrorResponse  # noqa: F401


def test_categories_category_id_delete(client: TestClient):
    """Test case for categories_category_id_delete

    Delete a category
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/categories/{categoryId}".format(categoryId='category_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_categories_category_id_get(client: TestClient):
    """Test case for categories_category_id_get

    Get a single category
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/categories/{categoryId}".format(categoryId='category_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_categories_category_id_put(client: TestClient):
    """Test case for categories_category_id_put

    Update a category
    """
    category_update = {"name":"Fitness","description":"Posts related to fitness and exercise routines.","id":"c1bfb8a0-3b84-4f43-949e-3a7f4f2a1e21"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/categories/{categoryId}".format(categoryId='category_id_example'),
    #    headers=headers,
    #    json=category_update,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_categories_get(client: TestClient):
    """Test case for categories_get

    Get all categories
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/categories",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_categories_post(client: TestClient):
    """Test case for categories_post

    Create a new category
    """
    category_create = {"name":"Fitness","description":"Posts related to fitness and exercise routines.","id":"c1bfb8a0-3b84-4f43-949e-3a7f4f2a1e21"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/categories",
    #    headers=headers,
    #    json=category_create,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

