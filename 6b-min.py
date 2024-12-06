from multiprocessing import Pool
def m(p,b):s=b[p];d=T[s];X=p%w+D[d];Y=p//w+D[-d-1];return(-1,0)if not(0<=X<w and 0<=Y<w)else(p,S[d+1])if b[Y*w+X]=='#'else(Y*w+X,s)
def l(a):
 b,p,x=a;b=[*b];b[x]='#';t=[0]*w*w
 while 1:
  p,s=m(p,b)
  if p<0:return 0
  b[p]=s;v=1<<T[s]
  if t[p]&v:return 1
  t[p]|=v
b=[*open('6')]
w=len(b)
b=[*''.join([l[:-1]for l in b])]
q=p=b.index('^')
T={'^':0,'>':1,'v':2,'<':3}
S='^>v<'*2
s='^'
D=0,1,0,-1
r=[*b]
while p>=0:r[p]=s;p,s=m(p,r)
print(sum(Pool().map(l,((b,q,p)for p in(p for p in range(w*w)if r[p]in S and p!=q)))))
