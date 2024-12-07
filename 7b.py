from itertools import product


def ft(target,ns):
  
  for ops in product('+*|',repeat=len(ns)-1):
    total=ns[0]
    for op,n in zip(ops,ns[1:]):
      if op=='+':
        total+=n
      elif op=='*':
        total*=n
      else:
        total =int(str(total)+str(n))
      if total>=target:break
    if total==target:return 1
 

tot=0
for l in open('7'):
  t,ns=l.split(':')
  ns=map(int,ns.split())
  t=int(t)
  if ft(t,[*ns]):
   tot+=t
print(tot)
