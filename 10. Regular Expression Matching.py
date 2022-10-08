import unittest


# I don't fully understand this solution.
# https://leetcode.com/problems/regular-expression-matching/
class Solution(object):
    def isMatch(self, text, pattern):
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j + 1 < len(pattern) and pattern[j + 1] == '*':
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)


class Test(unittest.TestCase):
    def test(self):
        cases = [
            # [["123", "123"], True],
            # [["123", "1.3"], True],
            # [["123", "1.3."], False],
            # [["123", "1.3.4"], False],
            [["123", "1.3*"], True],
        ]
        for ci, co in cases:
            result = Solution().isMatch(ci[0], ci[1])
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
