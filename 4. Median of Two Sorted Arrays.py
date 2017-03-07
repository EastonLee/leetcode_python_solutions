import unittest


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return 'value: {}'.format(self.val)


class Solution(object):

    # https://discuss.leetcode.com/topic/6947/intuitive-python-o-log-m-n-solution-by-kth-smallest-in-the-two-sorted-arrays-252ms/9
    # ChuntaoLu
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.

    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2, len(b) // 2
        ma, mb = a[ia], b[ib]

        # when k is bigger than the sum of a and b's median indices
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include
            # k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include
            # k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)

    # https://discuss.leetcode.com/topic/16797/very-concise-o-log-min-m-n-iterative-solution-with-detailed-explanation/2
    # stellari
    # here auxiliary imaginary arrays are employed
    def findMedianSortedArrays(self, nums1, nums2):
        N1, N2 = len(nums1), len(nums2)
        if N1 < N2:
            nums1, N1, nums2, N2 = nums2, N2, nums1, N1
        l, r = 0, N2 * 2
        while l <= r:
            j = (l + r) / 2
            i = N1 + N2 - j
            L1 = float('-inf') if i == 0 else nums1[(i - 1) >> 1]
            L2 = float('-inf') if j == 0 else nums2[(j - 1) >> 1]
            R1 = float('inf') if i == 2 * N1 else nums1[i >> 1]
            R2 = float('inf') if j == 2 * N2 else nums2[j >> 1]
            if L1 > R2:
                l = j + 1
            elif L2 > R1:
                r = j - 1
            else:
                return (max(L1, L2) + min(R1, R2)) / 2.0


class Test(unittest.TestCase):

    def test(self):
        nums1 = [1, 3]
        nums2 = [2]
        assert Solution().findMedianSortedArrays(nums1, nums2) == 2
        nums1 = [1, 2]
        nums2 = [3, 4]
        assert Solution().findMedianSortedArrays(nums1, nums2) == 2.5
        nums1 = [2,5,6,8]
        nums2 = [1,3,4,7]
        assert Solution().findMedianSortedArrays(nums1, nums2) == 4.5
        #cProfile.runctx('Solution().calculate(case)', globals(), locals())

if __name__ == '__main__':
    unittest.main()
