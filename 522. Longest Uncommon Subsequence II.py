import unittest

# https://discuss.leetcode.com/topic/85044/python-simple-explanation/2
# by @StefanPochmann


class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def issubsequence(s, t):
            t = iter(t)
            return all(c in t for c in s)
        for s in sorted(strs, key=len, reverse=True):
            if sum(issubsequence(s, t) for t in strs) == 1:
                return len(s)
        return -1


class Test(unittest.TestCase):

    def test(self):
        case = ["aba", "cdc"]
        assert Solution().findLUSlength(case) == 3
        case = ["aba", "cdca"]
        assert Solution().findLUSlength(case) == 4
        case = ["aaa", "aaa"]
        assert Solution().findLUSlength(case) == -1
        case = ["aaa", "aab"]
        assert Solution().findLUSlength(case) == 3
        case = ["ecyhzhrreknnlslstqtsvwrwnxcmjkdfdqtmnapngpjqobzaom",
                "ecyhzhrreknnlslstqtsvwrwnxcmjkdfdqtmnapngpjqobzaom"]
        assert Solution().findLUSlength(case) == -1
        case = ["aweffwaf",
                "aweffwaf"]
        assert Solution().findLUSlength(case) == -1
        case = ["aba", "cdc", "eae"]
        assert Solution().findLUSlength(case) == 3
        case = ["aba", "aba", "aba"]
        assert Solution().findLUSlength(case) == -1
        case = ["aaa", "aaa", "aa"]
        assert Solution().findLUSlength(case) == -1
        case = ["aabbcc", "aabbcc", "cb"]
        assert Solution().findLUSlength(case) == 2
        case = ["cb"]
        assert Solution().findLUSlength(case) == 2
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

if __name__ == '__main__':
    unittest.main()
