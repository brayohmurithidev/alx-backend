#!/usr/bin/env python3

'''LIFO caching'''

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''Removes element that was last inserted'''
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''Inserts new element'''
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lkey, lItem = self.cache_data.popitem()
                print(f'DISCARD: {lkey}')
            self.cache_data[key] = item
            return item

    def get(self, key):
        '''Prints cached data'''
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
