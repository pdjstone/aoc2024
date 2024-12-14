import re
from collections import*

w=101
h=103
D=0,1,0,-1

def m(b,p,d):
 x=p%w+D[d]
 y=p//w+D[~d]
 return b[y*w+x]if 0<=x<w and 0<=y<h else 0

def pb(b):
  s=''
  for y in range(h):
    l=''
    for x in range(w):
      v=b[y*w+x]
      l += str(v) if v >0 else '.'
    s+=l+'\n'
  return s

def it(i):
    b=defaultdict(int)   
    for x,y,vx,vy in r:
      vx=(w+vx)%w
      vy=(h+vy)%h
      x=(x+vx*i)%w
      y=(y+vy*i)%h
      b[y*w+x]+=1
    return b

T = 0
r = [[*map(int,re.findall('-?\d+',l))] for l in open('14')]
for j in range(30000):
  b=it(j)
  t=sum(v*m(b,p,i) for i in (0,1) for p,v in [*b.items()])
  if t > T:
    T = t
    print(pb(b))
    print(j,t)