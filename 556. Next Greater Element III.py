import unittest

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_str = list(str(n))
        for i in range(len(n_str)-2, -1, -1):
            if n_str[i] < n_str[i+1]:
                s = n_str[i:]
                idx = s.index(min(filter(lambda x:x>s[0], s[1:])))
                sl = s.pop(idx)
                return int(''.join(n_str[:i] + [sl] + sorted(s))) if n < 2**31 else -1
        return -1


class Test(unittest.TestCase):

    def test(self):
        assert Solution().nextGreaterElement(12) == 21
        assert Solution().nextGreaterElement(21) == -1
        assert Solution().nextGreaterElement(12345) == 12354
        assert Solution().nextGreaterElement(12222333) == 12223233
        assert Solution().nextGreaterElement(12443322) == 13222344
        self.assertEqual(Solution().nextGreaterElement(198765432), 213456789)

        #cProfile.runctx('Solution().nextGreaterElement(2147483647)', globals(), locals(), sort='cumtime')

if __name__ == '__main__':
    unittest.main()
