import unittest


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s.count('L') <= 2 and s.count('A') <= 1


class Test(unittest.TestCase):

    def test(self):
        Input = "PPALLP"
        Output = True
        assert Solution().checkRecord(Input) == Output
        Input = "PPALLL"
        Output = False
        assert Solution().checkRecord(Input) == Output


if __name__ == '__main__':
    unittest.main()
