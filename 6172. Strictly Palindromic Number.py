import unittest


# return the number base on 2, 3, 4
def num_base(num: int, base: int) -> str:
    if num == 0:
        return '0'
    if num == 1:
        return '1'
    if num < 0:
        return '-' + num_base(-num, base)
    res = ''
    while num:
        res = str(num % base) + res
        num //= base
    return res


def isPalindromic(n: str) -> bool:
    return n == n[::-1]


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2, n - 1):
            if not isPalindromic(num_base(n, base)):
                return False
        return True


class Test(unittest.TestCase):
    def test(self):
        cases = [
            [9, False]
        ]
        for ci, co in cases:
            result = Solution().isStrictlyPalindromic(ci)
            assert result == co, (ci, co, result)


if __name__ == '__main__':
    unittest.main(exit=False)
