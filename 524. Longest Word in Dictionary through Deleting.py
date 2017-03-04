import unittest
class Solution(object):

    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def str_in_str(a, b):
            for i in a:
                idx = b.find(i)
                if idx == -1:
                    return False
                a = a[1:]
                b = b[idx + 1:]
            if not a:
                return True
            return False
        d.sort(key=lambda x:-len(x))
        for i in d:
            if str_in_str(i, s):
                return i
        return ''

    # https://discuss.leetcode.com/topic/80887/short-python-solutions/2
    # by StefanPochmann  
    def xxfindLongestWord(self, s, d):
        import heapq
        heap = [(-len(word), word) for word in d]
        heapq.heapify(heap)
        while heap:
            word = heapq.heappop(heap)[1]
            it = iter(s)
            if all(c in it for c in word):
                return word
        return ''

    def xxfindLongestWord(self, s, d):
        from itertools import ifilter
        def isSubsequence(x):
            it = iter(s)
            return all(c in it for c in x)
        d.sort(key=lambda x: (-len(x), x))
        return next(ifilter(isSubsequence, d), '')

class Test(unittest.TestCase):

    def test(self):
        s = "abpcplea"
        d = ["ale", "apple", "monkey", "plea"]
        assert Solution().findLongestWord(s, d) == 'apple'
        s = "abpcplea"
        d = ["x", "y", "z"]
        assert Solution().findLongestWord(s, d) == ''

if __name__ == '__main__':
    unittest.main()
