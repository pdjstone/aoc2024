b,m=open('15').read().split('\n\n')
b=b.split('\n')
w=len(b)
b=[*''.join(b)]
D=0,1,0,-1
S='^>v<'

def pb():
  for i in range(0,w*w,w):
    print(''.join(b[i:i+w]))
    
def move(p,d):
  x=p%w+D[d]
  y=p//w+D[~d]
  return(y*w+x,b[y*w+x])if 0<=x<w and 0<=y<w else (0,0)

p=b.index('@')
for d in m.replace('\n',''):
  r=[p]
  while 1:
   p,v=move(p,S.index(d))
   if v=='.': r+=[p]; break
   elif v=='O': r+=[p]
   else: break
  if b[r[-1]]=='.': 
    for k,l in zip(r[::-1],r[-2::-1]):b[k]=b[l]
    b[r[0]]='.'
    p=r[1]
  else:
    p=r[0]

pb()
print(sum((i//w)*100+(i%w) for i,v in enumerate(b) if v=='O'))
