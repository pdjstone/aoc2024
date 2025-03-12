b=[l.strip()for l in open('16')]
w=len(b)
b=''.join(b).strip()
c=[10e8]*w*w
D=0,1,0,-1
def m(p,d):
  x=p%w+D[d]
  y=p//w+D[~d]
  p=y*w+x
  return(p,b[p])if 0<=x<=w and 0<=y<=y else(0,0)

e=b.find('E')
s=b.find('S')
c[s]=0
def fr(p,d):
  cost=c[p]
  for nd in 0,1,2,3:
    np,nv=m(p,nd)
    if nv not in '.E': continue
    nc=cost+1+(0 if nd==d else 1000)
    if nc<c[np]:
      c[np]=nc
      fr(np,nd)    
import sys
sys.setrecursionlimit(10000)
fr(s,1)
print(c[e])
