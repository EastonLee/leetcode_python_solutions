import unittest
from typing import List


class Solution(object):
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)
        size = 0
        for num in nums:
            l, r = 0, size
            while l != r:
                m = (l + r) // 2
                if tails[m] < num:
                    l = m + 1
                else:
                    r = m
            tails[l] = num
            size = max(l + 1, size)
        return size

    # this method knows what the longest increasing subsequence is
    def lengthOfLIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        tailing_longest = [nums[:1]] * length
        for i in range(1, length):
            increasing_seq = [
                j for j in tailing_longest[:i] if j[-1] < nums[i]]
            tailing_longest[i] = max(
                increasing_seq, key=len) + nums[i:i + 1] if increasing_seq else nums[i:i + 1]
            print(tailing_longest)
        return length and len(max(tailing_longest, key=len))

    # https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
    # by dietpepsi
    def lengthOfLIS3(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size


class Test(unittest.TestCase):

    def test(self):
        assert Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
        assert Solution().lengthOfLIS([]) == 0
        assert Solution().lengthOfLIS([3, 2, 1]) == 1
        assert Solution().lengthOfLIS([2, 2]) == 1
        assert Solution().lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6
        # cProfile.runctx('Solution().calculate(case)', globals(), locals())


if __name__ == '__main__':
    unittest.main()
