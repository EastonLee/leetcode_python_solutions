import unittest


class Test(unittest.TestCase):
    def test(self):
        cases = [
            ["1+7-(7+3+3)+6-3+1", -1]
        ]
        for ci, co in cases:
            result = Solution().calculate(ci)
            assert result == co, (ci, co, result)
        #cProfile.runctx('Solution().calculate(case)', globals(), locals(), sort='cumtime')

    def est_tree_draw(self):
        tree_draw(tree_deserialize('[1,2,3,4,5,6,7]'))


if __name__ == '__main__':
    unittest.main(exit=False)