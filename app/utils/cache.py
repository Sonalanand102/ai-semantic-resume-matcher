import hashlib
import json

from app.utils.redis_client import redis_client


def generate_cache_key(text: str):

    return hashlib.sha256(
        text.encode()
    ).hexdigest()


def get_cached_embedding(text: str):

    key = generate_cache_key(text)

    cached_value = redis_client.get(key)

    if cached_value:

        return json.loads(cached_value)

    return None


def set_cached_embedding(
    text: str,
    embedding
):

    key = generate_cache_key(text)

    redis_client.set(
        key,
        json.dumps(embedding)
    )