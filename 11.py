from collections import*
p={n:1 for n in map(int,open('11').read().split())}
for i in range(75):
 q=defaultdict(int)
 for n,c in p.items():
  s=str(n);l=len(s)
  if n<1:q[1]+=c
  elif l%2==0:q[int(s[:l//2])]+=c;q[int(s[l//2:])]+=c
  else:q[n*2024]+=c
 p=q
print(sum(q.values()))