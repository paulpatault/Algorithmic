"""
Implement an LFU (Least Frequently Used) cache. 
It should be able to be initialized with a cache size n, and contain the following methods:

• set(key, value): 
    Sets key to value. 
    If there are already n items in the cache and we are adding a new item, 
    then it should also remove the least frequently used item. 
    If there is a tie, then the least recently used key should be removed.
• get(key): 
    Gets the value at key. If no such key exists, return null.
"""
import sys


class LFUCache:
    def __init__(self, n):
        self.data = {}
        self.idx = 0
        self.n = n
        self.lower = None

    def set(self, key, value):
        if self.idx == self.n:
            self.data.pop(self.lower)
            self.data[key] = {"value": value, "usage": 0}
            self.lower = key
        else:
            self.idx += 1
            self.data[key] = {"value": value, "usage": 0}
            self.lower = key

    def get(self, key):
        try:
            self.data[key]["usage"] += 1
            self._changeLower()
            return self.data[key]
        except KeyError:
            return None

    def _changeLower(self):
        min = sys.maxsize
        for key, value in self.data.items():
            if value["usage"] < min:
                min = value["usage"]
                self.lower = key

    def __str__(self):
        return str(self.data)


cache = LFUCache(3)
cache.set(1, 1)
cache.set(2, 2)
cache.set(3, 3)
cache.get(1)
cache.get(1)
cache.get(3)
cache.set(4, 4)

# should remove the "2" value as it is never used
print(cache)
