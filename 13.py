import re,z3
def s(p):h,j,k,l,x,y=map(int,re.findall('\d+',p));O=10**13;A,B=z3.Ints('A B');s=z3.Solver();s+=A*h+B*k==x+O,A*j+B*l==y+O;return int(str(s.model().eval(A*3+B)))if s.check()==z3.sat else 0
print(sum(map(s,open('13').read().split('\n\n'))))