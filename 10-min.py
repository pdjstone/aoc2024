b=[*open('10')]
w=len(b)
b=[*map(int,''.join(l[:-1]for l in b))]
n=1,0,-1,0
def t(p):
 h={};v=b[p]
 if v>8:return{p:1}
 for d in 0,1,2,3:
  x=p%w+n[d];y=p//w+n[-d-1];P=y*w+x
  if(0<=x<w)&(0<=y<w)and b[P]==v+1:h|=t(P)
 return h
print(sum(len(t(p))for p,v in enumerate(b) if v<1))