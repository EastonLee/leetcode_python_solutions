import unittest
from pprint import pprint
import re
import cProfile
import heapq
import collections
import itertools
'''
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
'''
class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        s = s.strip()
        sign = 1
        integral = []
        length = len(s)
        after_integral = False
        for i in range(length):
            if i==0 and s[i] in '-+':
                if s[i] == '-':
                    sign = -1
                continue
            if after_integral:
                if s[i] not in'0123456789':
                    return 0
                else:
                    continue
            if s[i] in '0123456789':
                integral.append(ord(s[i])-ord('0'))
            elif s[i] == '.':
                after_integral = True
            else:
                break
        if len(integral) < 2:
            return len(integral) and sign*integral[0]
        integral = reduce(lambda x,y:10*x+y, integral)
        if sign*integral > 2147483647:
            return 2147483647
        elif sign*integral < -2147483648:
            return -2147483648
        else:
            return sign*integral




class Test(unittest.TestCase):

    def test(self):
        assert Solution().myAtoi('-100') == -100
        assert Solution().myAtoi('-1') == -1
        assert Solution().myAtoi('  -100  ') == -100
        assert Solution().myAtoi('  100  ') == 100
        assert Solution().myAtoi('-100.123') == -100
        assert Solution().myAtoi('100.123') == 100
        assert Solution().myAtoi('abc') == 0
        assert Solution().myAtoi('100.a') == 0
        assert Solution().myAtoi(' 2147483648 ') == 2147483647
        assert Solution().myAtoi('-2147483649') == -2147483648
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

if __name__ == '__main__':
    unittest.main()
