from collections import*
c=defaultdict(set)
p=set()
for l in open('23'):
  l=l.strip()
  a,b=l.split('-')
  c[a].add(b)
  c[b].add(a)
  p.add((a,b))
  
bigger=set()
bg=2
while 1:
  for t in p: 
    ns=c[t[0]].copy()
    for n in t:
      ns&=c[n]
    ns-=set(t)
  
    if not ns:
      continue
    for n in ns:
      nt=tuple(sorted([*t,n]))
      bigger.add(nt)

  if not bigger:
    break
  print(len(list(bigger)[0]))
  p=bigger
  bigger=set()

  
print(','.join(sorted(list(p)[0])))
