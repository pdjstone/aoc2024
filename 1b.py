from collections import defaultdict
la = []
lb = defaultdict(int)
for l in open('1'):
    a,b=map(int,l.split())
    la.append(a)
    lb[b]+=1
print(sum(a*lb[a] for a in la))