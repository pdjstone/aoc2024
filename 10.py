b=[*open('10')]
w=len(b)
b=[*map(int,''.join(l.strip()for l in b))]

def m(p,d):
 x=p%w; y=p//w
 if d==0: x+=1
 if d==1: y+=1
 if d==2: x-=1
 if d==3: y-=1
 p=y*w+x
 return (p,b[p]) if 0<=x<w and 0<=y<w else (0,0)

def t(p):
 h=set()
 v=b[p]
 if v==9: return {p}
 for d in (0,1,2,3):
  np,nv=m(p,d)
  if nv==v+1: h|=t(np)
 return h

print(sum(len(t(p))for p,v in enumerate(b) if v==0))