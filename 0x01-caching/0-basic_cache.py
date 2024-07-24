#!/usr/bin/env python3
"""basic caching modules"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class that inherits from the BaseCaching class
    and it a cache sytem"""

    def put(self, key, item):
        """a method to assign item value for the key
        If key or item is None, this method should not do anything."""

        if key is not None and item  is not None:
            return self.cache_data[key] = item

    def get(self, key):
        """ returned the assign itemm """
        return self.cache_data.get(key, none)
