import unittest
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0] * len(triangle) for _ in triangle]
        for i, row in enumerate(triangle):
            for j, col in enumerate(row):
                if i == 0:
                    dp[i][j] = col
                    if j > 1:
                        continue
                else:
                    if j == 0:
                        dp[i][j] = dp[i - 1][j] + col
                    elif j == i:
                        dp[i][j] = dp[i - 1][j - 1] + col
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + col
        return min(dp[-1])


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11],
            [[[-10]], -10],
        ]
        for ci, co in cases:
            result = Solution().minimumTotal(ci)
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
