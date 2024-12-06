b=[*open('6')]
w=len(b)
b=[*''.join([l.strip()for l in b])]
p=b.index('^')
S='^>v<'*2
D=(0,1,0,-1)
while 1:
 s=b[p];d=S.find(s);nx=p%w+D[d];ny=p//w+D[-d-1]
 if not(0<=nx<w and 0<=ny<w):break
 np=ny*w+nx
 if b[np]=='#':s=S[d+1]
 else:b[p]='X';p=np
 b[p]=s
print(b.count('X')+1)