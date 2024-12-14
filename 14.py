import re
from collections import*
w=101
h=103
i=100
mw=w//2
mh=h//2
b=defaultdict(int)
def pb():
  for y in range(h):
    l=''
    for x in range(w):
      v=b[y*w+x]
      l += str(v) if v >0 else '.'
    print(l)
    
for l in open('14'):
  x,y,vx,vy=map(int,re.findall(r'-?\d+',l))
  vx=(w+vx)%w
  vy=(h+vy)%h
  x=(x+vx*i)%w
  y=(y+vy*i)%h
  b[y*w+x]+=1

pb()
s=[0]*4
for p,v in b.items():
  if v==0: continue
  x=p%w
  y=p//w
  if x==mw or y==mh: continue
  q=[0,1][x>mw]+[0,2][y>mh]
  s[q]+=v
print(s)
a,b,c,d=s
print(a*b*c*d)
  
  
