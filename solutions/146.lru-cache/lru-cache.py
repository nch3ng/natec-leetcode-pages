from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()
        self.tm = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return self.cache[key]
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # print("Put key {}:value {} into cache, len = {}".format(key, value, len(self.cache)))
        if key not in self.cache:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        else:
            self.cache.pop(key, None)
 
        self.cache[key] = value
