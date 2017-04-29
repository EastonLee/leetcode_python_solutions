import unittest
from pprint import pprint
import re
import cProfile
import heapq
import collections
import itertools

# https://discuss.leetcode.com/topic/3040/linear-runtime-and-constant-space-solution
# by @pandora111


class Solution(object):
    def isMatch(self, s, p):
        """
        dp[n] means the substring s[:n] if match the pattern i
        dp[0] means the empty string '' or s[:0] which only match the pattern '*'
        use the reversed builtin because for every dp[n+1] we use the previous 'dp'
        """
        length = len(s)
        if len(p) - p.count('*') > length:
            return False
        dp = [True] + [False] * length
        for i in p:
            if i != '*':
                for n in reversed(range(length)):
                    dp[n + 1] = dp[n] and (i == s[n] or i == '?')
            else:
                for n in range(1, length + 1):
                    dp[n] = dp[n - 1] or dp[n]
            dp[0] = dp[0] and i == '*'
        return dp[-1]

# http://yucoding.blogspot.com/2013/02/leetcode-question-123-wildcard-matching.html
# very straightforward


class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        s_cur = 0
        p_cur = 0
        match = 0
        star = -1
        while s_cur < len(s):
            if p_cur < len(p) and (s[s_cur] == p[p_cur] or p[p_cur] == '?'):
                s_cur = s_cur + 1
                p_cur = p_cur + 1
            elif p_cur < len(p) and p[p_cur] == '*':
                match = s_cur
                star = p_cur
                p_cur = p_cur + 1
            elif (star != -1):
                p_cur = star + 1
                match = match + 1
                s_cur = match
            else:
                return False
        while p_cur < len(p) and p[p_cur] == '*':
            p_cur = p_cur + 1

        if p_cur == len(p):
            return True
        else:
            return False


class Solution(object):
    def isMatch(self, s, p):
        dp = [True] + [False] * len(s)
        for i in range(len(p)):
            if p[i] == '*':
                for j in range(1, len(s) + 1):
                    dp[j] = dp[j] or dp[j - 1]
            else:
                for j in range(1, len(s) + 1)[::-1]:
                    dp[j] = dp[j - 1] and p[i] in ('?', s[j - 1])
            dp[0] = dp[0] and p[i] == '*'
        return dp[-1]


class Test(unittest.TestCase):

    def test(self):

        assert Solution().isMatch("aa", "a") == False
        assert Solution().isMatch("aa", "aa") == True
        assert Solution().isMatch("aaa", "aa") == False
        assert Solution().isMatch("aa", "*") == True
        assert Solution().isMatch("aa", "a*") == True
        assert Solution().isMatch("ab", "?*") == True
        assert Solution().isMatch("aab", "c*a*b") == False
        assert Solution().isMatch("zacabz", "*a?b*") == False


if __name__ == '__main__':
    unittest.main()
