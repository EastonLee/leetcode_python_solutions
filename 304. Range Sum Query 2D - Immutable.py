import unittest
from typing import List


class NumMatrix:

	def __init__(self, matrix: List[List[int]]):
		m = len(matrix)
		n = len(matrix[0])
		self.dp = [[0] * (n + 1) for i in range(m + 1)]

		for i in range(1, m + 1):
			for j in range(1, n + 1):
				self.dp[i][j] = matrix[i - 1][j - 1] + self.dp[i - 1][j] + self.dp[i][j - 1] - self.dp[i - 1][j - 1]

	def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
		return self.dp[row2 + 1][col2 + 1] - self.dp[row2 + 1][col1] - self.dp[row1][col2 + 1] + self.dp[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
class Test(unittest.TestCase):
	def test(self):
		m = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
		cases = [
			[[2, 1, 4, 3], 8],
			[[1, 1, 2, 2], 11],
			[[1, 2, 2, 4], 12],
		]
		s = NumMatrix(m)
		for ci, co in cases:
			result = s.sumRegion(*ci)
			assert result == co, (ci, co, result)

# cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')


if __name__ == '__main__':
	unittest.main(exit=False)
