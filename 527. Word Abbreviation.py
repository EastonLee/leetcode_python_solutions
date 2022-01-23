import unittest
from pprint import pprint
import re
import cProfile
import heapq
import collections
import itertools



class Solution(object):
    def wordsAbbreviation(self, words):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        def first_diff(w, ws):
            """
            :type ws: list
            """
            for i in range(len(w)):
                if w[i] not in [j[i] for j in ws if w[i]!=j]:
                    return i
                else:
                    for j in enumerate([j[i] for j in ws if w[i]]):
                        ws.remove(j)
        d = collections.defaultdict(collections.defaultdict(list))
        rst = []
        for w in words:
            d[len(w)][w[0]+w[-1]].append(w)
        for w in words:
            if len(d[len(w)][w[0]+w[-1]]) == 1:
                rst.append(w)
            if len(d[len(w)][w[0]+w[-1]]) == 2:

class Test(unittest.TestCase):

    def test(self):
        Input = ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
        Output = ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
        assert Solution().wordsAbbreviation(Input) == Output
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

if __name__ == '__main__':
    unittest.main()
