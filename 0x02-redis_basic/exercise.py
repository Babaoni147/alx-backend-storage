#!/usr/bin/env python3
"""Module declares a redis class and methods"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of calls to a method."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to count calls to a method."""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a method."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to store the history of inputs and outputs."""
        # Define Redis keys for storing inputs and outputs
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))

        result = method(self, *args, **kwargs)

        self._redis.rpush(output_key, str(result))

        return result
    return wrapper


def replay(fn: Callable):
    """display the history of calls of a particular function."""
    r = redis.Redis()
    func_name = fn.__qualname__
    c = r.get(func_name)
    try:
        c = int(c.decode("utf-8"))
    except Exception:
        c = 0
    print("{} was called {} times:".format(func_name, c))
    inputs = r.lrange("{}:inputs".format(func_name), 0, -1)
    outputs = r.lrange("{}:outputs".format(func_name), 0, -1)
    for inp, outp in zip(inputs, outputs):
        try:
            inp = inp.decode("utf-8")
        except Exception:
            inp = ""
        try:
            outp = outp.decode("utf-8")
        except Exception:
            outp = ""
        print("{}(*{}) -> {}".format(func_name, inp, outp))


class Cache:
    """Cache class to store data."""
    def __init__(self):
        """Constructor method."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in Redis and returns the generated key."""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes],
                                                  Any]] = None) -> Any:
        """Gets the value of a key from Redis."""
        value = self._redis.get(key)
        if value is None:
            return None
        return fn(value) if fn else value

    def get_str(self, key: str) -> Optional[str]:
        """Gets the value of a key from Redis as a string."""
        return self.get(key, lambda v: v.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """Gets the value of a key from Redis as an integer."""
        return self.get(key, int)
