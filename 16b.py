b=[l.strip()for l in open('16ex')]
w=len(b)
b=''.join(b).strip()
c=[99999999]*w*w
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
    if nc<=c[np]:
      c[np]=nc
      fr(np,nd)    
import sys
sys.setrecursionlimit(10000)
fr(s,1)
print(c[e])

def cr(p,r):
  r.add(p)
  for d in 0,1,2,3:
    np,nv=m(p,d)
    if c[np]%1000<c[p]%1000:
      cr(np,r)

def pr():
  for i in range(0,w*w,w):
    l=b[i:i+w]
    pl=''
    for j,ch in enumerate(l):
      pl+='O' if i+j in r else ch
    print(pl)
      
r=set()
cr(e,r)
pr()
print(len(r))
x=5
y=7
p=y*w+x
print(c[p])
for d in 0,1,2,3:
  np,nd=m(p,d)
  print(' ',c[np])
