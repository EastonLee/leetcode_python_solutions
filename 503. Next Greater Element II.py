import unittest

class Solution(object):
    def nextGreaterElements(self, nums):
        st, res = [], [-1]*len(nums)
        for idx, i in enumerate(nums*2):
            while st and (nums[st[-1]] < i):
                res[st.pop()] = i
            if idx < len(nums):
                st.append(idx)
        return res

if __name__ == '__main__':
    unittest.main()
