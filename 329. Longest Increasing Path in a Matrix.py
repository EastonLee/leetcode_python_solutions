import unittest



class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.r_no = len(matrix)
        if self.r_no == 0: return 0
        self.c_no = len(matrix[0])
        memo = {}
        def helper(pos):
            x, y = pos
            if (x,y) in memo:
                return memo[(x,y)]
            neibs = [[x+i, y+j] for i, j in [[-1,0], [0,-1],[0,1],[1,0]] if 0<=x+i<self.r_no and 0<=y+j<self.c_no and (i or j)]
            larger_neibs = [[i,j] for i, j in neibs if matrix[i][j]>matrix[x][y]]
            if not larger_neibs:
                memo[(x,y)] = 1
                return 1
            rst = max(map(helper, larger_neibs)) + 1
            memo[(x,y)] = rst
            return rst
        return max(map(helper, [[i,j] for i in range(self.r_no) for j in range(self.c_no)]))

        


class Test(unittest.TestCase):

    def test(self):
        nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]

        assert Solution().longestIncreasingPath(nums) == 4
        nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
        assert Solution().longestIncreasingPath(nums) == 4
        #cProfile.runctx('Solution().calculate(case)', globals(), locals())

if __name__ == '__main__':
    unittest.main()
