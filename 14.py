import re
w=101
h=103
i=100
mw=w//2
mh=h//2
s=[0]*4   
for l in open('14'):
  x,y,vx,vy=map(int,re.findall(r'-?\d+',l))
  vx=(w+vx)%w
  vy=(h+vy)%h
  x=(x+vx*i)%w
  y=(y+vy*i)%h
  if x==mw or y==mh: continue
  s[[0,1][x>mw]+[0,2][y>mh]]+=1
a,b,c,d=s
print(a*b*c*d)
