import unittest
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cur_idx = 0
        last_idx = s.rfind(s[0])
        rst = []
        length = 1
        while True:
            if cur_idx == len(s) - 1:
                rst.append(length)
                break
            if cur_idx == last_idx:
                rst.append(length)
                length = 1
                cur_idx += 1
                cur = s[cur_idx]
                last_idx = s.rfind(cur)
                continue

            cur = s[cur_idx]
            last_idx = max(last_idx, s.rfind(cur))
            cur_idx += 1
            length += 1
        return rst


class Test(unittest.TestCase):

    def test(self):
        cases = [
            ["ababcbacadefegdehijhklij", [9, 7, 8]],
            ["eccbbbbdec", [10]]
        ]
        for ci, co in cases:
            result = Solution().partitionLabels(ci)
            assert result == co, (ci, co, result)
        # cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')


if __name__ == '__main__':
    unittest.main(exit=False)
