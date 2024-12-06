def pb(b):
    for l in (b[i:i+w] for i in range(0,len(b),w)):
        print(''.join(l))
    print('-')
    
def m(pos,b):
    s=b[pos]
    d=sprs.index(s)
    dx,dy = dirs[d]
    nx = pos%w+dx
    ny = pos//w+dy
    if not (0 <= nx < w and 0 <= ny < h):
        raise Exception()
    np=ny*w+nx
    obs=b[np]
    if obs in '.X':
        b[pos] = 'X'
        return np,s
    return pos, sprs[d+1]

def isloop(b):
    pos = b.index('^')
    pp=set()

    while 1:
        try:
            pos,s = m(pos,b)
        except:
            break
        if (pos,s) in pp:
            return 1
        pp.add((pos,s))
        b[pos] = s
    return 0

b=[*open('6')]
w = len(b[0])-1
h = len(b)
b = list(''.join([l.strip() for l in b]))
sprs='^>v<'*2
dirs=((0,-1),(1,0),(0,1),(-1,0))
t = 0
for pos in (p for p in range(len(b)) if b[p] == '.'):
    nb = [*b]
    nb[pos] = '#'
    if isloop(nb):
        print(pos%w, pos//w)
        t+=1
print(t)
assert t==1655
    

