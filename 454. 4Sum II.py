import unittest
from collections import Counter, defaultdict
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        c1, c2, c3, c4 = Counter(nums1), Counter(nums2), Counter(nums3), Counter(nums4)
        sum1, sum2 = defaultdict(list), defaultdict(list)
        for n1 in c1.keys():
            for n2 in c2.keys():
                sum1[n1 + n2].append((n1, n2))
        for n3 in c3.keys():
            for n4 in c4.keys():
                sum2[n3 + n4].append((n3, n4))

        ans = 0
        for k, pairs in sum1.items():
            if -k not in sum2:
                continue
            tmp1 = tmp2 = 0
            for pair in pairs:
                n1, n2 = pair
                tmp1 += c1[n1] * c2[n2]
            for pair in sum2[-k]:
                n3, n4 = pair
                tmp2 += c3[n3] * c4[n4]
            ans += tmp1 * tmp2

        return ans


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [[[1, 2], [-2, -1], [-1, 2], [0, 2]], 2],
            [[[0], [0], [0], [0]], 1],
            [[[-1, -1], [-1, 1], [-1, 1], [1, -1]], 6],
        ]
        for ci, co in cases:
            result = Solution().fourSumCount(ci[0], ci[1], ci[2], ci[3])
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
