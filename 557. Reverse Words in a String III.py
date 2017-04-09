import unittest


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = map(lambda x: x[::-1], s.split())
        return ' '.join(s)


class Test(unittest.TestCase):

    def test(self):
        Input = "Let's take LeetCode contest"
        Output = "s'teL ekat edoCteeL tsetnoc"
        assert Solution().reverseWords(Input) == Output
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

if __name__ == '__main__':
    unittest.main()
