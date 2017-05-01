import fileinput

def main():
    board = []
    indices = []
    for i in fileinput.input():
        board.append(i)
    for i in board:
        count = i.count('*')
        if count != 1:
            print 'invalid'
            return
        indices.append(i.index('*'))
    dia_indices = map(lambda x: x[0] - x[1], enumerate(indices))
    anti_dia_indices = map(lambda x: x[0] + x[1], enumerate(indices))
    if len(set(indices)) < 8 or len(set(dia_indices)) < 8 or len(set(anti_dia_indices)) < 8:
        print 'invalid'
        return
    print 'valid'
    return

main()
