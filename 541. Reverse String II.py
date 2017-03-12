import unittest

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        split = [s[i:i+2*k] for i in range(0, len(s), 2*k)]
        for i in range(len(split)):
            split[i] = split[i][0:k][::-1] + split[i][k:2*k]
        return ''.join(split)



class Test(unittest.TestCase):

    def test(self):
        s = "abcdefg"; k = 2
        assert Solution().reverseStr(s, k) == "bacdfeg"
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

if __name__ == '__main__':
    unittest.main()
