from zenml import pipeline

from steps.etl import fetch_velog_posts, get_or_create_user


@pipeline
def velog_data_etl(
    user_full_name: str,
    velog_username: str,
    access_token: str,
    refresh_token: str,
) -> str:
    user = get_or_create_user(user_full_name)
    last_step = fetch_velog_posts(
        user=user,
        velog_username=velog_username,
        access_token=access_token,
        refresh_token=refresh_token,
    )

    return last_step.invocation_id
