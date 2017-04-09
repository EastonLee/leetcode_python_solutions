import unittest
import collections


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        w = collections.defaultdict(int)
        for i in wall:
            tmp_w = 0
            for j in i:
                tmp_w += j
                w[tmp_w] += 1
        if len(w) == 1: return len(wall)
        return len(wall) - sorted(w.values(), reverse=True)[1]

class Test(unittest.TestCase):

    def test(self):
        Input = \
[[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]
        Output = 2
        print(Solution().leastBricks(Input))
        assert Solution().leastBricks(Input) == Output
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

if __name__ == '__main__':
    unittest.main()
