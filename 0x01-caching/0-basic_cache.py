#!/usr/bin/env python3

'''
Basic Dictionary
'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Basic dict class
    """
    def __init__(self):
        super().__init__()   # call the parents init to initialize cachedata

    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
