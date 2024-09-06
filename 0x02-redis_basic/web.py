#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""
import requests
import redis
from functools import wraps
from typing import Callable


# Initialize Redis connection (include decode_responses for convenience)
_redis = redis.Redis(decode_responses=True)


def count_request(method: Callable) -> Callable:
    """Decorator that counts the number of requests sent to a URL."""

    @wraps(method)
    def wrapper(url):
        """Wrapper function to track requests and cache the result."""
        # Keys for request count and cached response
        count_key = f"count:{url}"
        cache_key = f"cached:{url}"

        # Increment request count for this URL
        _redis.incr(count_key)

        # Check if response is cached
        cached_response = _redis.get(cache_key)
        if cached_response:
            return cached_response

        # If not cached, fetch from the URL and cache the result
        html = method(url)
        _redis.setex(cache_key, 10, html)  # Cache expires in 10 seconds
        return html

    return wrapper


@count_request
def get_page(url: str) -> str:
    """Fetch the HTML content of a given URL."""
    response = requests.get(url)
    return response.text
