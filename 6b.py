from multiprocessing import Pool

def m(pos,b):
    s=b[pos]
    d=S[s]
    dx,dy = dirs[d]
    nx = pos%w+dx
    ny = pos//w+dy
    if not (0 <= nx < w and 0 <= ny < h):
        return-1,0
    np=ny*w+nx
    if b[np] == '#':
        return pos, sprs[d+1]
    return np,s
    
def isloop(*args):
    b, pos, xb = args[0]
    b = [*b]
    b[xb] = '#'
    trail = [0 for _ in b]
    while 1:
        pos,s = m(pos,b)
        if pos<0: break
        b[pos] = s
        v=1<<S[s]
        if trail[pos]&v:
            return 1
        trail[pos]|=v
    return 0

b=[*open('6')]
w = len(b[0])-1
h = len(b)
b = list(''.join([l.strip() for l in b]))
pos =p= b.index('^')
S = {'^':0,'>':1,'v':2,'<':3}
sprs='^>v<'*2
dirs=((0,-1),(1,0),(0,1),(-1,0))
bb=b.copy()
while 1:
  p,s=m(p,bb)
  if p<0:break
  bb[p]=s

p=Pool()
print(sum(p.map(isloop, ((b,pos,p) for p in (p for p in range(len(b)) if bb[p] in sprs and p!=pos)))))

