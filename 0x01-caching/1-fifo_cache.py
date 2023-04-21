#!/usr/bin/env python3

'''FIFO Caching'''

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''Implents deleting elements in cache based on FIFO algorithm'''
    data_keys = []

    def __init__(self):
        # grab the parent constructor method
        super().__init__()

    def put(self, key, item):
        '''adds items to the cache_data'''
        if key is not None and item is not None:
            num = len(self.cache_data)
            if num >= BaseCaching.MAX_ITEMS:
                fkey = next(iter(self.cache_data))
                del self.cache_data[fkey]
                print(f'DISCARD: {fkey}')
            self.cache_data[key] = item
            return item

    def get(self, key):
        """Fetch cache data"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
