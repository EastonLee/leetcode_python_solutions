import unittest


class Solution(object):

    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        #board = board
        r_no = len(board)
        c_no = r_no and len(board[0])

        def get_adj(pos):

            x, y = pos
            adj = [[x + i, y + j, borad[x + i][y + j]]
                   for i in (-1, 0, 1) for j in (-1, 0, 1) if (i or j) and 0 <= x + i < r_no and 0 <= y + j < c_no]
            return adj
        x, y = click[0], click[1]
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        if board[x][y] == 'E':
            adj = get_adj(click)
            adj_mine_no = len(filter(lambda x: x[2] == 'M', adj))
            if adj_mine_no:
                board[x][y] = str(adj_mine_no)
                return board
            else:
                board[x][y] = 'B'
                for i in adj:
                    if board[i[0]][i[1]] == 'E':
                        self.updateBoard(board, i[:2])
                return board


class Test(unittest.TestCase):

    def test(self):
        case = \
            [['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'M', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E']]
        assert Solution().updateBoard(case, [3, 0]) == \
            [['B', '1', 'E', '1', 'B'],
             ['B', '1', 'M', '1', 'B'],
             ['B', '1', '1', '1', 'B'],
             ['B', 'B', 'B', 'B', 'B']]
        case = \
            [['B', '1', 'E', '1', 'B'],
             ['B', '1', 'M', '1', 'B'],
                ['B', '1', '1', '1', 'B'],
                ['B', 'B', 'B', 'B', 'B']]
        assert Solution().updateBoard(case, [1, 2]) == \
            [['B', '1', 'E', '1', 'B'],
             ['B', '1', 'X', '1', 'B'],
             ['B', '1', '1', '1', 'B'],
             ['B', 'B', 'B', 'B', 'B']]

if __name__ == '__main__':
    unittest.main()
