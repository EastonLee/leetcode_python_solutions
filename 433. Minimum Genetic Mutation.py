import unittest


class Solution(object):

    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        from itertools import chain
        new = [start]
        seen = set([start])
        ATCG = 'ATCG'

        def new_start(start):
            start = [start] * len(start)
            for idx, i in enumerate(start):
                start[idx] = [i[:idx] + j + i[idx + 1:]
                              for j in ATCG if j != i[idx]]
            start = [j for i in start for j in i if j in bank and j not in seen]
            return start
        count = 1
        while new:
            new = list(chain.from_iterable([new_start(i) for i in new]))
            if end in new:
                return count
            seen |= set(new)
            count += 1
        return -1


class Test(unittest.TestCase):

    def test(self):
        start = "AACCGGTT"
        end = "AACCGGTA"
        bank = ["AACCGGTA"]
        assert Solution().minMutation(start, end, bank) == 1
        start = "AACCGGTT"
        end = "AAACGGTA"
        bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
        assert Solution().minMutation(start, end, bank) == 2
        start = "AAAAACCC"
        end = "AACCCCCC"
        bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
        assert Solution().minMutation(start, end, bank) == 3
        start = "AAAAAAAA"
        end = "CCCCCCCC"
        bank = ["AAAAAAAA", "AAAAAAAC", "AAAAAACC", "AAAAACCC", "AAAACCCC",
                "AACACCCC", "ACCACCCC", "ACCCCCCC", "CCCCCCCA", "CCCCCCCC"]
        assert Solution().minMutation(start, end, bank) == 8
        start = "AAAACCCC"
        end = "CCCCCCCC"
        bank = ["AAAACCCA", "AAACCCCA", "AACCCCCA", "AACCCCCC",
                "ACCCCCCC", "CCCCCCCC", "AAACCCCC", "AACCCCCC"]
        assert Solution().minMutation(start, end, bank) == 4
        #cProfile.runctx('Solution().calculate(case)', globals(), locals())

if __name__ == '__main__':
    unittest.main()
