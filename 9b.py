ns=[*map(int,[*open('9').read().strip()+'0'])]
pos=0
l=sum(ns)
print(l)
b=[-1]*l
files=[]
for fid,(size,gap) in enumerate(zip(ns[::2],ns[1::2])):
  b[pos:pos+size]=[fid]*size
  files.append((pos,size))
  pos+=size+gap

while fid>=0:
  pos,size=files[fid]
  s=0
  p=0
  fp=-1
  for i in range(l):
   if b[i]==-1:
    s+=1
    if fp==-1:
     fp = i
   else:
    s=0
    fp=-1
   if s==size:break
  if fp>=0 and fp<pos:
   b[fp:fp+size]=[fid]*size
   b[pos:pos+size]=[-1]*size
  fid-=1
print(sum(i*fid for i,fid in enumerate(b) if fid>=0))

