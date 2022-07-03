import unittest
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        rest, ans, idx = truckSize, 0, 0
        while rest > 0 and idx < len(boxTypes):
            if boxTypes[idx][0] <= rest:
                rest -= boxTypes[idx][0]
                ans += boxTypes[idx][0] * boxTypes[idx][1]
                idx += 1
            else:
                ans += rest * boxTypes[idx][1]
                break
        return ans


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [([[1, 3], [2, 2], [3, 1]], 4), 8],
            [([[5, 10], [2, 5], [4, 7], [3, 9]], 10), 91],
            [([[1, 3], [5, 5], [2, 5], [4, 2], [4, 1], [3, 1], [2, 2], [1, 3], [2, 5], [3, 2]], 35), 76],
        ]
        for ci, co in cases:
            result = Solution().maximumUnits(*ci)
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
