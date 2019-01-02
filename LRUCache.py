#Imports
#Class def
# method def
# getters / setters
#

#imports - Not sure what I'll need yet, typically I/O, datetime or data structures
import collections

#Class Defs


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.tm = 0
        self.cache = {}
        self.lru = {}

    def get(self, key):
        try:
            if key in self.cache:
                self.lru[key] = self.tm
                self.tm += 1
                return self.cache[key]
        except:
            print("Key not in Cache")
            return -1

    def set(self, key, value):
        if len(self.cache) >= self.capacity:
            old_key = min(self.lru.keys(), key=lambda k: self.lru[k])
            self.cache.pop(old_key)
            self.lru.pop(old_key)
        self.cache[key] = value
        self.lru[key]=self.tm
        self.tm += 1



