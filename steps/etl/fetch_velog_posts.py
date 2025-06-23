from __future__ import annotations

from loguru import logger
from typing_extensions import Annotated
from zenml import get_step_context, step

from llm_engineering.application.crawlers.velog import VelogCrawler
from llm_engineering.domain.documents import UserDocument


@step
def fetch_velog_posts(
    user: Annotated[UserDocument, "user"],
    velog_username: str,
) -> Annotated[list[str], "post_ids"]:
    logger.info(f"Fetching Velog posts for {velog_username}")
    crawler = VelogCrawler()
    profile_link = f"https://velog.io/@{velog_username}"
    post_ids = crawler.extract(profile_link, user=user)
    step_context = get_step_context()
    step_context.add_output_metadata(
        output_name="post_ids", metadata={"num_posts": len(post_ids)}
    )
    return post_ids
