import unittest
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        m = {}
        for w in words:
            chars = 0
            for l in w:
                chars |= 1 << ord(l) - ord('a')
            m[chars] = max(m.get(chars, 0), len(w))
        return max([m[x] * m[y] for x in m for y in m if not x & y] or [0])


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [["abcw", "baz", "foo", "bar", "xtfn", "abcdef"], 16],
            [["a", "ab", "abc", "d", "cd", "bcd", "abcd"], 4],
            [["a", "aa", "aaa", "aaaa"], 0]
        ]
        for ci, co in cases:
            result = Solution().maxProduct(ci)
            assert result == co, (ci, co, result)
        # cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')


if __name__ == '__main__':
    unittest.main(exit=False)
