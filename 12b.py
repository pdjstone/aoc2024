
b=[*open('12')]
w=len(b)
b=''.join(s.strip()for s in b)
D=0,1,0,-1
fol=(
 ((-1,-1),(0,-1)),
 ((1,-1),(1,0)),
 ((1,1),(0,1)),
 ((-1,1),(-1,0))
) 

def look(p,d):
  x=p%w
  y=p//w
  v=b[p]
  t=0
  for i,(dx,dy) in enumerate(fol[d]):
    xx=x+dx
    yy=y+dy
    if 0<=xx<w and 0<=yy<w:
     vv=b[yy*w+xx]
    else:
     vv=-1
    t+=(vv==v)*(1<<i)
  return t


def mrc(p,d):
 dx,dy=fol[d][0]
 x=p%w+dx
 y=p//w+dy
 assert 0<=x<w and 0<=y<w
 return y*w+x
 
def tr(p):
 sp=p
 sd=d=0
 sides=0
 ss={p}
 i=0
 while 1:
  v=look(p,d)
  if v in (0,1): 
   d=(d+1)%4
   sides+=1
  elif v==3:
   p=mrc(p,d)
   d=(d+3)%4
   sides+=1
  else:
   p,_=m(p,d)  
  ss.add(p)
  if p==sp and d==sd:
   return sides,sum(ss)
  
  
def m(p,d):
 x=p%w+D[d]
 y=p//w+D[~d]
 if 0<=x<w and 0<=y<w:
   return y*w+x, b[y*w+x]
 return 0,0
 
def fr(p,ps):
  t=0
  ps.add(p)
  for d in 0,1,2,3:
   np,v=m(p,d)
   if np not in ps and v==b[p]:
     t+=fr(np,ps)
   if v!=b[p]:
     t+=1
  return t

done=set()
t=0
for i in range(w*w):
 if i in done: continue
 s=set()
 p=fr(i,s)
 edges=set()
 sides=0
 for p in s:
   _,vv=m(p,3)
   if b[i]==vv: continue
   sides_,ss=tr(p)
   if ss not in edges:
    sides+=sides_
    edges.add(ss)
 print(b[i],i%w,i//w,len(s),sides)
 done|=s
 t+=len(s)*sides
print(t)

