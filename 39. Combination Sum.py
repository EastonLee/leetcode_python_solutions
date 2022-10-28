import unittest
from typing import *


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.dfs(candidates, target, 0, [], ans)
        return ans

    def dfs(self, candidates, target, index, path, ans):
        if target == 0:
            ans.append(path)
            return
        if target < 0:
            return
        for i in range(index, len(candidates)):
            self.dfs(candidates, target - candidates[i], i, path + [candidates[i]], ans)


class Test(unittest.TestCase):
    def test(self):
        cases = [
            ["1+7-(7+3+3)+6-3+1", -1]
        ]
        for ci, co in cases:
            result = Solution().calculate(ci)
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
