#!/usr/bin/env python3

'''LRU Caching'''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class that inherits from BaseCaching """

    def __init__(self):
        """ Initialize LRUCache """
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # If key already exists in cache, update its value
            self.key_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # If cache is full, remove the least recently used item
            lru_key = self.key_order.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

        self.key_order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        # Move key to end of key_order list to mark it as recently used
        self.key_order.remove(key)
        self.key_order.append(key)

        return self.cache_data[key]
