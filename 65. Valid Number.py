

import unittest




class Solution(object):
    # non-sense problem for OJ, if asked in interview, you should clarify all possible situations.
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try: float(s)
        except ValueError: return False
        else: return True
        


class Test(unittest.TestCase):

    def test(self):
        def t(s, b=True):
            assert Solution().isNumber(s) == b
        t('0', True)
        t(" 0.1 ", True)
        t("abc", False)
        t("1 a", False)
        t("2e10", True)

        t('9 e 10')
        t('2.')
        t('.2')
        t('001')
        t('-0')
        t('5,000')
        t("+.8")

        t('-', False)
        t('.', False)
        t('', False)
        t(' ', False)
        t('e', False)
        t('', False)


        #cProfile.runctx('Solution().calculate(case)', globals(), locals())

if __name__ == '__main__':
    unittest.main()
