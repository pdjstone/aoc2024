from itertools import combinations

board = [*open('8')]
w = len(board)
board = ''.join(l.strip() for l in board)


antennas = {*board}-{'.'}
antepodes = ['.']*w*w

def iter_locs(c):
    for i in range(w*w):
        if board[i]==c: yield i

def inboard(x,y):
    return 0 <= x < w and 0 <= y < w

for A in antennas:
    for a,b in combinations(iter_locs(A),2):
        ax = a%w
        ay = a//w
        bx = b%w
        by = b//w
        dx = bx-ax
        dy = by-ay
        
        ap1x = ax - dx
        ap1y = ay - dy
        ap2x = bx + dx
        ap2y = by + dy
        if inboard(ap1x, ap1y):
            antepodes[ap1y*w+ap1x] = '#'
        if inboard(ap2x, ap2y):
            antepodes[ap2y*w+ap2x] = '#'

print(antepodes.count('#'))