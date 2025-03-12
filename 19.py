p,q=open('19').read().split('\n\n')
p=p.split(', ')
p=sorted(p,key=len)

def m(s):
  #print(s)
  if s=='': return 1
  for prefix in usedparts:
    if s.startswith(prefix):
      #print(s,prefix)
      if m(s[len(prefix):]): return 1
  #print(s,'xxx')
  return 0

t=0
usedparts=[]
q=q.strip().split('\n')
for part in p:
  n=sum(1 for patt in q if part in patt)
  if n:
    usedparts.append(part)
print(len(p),len(usedparts))

print(usedparts)
for i,patt in enumerate(q):
  print(patt)

  a=m(patt)
  print(i,len(q),a)
  t+=a
  print('-----')

print(t)
