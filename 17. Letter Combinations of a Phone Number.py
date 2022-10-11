import unittest
from typing import *


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dial = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        ans = []
        for d in digits:
            if not ans:
                ans = list(dial[d])
            else:
                ans = [a + b for a in ans for b in dial[d]]
        return ans


class Test(unittest.TestCase):
    def test(self):
        cases = [
            ["23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]]
        ]
        for ci, co in cases:
            result = Solution().letterCombinations(ci)
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
