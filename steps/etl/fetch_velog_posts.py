from __future__ import annotations

from loguru import logger
from typing_extensions import Annotated
from zenml import get_step_context, step

from llm_engineering.application.velog import VelogService
from llm_engineering.domain.documents import PostDocument, UserDocument


@step
def fetch_velog_posts(
    user: Annotated[UserDocument, "user"],
    velog_username: str,
    access_token: str,
    refresh_token: str,
) -> Annotated[list[str], "post_ids"]:
    logger.info(f"Fetching Velog posts for {velog_username}")
    service = VelogService(access_token=access_token, refresh_token=refresh_token)
    posts = service.get_all_posts(velog_username)
    post_ids: list[str] = []
    for post in posts:
        doc = PostDocument(
            content={
                "title": post.get("title", ""),
                "short_description": post.get("short_description", ""),
                "body": post.get("body", ""),
            },
            image=post.get("thumbnail"),
            link=f"https://velog.io/@{velog_username}/{post.get('url_slug')}",
            platform="velog",
            author_id=user.id,
            author_full_name=user.full_name,
        )
        saved = doc.save()
        if saved:
            post_ids.append(str(doc.id))

    step_context = get_step_context()
    step_context.add_output_metadata(
        output_name="post_ids", metadata={"num_posts": len(post_ids)}
    )
    return post_ids
