from collections import*
c=defaultdict(set)
p=set()
for l in open('23'):
  l=l.strip()
  a,b=l.split('-')
  c[a].add(b)
  c[b].add(a)
  p.add((a,b))

triples=set()
for a,b in p:
  third=c[a]&c[b]
  for n in third:
    t=tuple(sorted([a,b,n]))
    triples.add(t)

w=set()
for t in triples:
  for n in t:
    if n[0]=='t':
      w.add(t)
      break
print(w)
print(len(w))
