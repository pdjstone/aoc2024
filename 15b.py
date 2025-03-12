b,m=open('15').read().split('\n\n')
b=b.split('\n')
w=h=len(b)
w=w*2
bb=[]
for l in b:
  for c in l:
    if c=='#': c='##'
    if c=='.': c='..'
    if c=='@': c='@.'
    if c=='O': c='[]'
    bb+=[*c]
    
b=bb
D=0,1,0,-1
S='^>v<'

def cb():
  return sum(1 for c in b if c=='[')
  
def pb():
  for i in range(0,w*h,w):
    print(''.join(b[i:i+w]))
    
def move(p,d):
  x=p%w+D[d]
  y=p//w+D[~d]
  return(y*w+x,b[y*w+x])if 0<=x<w and 0<=y<h else (0,0)


def movelr(p,d):
  r=[p]
  while 1:
      p,v=move(p,d)
      if v=='.': r+=[p]; break
      elif v in '[]': r+=[p]
      else: break
  if b[r[-1]]=='.': 
      for k,l in zip(r[::-1],r[-2::-1]):b[k]=b[l]
      b[r[0]]='.'
      p=r[1]
  else:
      p=r[0]
  return p

def fb(box,boxes,d):
  boxes+=[box]
  for n in box,box+1:
    p,v=move(n,d)
    if v=='#': return 0
    if v=='[' and not fb(p,boxes,d): return 0
    if v==']' and not fb(p-1,boxes,d): return 0
  return 1
   
def moveud(p,d):
  P,v=move(p,d)
  if v=='.':
    b[p]='.'
    b[P]='@'
    return P
  elif v=='#':
    return p

  box=P if v=='[' else P-1
  boxes=[]
  if not fb(box,boxes,d):
    return p
  boxes=sorted(boxes)
  if d==2:
    boxes=boxes[::-1]
  for box in boxes:
    nb,_=move(box,d)
    b[nb:nb+2]=[*'[]']
    b[box:box+2]=[*'..']
  b[p]='.'
  b[P]='@'
  return P
  
  
  
  
pb()
nboxes=cb()

p=b.index('@')
m=m.replace('\n','')
#m='<v<^^'
for d in m:
  dn=S.index(d)
  if d in '<>':
    p=movelr(p,dn)
  else:
    p=moveud(p,dn)
  if cb()<nboxes:
    print(p%w,p//w,d)
    break
pb()
print(cb())
print(sum((i//w)*100+(i%w) for i,v in enumerate(b) if v=='['))
