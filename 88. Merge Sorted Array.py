import unittest
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return
        # nums1 = nums1[:m]
        for i in range(len(nums1) - m):
            nums1.pop()
        i = j = 0
        while True:
            if i == len(nums1) or nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                j += 1
                if j == n:
                    break
            i += 1


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [dict(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3), [1, 2, 2, 3, 5, 6]],
            [dict(nums1=[1], m=1, nums2=[], n=0), [1]]
        ]
        for ci, co in cases:
            nums1, m, nums2, n = ci["nums1"], ci["m"], ci["nums2"], ci["n"]
            Solution().merge(nums1, m, nums2, n)
            assert nums1 == co, (ci, co, nums1)


if __name__ == '__main__':
    unittest.main(exit=False)
