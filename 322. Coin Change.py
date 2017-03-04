import unittest


class Solution(object):

    def coinChange(self, coins, amount):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        new, seen = {0}, {0}
        count = 0
        while new:
            if amount in seen:
                return count
            new = {i + j for i in new for j in coins if i + j <= amount} - seen
            seen |= new
            count += 1
        return -1


class Test(unittest.TestCase):

    def test(self):
        assert Solution().coinChange([1, 2, 5], 11) == 3
        assert Solution().coinChange([2], 3) == -1

if __name__ == '__main__':
    unittest.main()
