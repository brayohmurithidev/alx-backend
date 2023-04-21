#!/usr/bin/python3
"""Defines the LFUCache class"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU caching"""

    def __init__(self):
        """Initialize class instance"""
        super().__init__()
        self.queue = []
        self.counter = {}

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        item_count = self.counter.get(key, None)

        if item_count is not None:
            self.counter[key] += 1
        else:
            self.counter[key] = 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = self.get_first_list(self.queue)
            if first:
                self.queue.pop(0)
                del self.cache_data[first]
                del self.counter[first]
                print("DISCARD: {}".format(first))

        if key not in self.queue:
            self.queue.insert(0, key)
        self.move_to_right(key)

    def get(self, key):
        """Return the value of a given key from the cache"""
        item = self.cache_data.get(key, None)
        if item is not None:
            self.counter[key] += 1
            self.move_to_right(key)
        return item

    def move_to_right(self, item):
        """Move element to the right, taking into account LFU"""
        length = len(self.queue)

        idx = self.queue.index(item)
        item_count = self.counter[item]

        for i in range(idx, length):
            if i != (length - 1):
                nxt = self.queue[i + 1]
                nxt_count = self.counter[nxt]

                if nxt_count > item_count:
                    break

        self.queue.insert(i + 1, item)
        self.queue.remove(item)

    @staticmethod
    def get_first_list(array):
        """Return the first element of a list or None"""
        return array[0] if array else None
