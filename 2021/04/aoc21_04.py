# %%
from aocd import lines
# %%
linesW = {frozenset([(i,i) for i in range(5)]),frozenset([(i,5-i-1) for i in range(5)])}
for x in range(5):
    linesW.add(frozenset([(x,i) for i in range(5)]))
    linesW.add(frozenset([(i,x) for i in range(5)]))

def draw(v,board):
    t = [(i, col.index(v)) for (i, col) in enumerate(board) if v in col]
    if t:
        return t
    

def test_win(drew,linesW=linesW):
    for x in linesW:
        if x.issubset(drew):
            return True
        else:
            return False

# %%
def bingo(boards=boards,linesW=linesW):
    x = {b:set() for b in boards}
    win = False
    for v in input:
        for b in boards:
            a = draw(v,boards[b])
            if a:
                x[b].add(a[0])
            win = test_win(x[b],linesW)
        if win:
            break
    return(b,x[b],v)

def results(board,x,v):
    board_f = [val for sub in board for val in sub]
    picked = [board[y[0]][y[1]] for y in x]
    return((sum(board_f)-sum(picked))*v)


# %%
lines[0]
# %%
list(map(int,lines[0].split(',')))

# %%
