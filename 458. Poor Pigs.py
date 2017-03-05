import unittest


class Solution(object):

    # https://discuss.leetcode.com/topic/67666/another-explanation-and-solution/2
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        pigs = 0
        while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs


class Test(unittest.TestCase):

    def test(self):
        assert Solution().poorPigs(1000, 15, 60) == 5
        #cProfile.runctx('Solution().calculate(case)', globals(), locals())

if __name__ == '__main__':
    unittest.main()
