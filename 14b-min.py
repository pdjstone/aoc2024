import re
w=101
h=103
D=0,1,0,-1
T=0
r=[[*map(int,re.findall('-?\d+',l))]for l in open('14')]
for j in range(w*h):
 b=[0]*w*h
 for x,y,vx,vy in r:b[(x+(w+vx)*j)%w+w*((y+(h+vy)*j)%h)]+=1
 t=sum(a*b for a,b in zip(b,b[1:]))
 if t>T:T=t;print('\n'.join(''.join('.#'[b[y*w+x]>0]for x in range(w))for y in range(h)),j)
