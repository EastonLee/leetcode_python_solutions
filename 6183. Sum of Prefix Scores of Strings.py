import unittest
from typing import List


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # get prefix map
        prefix_map = {}
        for word in words:
            prefix = ""
            for c in word:
                prefix += c
                if prefix in prefix_map:
                    prefix_map[prefix] += 1
                else:
                    prefix_map[prefix] = 1

        ans = []
        for word in words:
            score = 0
            prefix = ""
            for c in word:
                prefix += c
                score += prefix_map[prefix]
            ans.append(score)
        return ans


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [["abc", "ab", "bc", "b"], [5, 4, 3, 2]],
            [["abcd"], [4]],
        ]
        for ci, co in cases:
            result = Solution().sumPrefixScores(ci)
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
