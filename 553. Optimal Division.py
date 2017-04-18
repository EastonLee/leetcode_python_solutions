import unittest


class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = map(str, nums)
        if len(nums) <= 2: return '/'.join(nums)
        return '{}/({})'.format(nums[0], nums[1:])



class Test(unittest.TestCase):

    def test(self):
        case = [1000,100,10,2]
        assert Solution().optimalDivision(case) == "1000/(100/10/2)"
        case = [2]
        assert Solution().optimalDivision(case) == "2"
        case = [3,2]
        assert Solution().optimalDivision(case) == "3/2"


if __name__ == '__main__':
    unittest.main()
