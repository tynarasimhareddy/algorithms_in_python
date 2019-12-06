from collections import OrderedDict
  
class LRUCache(object):

    def __init__(self, capacity):
        self.size = capacity
        self.data = OrderedDict()

    def get(self, key):
        try:
            value = self.data.pop(key)
            self.data[key] = value
            return value
        except Exception as e:
            return -1


    def put(self, key, value):
        try:
            self.data.pop(key)
            self.data[key] = value
        except:
            if self.size == len(self.data):
                self.data.pop(self.data.keys()[0])
            self.data[key] = value

cache = LRUCache( 2)

cache.put(1, 1)
cache.put(2, 2)
assert(cache.get(1) == 1)       # returns 2
cache.put(3, 3)    # evicts key 2
assert(cache.get(2) == -1)       # returns -1 (not found)
cache.put(4, 4)    # evicts key 1
assert(cache.get(1) == -1)       # returns -1 (not found)
assert(cache.get(3) == 3)       # returns 3
assert(cache.get(4) == 4)      # returns 4
