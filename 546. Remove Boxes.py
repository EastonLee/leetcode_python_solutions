import unittest


'''

'''
# Definition for a binary tree node.


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return 'value: {}'.format(self.val)

# https://discuss.leetcode.com/topic/84307/python-fast-dp-with-explanation
# by @awice
class Solution(object):
    def removeBoxes(self, A):
        """
        :type boxes: List[int]
        :rtype: int
        """
        N = len(A)
        memo = [[[0]*N for _ in xrange(N) ] for _ in xrange(N) ]
        
        def dp(i, j, k):
            if i > j: return 0
            if not memo[i][j][k]:
                m = i
                while m+1 <= j and A[m+1] == A[i]:
                    m += 1
                i, k = m, k + m - i
                ans = dp(i+1, j, 0) + (k+1) ** 2
                for m in xrange(i+1, j+1):
                    if A[i] == A[m]:
                        ans = max(ans, dp(i+1, m-1, 0) + dp(m, j, k+1))
                memo[i][j][k] = ans
            return memo[i][j][k]
        
        return dp(0, N-1, 0)


class Test(unittest.TestCase):

    def test(self):
        case = [1, 3, 2, 2, 2, 3, 4, 3, 1]
        assert Solution().removeBoxes(case) == 23
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

if __name__ == '__main__':
    unittest.main()
