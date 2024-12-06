def pb():
    for l in (b[i:i+w] for i in range(0,len(b),w)):
        print(''.join(l))
    print('-')
    
def m(pos):
    s=b[pos]
    d=sprs.index(s)
    dx,dy = dirs[d]
    np=pos + dx + dy*w
    try:
        obs=b[np]
    except:
        obs='.'
    if obs in '.X':
        b[pos] = 'X'
        return np,s
    return pos, sprs[d+1]


b=[*open('6')]
w = len(b[0])-1
h = len(b)
b = list(''.join([l.strip() for l in b]))
pos=b.index('^')
sprs='^>v<'*2
dirs=((0,-1),(1,0),(0,1),(-1,0))

while 0 <= pos <= w*h:
    pos,s = m(pos)
    try:
        b[pos] = s
    except:
        break

pb()

print(b.count('X'))