import unittest


class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans = 1
        left, right = 0, 0
        for right in range(1, len(s)):
            # char is next char in alphabet
            if ord(s[right]) == ord(s[right - 1]) + 1:
                ans = max(ans, right - left + 1)
            else:
                left = right

        return ans


class Test(unittest.TestCase):
    def test(self):
        cases = [
            ["abacaba", 2],
            ["abcde", 5]
        ]
        for ci, co in cases:
            result = Solution().longestContinuousSubstring(ci)
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
