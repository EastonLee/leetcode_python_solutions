import unittest


class Solution(object):

    def licenseKeyFormatting(self, S, K):
        S = S.upper().replace('-', '')
        result, c = [], 0
        for i in S[::-1]:
            c += 1
            if c == K + 1:
                result.append('-')
                c = 1
            result.append(i)
        return ''.join(result[::-1])

    # https://discuss.leetcode.com/topic/74891/python-solution/2
    # yujiao03gmail.com
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace('-', '').upper()
        size = len(S)
        s1 = K if size % K == 0 else size % K
        res = S[:s1]
        while s1 < size:
            res += '-' + S[s1:s1 + K]
            s1 += K
        return res


class Test(unittest.TestCase):

    def test(self):
        case = "2-4A0r7-4k"
        assert Solution().licenseKeyFormatting(case, 4) == "24A0-R74K"
        case = '2-4A0r7-4k'
        assert Solution().licenseKeyFormatting(case, 3) == "24-A0R-74K"

if __name__ == '__main__':
    unittest.main()
