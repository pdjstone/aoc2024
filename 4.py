board=[*open('4')]
def b(x,y):
 if x<0 or y<0:
  return None
 try:
  return board[y][x]
 except:
  return None
def m(x,y,d,l):
  dx,dy=d
  return b(x+dx*l,y+dy*l)
def isxmas(x,y,d):
 for i,c in enumerate("XMAS"):
  if m(x,y,d,i) != c:
   return 0
 return 1
def cx(x,y):
 return sum((isxmas(x,y,d)for d in dirs))

dirs=((1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1))

t=0
for y in range(len(board)):
  for x in range(len(board[0])):
    n=cx(x,y)
    if n:
     print(x,y,n)
    t+=n
print(t)

