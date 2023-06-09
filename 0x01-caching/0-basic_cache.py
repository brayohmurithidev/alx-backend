#!/usr/bin/env python3

'''
Basic Dictionary
'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    The class puts into a dictionary created in the parent
    class and outputs it
    """

    def put(self, key, item):
        """
        Update cache data
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            return item

    def get(self, key):
        """Fetch cache data"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
