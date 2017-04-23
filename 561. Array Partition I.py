import unittest
from pprint import pprint
import re
import cProfile
import heapq
import collections
import itertools
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[::2])


class Test(unittest.TestCase):

    def test(self):
        case = [1,2,3,4]
        assert Solution().arrayPairSum(case) == 4
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

if __name__ == '__main__':
    unittest.main()
