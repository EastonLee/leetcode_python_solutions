import unittest

# https://codereview.stackexchange.com/questions/135661/lru-cache-in-python
# Make sure you know how OderedDict works.
# https://discuss.leetcode.com/topic/14591/python-dict-double-linkedlist
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        from collections import OrderedDict
        self.capacity = capacity
        self.cache = OrderedDict()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        v = self.cache.pop(key)
        self.cache[key] = v
        return v
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key] = value
        while len(self.cache) > self.capacity:
            self.cache.popitem(last=False)



class Test(unittest.TestCase):

    def test(self):
        cache = LRUCache( 2 )

        cache.put(1, 1)
        cache.put(2, 2)
        assert cache.get(1) == 1       # returns 1
        cache.put(3, 3)    # evicts key 2
        assert cache.get(2) == -1      # returns -1 (not found)
        cache.put(4, 4)    # evicts key 1
        assert cache.get(1) == -1      # returns -1 (not found)
        assert cache.get(3) == 3       # returns 3
        assert cache.get(4) == 4       # returns 4

if __name__ == '__main__':
    unittest.main()
