import time,sys
g=[(*map(int,l.split(',')),)for l in open('18')]
w=7 if len(g)<1024 else 71
print(w)
D=0,1,0,-1


def pb():
  global b
  for i in range(0,w*w,w):
    print(''.join('.#'[v] for v in b[i:i+w]))
  print()

def m(p,d):
  global b
  x=p%w+D[d]
  y=p//w+D[~d]
  p=y*w+x
  return (p,b[p])if 0<=x<w and 0<=y<w else(-1,1)

t=0
def f(p):
  global t,b,c 
  cost=c[p]
  #if t%10000==0:
  #  pr()
  #  print(t, p, p%w,p//w,cost)
  #  time.sleep(1)
  t+=1
  #if t>10000: return
  for d in 0,1,2,3:
    P,v=m(p,d)
    #if p==2189:
    #  print(t,'x',p%w,'y',p//w,'d',d,'v',v,cost,c[P])
    if v>0:continue
    nc=cost+1
    if c[P]<=nc: continue
    c[P]=nc
    f(P)
    
  
    
exit=w*w-1
start=0
sys.setrecursionlimit(20000)
for i in range(len(g)-1,12 if w<50 else 1024,-1):
  b=[0]*w*w
  c=[10**8]*w*w
  
  for x,y in g[:i]:
    b[y*w+x]=1
  #pb()  
  c[exit]=0
  f(exit)
  if c[0]<10**8:
    print(g[i])
    break
  print(i,len(g))

def pr():
 for i in range(0,w*w,w):
  print(''.join(('*' if x<10**8 else '.')if b[i+j]==0 else '#' for j,x in enumerate(c[i:i+w])))
 print('--')


