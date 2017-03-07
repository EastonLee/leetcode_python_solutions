import unittest


class Solution(object):

    def lengthOfLIS(self, nums):
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
            print tailing_longest
        return length and len(max(tailing_longest, key=len))

    # https://discuss.leetcode.com/topic/28738/java-python-binary-search-o-nlogn-time-with-explanation/8
    # by dietpepsi
    def lengthOfLIS(self, nums):
        if not nums: return 0
        tails = [nums[0]]
        for i in nums:
            if i > tails[-1]:
                tails.append(i)
                continue
            l, r, m = 0, len(tails) - 1, 0
            while l < r :
                m = (l+r) / 2
                if tails[m] < i:
                    l = m + 1
                else:
                    r = m
            tails[l] = i
        return len(tails) 


class Test(unittest.TestCase):

    def test(self):
        assert Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
        assert Solution().lengthOfLIS([]) == 0
        assert Solution().lengthOfLIS([3,2,1]) == 1
        assert Solution().lengthOfLIS([2,2]) == 1
        assert Solution().lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6
        #cProfile.runctx('Solution().calculate(case)', globals(), locals())

if __name__ == '__main__':
    unittest.main()
