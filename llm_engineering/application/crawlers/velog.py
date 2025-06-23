from __future__ import annotations

import re
from urllib.parse import urlparse

from loguru import logger

from llm_engineering.application.velog import VelogService
from llm_engineering.domain.documents import PostDocument

from .base import BaseSeleniumCrawler


class VelogCrawler(BaseSeleniumCrawler):
    """Crawler for Velog posts using the public GraphQL API."""

    model = PostDocument

    def extract(self, link: str, **kwargs) -> list[str]:
        """Fetch all posts from a Velog user page.

        Args:
            link: A link to a Velog profile, e.g. ``https://velog.io/@username``.
            **kwargs: Additional arguments. Requires ``user`` pointing to a
                :class:`~llm_engineering.domain.documents.UserDocument`.
        """
        logger.info(f"Starting Velog scrape for {link}")

        username = self._parse_username(link)
        service = VelogService()
        posts = service.get_all_posts(username)

        user = kwargs["user"]
        post_ids: list[str] = []
        for post in posts:
            doc = PostDocument(
                content={
                    "title": post.get("title", ""),
                    "short_description": post.get("short_description", ""),
                    "body": post.get("body", ""),
                },
                image=post.get("thumbnail"),
                link=f"https://velog.io/@{username}/{post.get('url_slug')}",
                platform="velog",
                author_id=user.id,
                author_full_name=user.full_name,
            )
            saved = doc.save()
            if saved:
                post_ids.append(str(doc.id))

        logger.info(f"Finished Velog scrape for {link}")

        return post_ids

    def _parse_username(self, link: str) -> str:
        parsed = urlparse(link)
        path = parsed.path
        match = re.search(r"@([^/]+)", path)
        if not match:
            raise ValueError(f"Invalid Velog link: {link}")
        return match.group(1)
