#!/usr/bin/env python3
"""A cache system module"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """An object that allows storing and receiving of items
    in the dictionary and also implements the FIFO algorithm"""
    def __init__(self):
        """Initializes the cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """A put method to assign items to the dictionary"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Get the keys in the dictionary"""
        return self.cache_data.get(key, None)
