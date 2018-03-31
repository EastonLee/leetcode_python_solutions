import unittest



class Solution(object):

    # https://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/
    # O(m*n) space
    def minDistance(self, word1, word2):
        l1, l2 = len(word1)+1, len(word2)+1
        dp = [[0 for _ in range(l2)] for _ in range(l1)]
        for i in range(l1):
            dp[i][0] = i
        for j in range(l2):
            dp[0][j] = j
        for i in range(1, l1):
            for j in range(1, l2):
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+(word1[i-1]!=word2[j-1]))
        return dp[-1][-1]



class Test(unittest.TestCase):

    def test(self):
        assert Solution().minDistance('abc', 'de') == 3
        assert Solution().minDistance('abc', 'ab') == 1
        assert Solution().minDistance("sea", "eat") == 2
        print(Solution().minDistance("horse", "ros"))
        assert Solution().minDistance("horse", "ros") == 3
        #cProfile.runctx('Solution().calculate(case)', globals(), locals())

if __name__ == '__main__':
    unittest.main()
