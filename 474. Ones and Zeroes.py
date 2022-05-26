import collections
import unittest
from typing import List


class Solution:
	def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
		dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs) + 1)]
		for i in range(1, len(strs)+1):
			s = strs[i-1]
			zeros, ones = s.count('0'), s.count('1')
			for j in range(m+1):
				for k in range(n+1):
					if j >= zeros and k >= ones:
						dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-zeros][k-ones] + 1)
					else:
						dp[i][j][k] = dp[i-1][j][k]
		return dp[-1][-1][-1]


class Test(unittest.TestCase):
	def test(self):
		cases = [
			[(["10", "0001", "111001", "1", "0"], 5, 3), 4],
			[(["10", "0", "1"], 1, 1), 2],
		]
		for ci, co in cases:
			result = Solution().findMaxForm(*ci)
			assert result == co, (ci, co, result)

# cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')


if __name__ == '__main__':
	unittest.main(exit=False)


# by https://leetcode.com/licaiuu
class Solution2(object):
	def findMaxForm(self, S, m, n):
		S = [collections.Counter(s) for s in S]
		S = [[s['0'], s['1']] for s in S]
		dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len(S) + 1)]
		for i in range(1, len(S) + 1):
			zero, one = S[i - 1]
			for j in range(0, m + 1):
				for k in range(0, n + 1):
					if j >= zero and k >= one:
						dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - zero][k - one] + 1)
					else:
						dp[i][j][k] = dp[i - 1][j][k]
		return dp[i][j][k]

	def findMaxForm_space_saving(self, S, m, n):
		S = [collections.Counter(s) for s in S]
		S = [[s['0'], s['1']] for s in S]
		dp = [[0] * (n + 1) for _ in range(m + 1)]
		for i in range(1, len(S) + 1):
			zero, one = S[i - 1]
			for j in range(m, -1, -1):
				for k in range(n, -1, -1):
					if j >= zero and k >= one:
						dp[j][k] = max(dp[j][k], dp[j - zero][k - one] + 1)
					else:
						dp[j][k] = dp[j][k]
		return dp[m][n]
