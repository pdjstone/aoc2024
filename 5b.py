o=[]
t=0
def ok(ns,os):
  return all((ns.index(a)<ns.index(b)for a,b in os if a in ns and b in ns))

 
for l in open('5'):
  l=l.strip()
  if '|' in l:
    o.append([*map(int,l.split('|'))])
  elif l:
    ns=[*map(int,l.split(','))]
    if ok(ns,o):continue
    while not ok(ns,o):
      for a,b in o:
        if a in ns and b in ns:
          ia=ns.index(a)
          ib=ns.index(b)
          if ia>ib:
            ns[ia]=b
            ns[ib]=a
    t+=ns[len(ns)//2]

print(t)
