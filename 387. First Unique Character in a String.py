import unittest
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i
        return -1


class Test(unittest.TestCase):
    def test(self):
        cases = [
            ["leetcode", 0],
            ["loveleetcode", 2],
            ["aabb", -1],
        ]
        for ci, co in cases:
            result = Solution().firstUniqChar(ci)
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
