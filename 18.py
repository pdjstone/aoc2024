import time
g=[(*map(int,l.split(',')),)for l in open('18ex')]
w=7 if len(g)<1024 else 71
print(w)
b=[0]*w*w
c=[10**8]*w*w
D=0,1,0,-1

for x,y in g[:12 if w<10 else 1024]:
  #print(x,y,y*w+x)
  b[y*w+x]=1

def pb():
  for i in range(0,w*w,w):
    print(''.join('.#'[v] for v in b[i:i+w]))

def m(p,d):
  x=p%w+D[d]
  y=p//w+D[~d]
  p=y*w+x
  return (p,b[p])if 0<=x<w and 0<=y<w else(-1,1)

t=0
def f(p):
  global t  
  cost=c[p]
  #if t%10000==0:
  #  pr()
  #  print(t, p, p%w,p//w,cost)
  #  time.sleep(1)
  t+=1
  #if t>10000: return
  for d in 0,1,2,3:
    P,v=m(p,d)
    if p==2189:
      print(t,'x',p%w,'y',p//w,'d',d,'v',v,cost,c[P])
    if v>0:continue
    nc=cost+1
    if c[P]<=nc: continue
    c[P]=nc
    f(P)
    
  
    
pb()
exit=w*w-1
start=0
c[exit]=0

def pr():
 for i in range(0,w*w,w):
  print(''.join(('*' if x<10**8 else '.')if b[i+j]==0 else '#' for j,x in enumerate(c[i:i+w])))
 print('--')

f(exit)

print(c[0])
