import re
from z3 import Solver, Ints, unsat

def solve(p):
    ax, ay, bx, by, px, py = map(int, re.findall('\d+', p))
    O = 10000000000000
    A, B = Ints('A B')
    s = Solver()
    s += A*ax + B*bx == px + O, A*ay + B*by == py + O
    if s.check() == unsat:
        return 0
    return s.model().eval(A*3+B).as_long()

print(sum(map(solve, open('13').read().split('\n\n'))))