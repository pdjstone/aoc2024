from itertools import product
from multiprocessing import Pool

def ft(l):
  t,ns=l.split(':') 
  ns=[*map(int,ns.split())]
  target=int(t) 
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
    if total==target:return target
  return 0
 

print(sum(Pool().map(ft,open('7'))))
 
