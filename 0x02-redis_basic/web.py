#!/usr/bin/env python3
'''The module-level Redis instance.
'''
import requests
import redis
from functools import wraps
from time import time
from typing import Optional

redis_store = redis.Redis()

# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)


def cache_result(ttl: int = 10):
    """Decorator to cache the result of a function."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Generate cache key
            cache_key = f"{func.__name__}:{args[0]}"

            # Get cached result
            cached_result = redis_client.get(cache_key)
            if cached_result:
                return cached_result.decode('utf-8')

            # Execute function and cache result
            result = func(*args, **kwargs)
            redis_client.set(cache_key, result, ex=ttl)

            # Update access count
            count_key = f"count:{args[0]}"
            redis_client.incr(count_key, 1)

            return result
        return wrapper
    return decorator


@cache_result(ttl=10)
def get_page(url: str) -> Optional[str]:
    """Fetch HTML content of a URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None


def get_access_count(url: str) -> int:
    """Get access count for a URL."""
    count_key = f"count:{url}"
    return int(redis_client.get(count_key) or 0)
