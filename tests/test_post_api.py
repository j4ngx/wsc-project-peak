# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.error_response import ErrorResponse  # noqa: F401
from openapi_server.models.post_create import PostCreate  # noqa: F401
from openapi_server.models.post_list_paginated import PostListPaginated  # noqa: F401
from openapi_server.models.post_patch import PostPatch  # noqa: F401
from openapi_server.models.post_response import PostResponse  # noqa: F401
from openapi_server.models.post_update import PostUpdate  # noqa: F401


def test_posts_get(client: TestClient):
    """Test case for posts_get

    Get all posts or search for posts
    """
    params = [("title", 'title_example'),     ("author", 'author_example'),     ("visibility", 'visibility_example'),     ("limit", 56),     ("offset", 56)]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/posts",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_posts_post(client: TestClient):
    """Test case for posts_post

    Create a new post
    """
    post_create = {"created_at":"2024-10-06T12:00:00Z","images":[{"alt_text":"Person doing a squat","url":"https://example.com/images/squat.jpg"},{"alt_text":"Person doing a squat","url":"https://example.com/images/squat.jpg"}],"visibility":"draft","author":"Jane Doe","id":"9bdb5b16-4d3f-43cb-8f71-839b1e56b2d4","categories":[{"name":"Fitness","description":"Posts related to fitness and exercise routines.","id":"c1bfb8a0-3b84-4f43-949e-3a7f4f2a1e21"},{"name":"Fitness","description":"Posts related to fitness and exercise routines.","id":"c1bfb8a0-3b84-4f43-949e-3a7f4f2a1e21"}],"title":"How to do Squats","content":"\"# Squats \\n\nSquats are a fundamental exercise to build strength in your legs and glutes...\"\n","updated_at":"2024-10-06T12:05:00Z"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/posts",
    #    headers=headers,
    #    json=post_create,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_posts_post_id_delete(client: TestClient):
    """Test case for posts_post_id_delete

    Delete a post
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/posts/{postId}".format(postId='post_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_posts_post_id_get(client: TestClient):
    """Test case for posts_post_id_get

    Get a single post
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/posts/{postId}".format(postId='post_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_posts_post_id_patch(client: TestClient):
    """Test case for posts_post_id_patch

    Partially update a post
    """
    post_patch = {"created_at":"2024-10-06T12:00:00Z","images":[{"alt_text":"Person doing a squat","url":"https://example.com/images/squat.jpg"},{"alt_text":"Person doing a squat","url":"https://example.com/images/squat.jpg"}],"visibility":"draft","author":"Jane Doe","id":"9bdb5b16-4d3f-43cb-8f71-839b1e56b2d4","categories":[{"name":"Fitness","description":"Posts related to fitness and exercise routines.","id":"c1bfb8a0-3b84-4f43-949e-3a7f4f2a1e21"},{"name":"Fitness","description":"Posts related to fitness and exercise routines.","id":"c1bfb8a0-3b84-4f43-949e-3a7f4f2a1e21"}],"title":"How to do Squats","content":"\"# Squats \\n\nSquats are a fundamental exercise to build strength in your legs and glutes...\"\n","updated_at":"2024-10-06T12:05:00Z"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/posts/{postId}".format(postId='post_id_example'),
    #    headers=headers,
    #    json=post_patch,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_posts_post_id_put(client: TestClient):
    """Test case for posts_post_id_put

    Update a post
    """
    post_update = {"created_at":"2024-10-06T12:00:00Z","images":[{"alt_text":"Person doing a squat","url":"https://example.com/images/squat.jpg"},{"alt_text":"Person doing a squat","url":"https://example.com/images/squat.jpg"}],"visibility":"draft","author":"Jane Doe","id":"9bdb5b16-4d3f-43cb-8f71-839b1e56b2d4","categories":[{"name":"Fitness","description":"Posts related to fitness and exercise routines.","id":"c1bfb8a0-3b84-4f43-949e-3a7f4f2a1e21"},{"name":"Fitness","description":"Posts related to fitness and exercise routines.","id":"c1bfb8a0-3b84-4f43-949e-3a7f4f2a1e21"}],"title":"How to do Squats","content":"\"# Squats \\n\nSquats are a fundamental exercise to build strength in your legs and glutes...\"\n","updated_at":"2024-10-06T12:05:00Z"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/posts/{postId}".format(postId='post_id_example'),
    #    headers=headers,
    #    json=post_update,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

