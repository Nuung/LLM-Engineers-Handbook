from __future__ import annotations

from typing import Any, Optional

import requests
from loguru import logger

from .constants import GET_POST_QUERY, POSTS_QUERY, V2_URL, V3_URL


class VelogService:
    """Simple client for the Velog GraphQL API."""

    def __init__(self, access_token: str, refresh_token: str) -> None:
        self.access_token = access_token
        self.refresh_token = refresh_token

    def _headers(self) -> dict[str, str]:
        if not self.access_token or not self.refresh_token:
            raise ValueError("Velog tokens are missing")

        return {
            "origin": "https://velog.io",
            "content-type": "application/json",
            "cookie": f"access_token={self.access_token}; refresh_token={self.refresh_token}",
        }

    def _execute_query(
        self, url: str, query: str, variables: Optional[dict[str, Any]] = None, operation_name: str | None = None
    ) -> dict[str, Any]:
        payload: dict[str, Any] = {"query": query}
        if variables:
            payload["variables"] = variables
        if operation_name:
            payload["operationName"] = operation_name

        response = requests.post(url, json=payload, headers=self._headers(), timeout=10)
        response.raise_for_status()
        result = response.json()
        return result.get("data", {})

    def get_posts(self, username: str, cursor: str = "", limit: int = 50) -> list[dict[str, Any]]:
        variables = {"input": {"username": username, "cursor": cursor, "limit": limit}}
        data = self._execute_query(V3_URL, POSTS_QUERY, variables)
        return data.get("posts", [])

    def get_post(self, post_id: str) -> dict[str, Any]:
        variables = {"id": post_id}
        data = self._execute_query(V2_URL, GET_POST_QUERY, variables)
        return data.get("post", {})

    def get_all_posts(self, username: str) -> list[dict[str, Any]]:
        cursor = ""
        posts: list[dict[str, Any]] = []
        while True:
            batch = self.get_posts(username=username, cursor=cursor)
            if not batch:
                break
            posts.extend(batch)
            cursor = batch[-1]["id"]

        detailed_posts = []
        for post in posts:
            try:
                detailed = self.get_post(post["id"])
            except Exception as exc:
                logger.error(f"Failed to fetch post details: {exc!s}")
                detailed = post
            detailed_posts.append(detailed)
        return detailed_posts
