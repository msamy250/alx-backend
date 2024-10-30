#!/usr/bin/python3
"""BasicCache that inherits from BaseCaching"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        """Assign the item value for the key in self.cache_data"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to key in self.cache_data"""
        return self.cache_data.get(key) if key is not None else None
