import unittest


# https://codereview.stackexchange.com/questions/135661/lru-cache-in-python
# Make sure you know how OderedDict works.
# https://discuss.leetcode.com/topic/14591/python-dict-double-linkedlist
class LRUCache2(object):

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


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.history = []
        self.d = {}

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        v = self.d.get(key)
        self.history.remove(key)
        self.history.append(key)
        return v

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.history.remove(key)
        self.history.append(key)
        self.d[key] = value
        if len(self.history) > self.capacity:
            k = self.history.pop(0)
            del self.d[k]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class Test(unittest.TestCase):

    def test1(self):
        cache = LRUCache(2)

        cache.put(1, 1)
        cache.put(2, 2)
        assert cache.get(1) == 1  # returns 1
        cache.put(3, 3)  # evicts key 2
        assert cache.get(2) == -1  # returns -1 (not found)
        cache.put(4, 4)  # evicts key 1
        assert cache.get(1) == -1  # returns -1 (not found)
        assert cache.get(3) == 3  # returns 3
        assert cache.get(4) == 4  # returns 4

    def test2(self):
        cache = LRUCache(2)
        assert cache.get(2) == -1
        cache.put(2, 6)
        assert cache.get(1) == -1
        cache.put(1, 5)
        cache.put(1, 2)
        assert cache.get(1) == 2
        assert cache.get(2) == 6

    def test3(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        assert cache.get(1) == 1
        cache.put(3, 3)
        assert cache.get(2) == -1
        cache.put(4, 4)
        assert cache.get(1) == -1
        assert cache.get(3) == 3
        assert cache.get(4) == 4

    def test4(self):
        cache = LRUCache(2)
        cache.put(2, 1)
        cache.put(1, 1)
        cache.put(2, 3)
        cache.put(4, 1)
        assert cache.get(1) == -1
        assert cache.get(2) == 3


if __name__ == '__main__':
    unittest.main()
