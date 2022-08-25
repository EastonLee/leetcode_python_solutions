import unittest
from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def util(s: str, k: int):
            cnt = Counter(s)
            invalid = list(filter(lambda x: cnt[x] < k, cnt.keys()))
            if len(invalid) == 0:
                return len(s)
            split = s.split(invalid[0], 1)
            if len(split) == 0:
                return 0
            if len(split) == 1:
                return util(split[0], k)
            if len(split) == 2:
                return max(util(split[0], k), util(split[1], k))

        return util(s, k)


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [("aaabb", 3), 3],
            [("ababbc", 2), 5],
        ]
        for ci, co in cases:
            result = Solution().longestSubstring(ci[0], ci[1])
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
