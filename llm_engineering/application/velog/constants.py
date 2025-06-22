V3_URL = "https://v3.velog.io/graphql"
V2_URL = "https://v2.velog.io/graphql"

POSTS_QUERY = """
query velogPosts($input: GetPostsInput!) {
    posts(input: $input) {
        id
        title
        short_description
        thumbnail
        url_slug
        released_at
        updated_at
    }
}
""".strip()

GET_POST_QUERY = """
query GetPost($id: ID) {
    post(id: $id) {
        id
        title
        body
        short_description
        thumbnail
        url_slug
        released_at
        updated_at
    }
}
""".strip()
