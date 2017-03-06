import unittest



class Solution(object):

    def findRotateSteps(self, ring, key):
        pre_pos_cost = [[0,0]]
        pos_d = {}
        ring_len = len(ring)
        for idx, i in enumerate(ring):
            if i in pos_d:
                pos_d[i].append(idx)
            else:
                pos_d[i] = [idx]
        for k in key:
            cur_pos_cost = []
            pos_l = pos_d[k]
            for p in pos_l:
                tmp_min = float('inf')
                for pre in pre_pos_cost:
                    tmp_min = min(min(abs(pre[0]-p), ring_len-abs(pre[0]-p)) + pre[1], tmp_min)
                cur_pos_cost.append([p, tmp_min])
            pre_pos_cost = cur_pos_cost
        return min([p[1] for p in pre_pos_cost]) + len(key)

class Test(unittest.TestCase):

    def test(self):
        ring = "godding"
        key = "gd"
        assert Solution().findRotateSteps(ring, key) == 4
        ring = "rtmdx"
        key = "dmrtx"
        assert Solution().findRotateSteps(ring, key) == 13
        ring = "godding"
        key = "godding"
        assert Solution().findRotateSteps(ring, key) == 13
        ring = "pqwcx"
        key = "cpqwx"
        assert Solution().findRotateSteps(ring, key) == 13
        ring = "caotmcaataijjxi"
        key = "oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx"
        assert Solution().findRotateSteps(ring, key) == 137
        #cProfile.runctx('Solution().calculate(case)', globals(), locals())

if __name__ == '__main__':
    unittest.main()
