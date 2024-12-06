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
def isword(x,y,w,d):
 for ww in  (w,w[::-1]):
  l=0
  for i,c in enumerate(ww):
   if m(x,y,d,i)==c:
    l+=1
  if l==len(ww):
   return 1
 return 0

def mas(x,y):
  return isword(x-1,y-1,"MAS",(1,1)) and isword(x+1,y-1,"MAS",(-1,1))

t=0
for y in range(len(board)):
  for x in range(len(board[0])):
    n=mas(x,y)
    if n:
     print(x,y,n)
    t+=n
print(t)

