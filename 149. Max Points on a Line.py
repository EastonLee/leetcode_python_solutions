import unittest
import cProfile

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)

class Solution(object):

    # Easton old, using float, causing error
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) < 2:
            return len(points)
        from collections import defaultdict
        lines = defaultdict(set)
        for idx1, p1 in enumerate(points):
            for idx2, p2 in zip(range(idx1+1, len(points)), points[idx1+1:]):
                slope = float(p1.y - p2.y) / (p1.x - p2.x) if (p1.x-p2.x) else float('inf')
                intcpt = p1.y - p1.x * slope if (p1.x!=p2.x) else p1.x
                lines[(slope, intcpt)] |= {idx1,idx2}
        return max(map(len, lines.values()))

    # https://discuss.leetcode.com/topic/35643/clean-python-code
    # shiyanhui
    # Python fractions is doable, but with poor performance
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) < 2:
            return len(points)
        def get_gcd(a, b):
            while b:
                a, b = b, a%b
            return a
        from collections import defaultdict, Counter
        counter = Counter([(i.x,i.y) for i in points])
        lines = defaultdict(set)
        for idx1, p1 in enumerate(points):
            for idx2, p2 in zip(range(idx1+1, len(points)), points[idx1+1:]):
                a, b, c = p1.y-p2.y, p2.x-p1.x, p1.x*p2.y-p2.x*p1.y
                if a==0 and b==0:
                    continue
                if a<0 or a==0 and b<0:
                    a, b, c = -a, -b, -c
                gcd = get_gcd(get_gcd(abs(a), abs(b)), abs(c))
                lines[(a/gcd, b/gcd, c/gcd)] |= {idx1,idx2}
        return max(map(len, lines.values()) + counter.values())

class Test(unittest.TestCase):

    def test(self):
        case = []
        assert Solution().maxPoints(case) == 0
        case = [Point(0,0)]
        assert Solution().maxPoints(case) == 1
        case = [Point(0,0),Point(0,0)]
        assert Solution().maxPoints(case) == 2
        case =  [[560,248],[0,16],[30,250],[950,187],[630,277],[950,187],[-212,-268],[-287,-222],[53,37],[-280,-100],[-1,-14],[-5,4],[-35,-387],[-95,11],[-70,-13],[-700,-274],[-95,11],[-2,-33],[3,62],[-4,-47],[106,98],[-7,-65],[-8,-71],[-8,-147],[5,5],[-5,-90],[-420,-158],[-420,-158],[-350,-129],[-475,-53],[-4,-47],[-380,-37],[0,-24],[35,299],[-8,-71],[-2,-6],[8,25],[6,13],[-106,-146],[53,37],[-7,-128],[-5,-1],[-318,-390],[-15,-191],[-665,-85],[318,342],[7,138],[-570,-69],[-9,-4],[0,-9],[1,-7],[-51,23],[4,1],[-7,5],[-280,-100],[700,306],[0,-23],[-7,-4],[-246,-184],[350,161],[-424,-512],[35,299],[0,-24],[-140,-42],[-760,-101],[-9,-9],[140,74],[-285,-21],[-350,-129],[-6,9],[-630,-245],[700,306],[1,-17],[0,16],[-70,-13],[1,24],[-328,-260],[-34,26],[7,-5],[-371,-451],[-570,-69],[0,27],[-7,-65],[-9,-166],[-475,-53],[-68,20],[210,103],[700,306],[7,-6],[-3,-52],[-106,-146],[560,248],[10,6],[6,119],[0,2],[-41,6],[7,19],[30,250]]
        case = [Point(i,j) for i,j in case]
        assert Solution().maxPoints(case) == 22
        case = [[40,-23],[9,138],[429,115],[50,-17],[-3,80],[-10,33],[5,-21],[-3,80],[-6,-65],[-18,26],[-6,-65],[5,72],[0,77],[-9,86],[10,-2],[-8,85],[21,130],[18,-6],[-18,26],[-1,-15],[10,-2],[8,69],[-4,63],[0,3],[-4,40],[-7,84],[-8,7],[30,154],[16,-5],[6,90],[18,-6],[5,77],[-4,77],[7,-13],[-1,-45],[16,-5],[-9,86],[-16,11],[-7,84],[1,76],[3,77],[10,67],[1,-37],[-10,-81],[4,-11],[-20,13],[-10,77],[6,-17],[-27,2],[-10,-81],[10,-1],[-9,1],[-8,43],[2,2],[2,-21],[3,82],[8,-1],[10,-1],[-9,1],[-12,42],[16,-5],[-5,-61],[20,-7],[9,-35],[10,6],[12,106],[5,-21],[-5,82],[6,71],[-15,34],[-10,87],[-14,-12],[12,106],[-5,82],[-46,-45],[-4,63],[16,-5],[4,1],[-3,-53],[0,-17],[9,98],[-18,26],[-9,86],[2,77],[-2,-49],[1,76],[-3,-38],[-8,7],[-17,-37],[5,72],[10,-37],[-4,-57],[-3,-53],[3,74],[-3,-11],[-8,7],[1,88],[-12,42],[1,-37],[2,77],[-6,77],[5,72],[-4,-57],[-18,-33],[-12,42],[-9,86],[2,77],[-8,77],[-3,77],[9,-42],[16,41],[-29,-37],[0,-41],[-21,18],[-27,-34],[0,77],[3,74],[-7,-69],[-21,18],[27,146],[-20,13],[21,130],[-6,-65],[14,-4],[0,3],[9,-5],[6,-29],[-2,73],[-1,-15],[1,76],[-4,77],[6,-29]]
        case = [Point(i,j) for i,j in case]
        assert Solution().maxPoints(case) == 25

        #cProfile.runctx('Solution().maxPoints(case)', globals(), locals(), sort='cumtime')
if __name__ == '__main__':
    unittest.main()
