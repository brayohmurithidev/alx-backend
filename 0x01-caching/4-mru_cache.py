#!/usr/bin/python3
"""
MRU caching module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRU cache class
    """

    def __init__(self):
        """
        Initialize MRU cache
        """
        super().__init__()
        self.mru_keys = []

    def put(self, key, item):
        """
        Add an item in the cache using MRU algorithm
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                mru_key = self.mru_keys.pop()
                del self.cache_data[mru_key]
                print("DISCARD:", mru_key)

        self.cache_data[key] = item
        if key in self.mru_keys:
            self.mru_keys.remove(key)
        self.mru_keys.append(key)

    def get(self, key):
        """
        Get an item from the cache using MRU algorithm
        """
        if key is None or key not in self.cache_data:
            return None

        if key in self.mru_keys:
            self.mru_keys.remove(key)
        self.mru_keys.append(key)

        return self.cache_data[key]
