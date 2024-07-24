#!/usr/bin/env python3
""" a cache system module"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """an object that allows storing and receiving of items
    in the dictionary and also implement the fifo algorithm"""
    def __init__(self):
        """initializes the cach"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ a put method to assign items to the dictionary"""
        if key is not None and item is not None:
            return
        self.cache_data[key] = item
        if (len.self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """get the keys in the dictionary"""
        return self.cache_data.get(key, None)
