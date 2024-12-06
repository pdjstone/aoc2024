b=[*open('6')]
w=len(b)
b=[*''.join([l[:-1]for l in b])]
p=b.index('^')
S='^>v<'*2
D=0,1,0,-1
while 1:
 s=b[p];d=S.find(s);X=p%w+D[d];Y=p//w+D[-d-1]
 if not(0<=X<w and 0<=Y<w):break
 P=Y*w+X
 if b[P]=='#':s=S[d+1]
 else:b[p]='X';p=P
 b[p]=s
print(b.count('X')+1)