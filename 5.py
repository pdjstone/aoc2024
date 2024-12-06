o=[]
t=0 
for l in open('5'):
  l=l.strip()
  if '|' in l:
    o.append([*map(int,l.split('|'))])
  elif l:
    ns=[*map(int,l.split(','))]
    if all(ns.index(a)<ns.index(b)for a,b in o if a in ns and b in ns):
     t+=ns[len(ns)//2]
print(t)
