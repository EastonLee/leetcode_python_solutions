import unittest



class Solution(object):

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        l1 = 'qwertyuiop'
        l2 = 'asdfghjkl'
        l3 = 'zxcvbnm'
        def one_row(w):
            w = w.lower()
            return all(i in l1 for i in w) or \
                all(i in l2 for i in w) or all(i in l3 for i in w)
        return filter(one_row, words)


class Test(unittest.TestCase):

    def test(self):
        case = ["Hello", "Alaska", "Dad", "Peace"]
        outcome = ["Alaska", "Dad"]
        print Solution().findWords(case)
        assert Solution().findWords(case) == outcome
        #cProfile.runctx('Solution().calculate(case)', globals(), locals())

if __name__ == '__main__':
    unittest.main()
