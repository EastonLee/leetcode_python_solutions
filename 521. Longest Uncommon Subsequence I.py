import unittest


class Solution(object):

    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        return -1 if a == b else max(len(a), len(b))


class Test(unittest.TestCase):

    def test(self):
        case = ["aba", "cdc"]
        assert Solution().findLUSlength(case[0], case[1]) == 3
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

if __name__ == '__main__':
    unittest.main()
