b=[*open('12')]
w=len(b)
b=''.join(s.strip()for s in b)
D=0,1,0,-1

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
 done|=s
 t+=p*len(s)
print(t)
 
