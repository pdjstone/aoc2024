m=map
def s(n):d=[y-x for x,y in zip(n[1:],n[:-1])];return all(m(lambda x:0<x*x<16,d))&(all(m(lambda x:x>0,d))|all(m(lambda x:x<0,d)))
print(sum(s(p)|any((s(x)for x in([x for i,x in enumerate(p)if i!=j]for j in range(len(p)))))for p in([*m(int,l.split())]for l in open('2'))))
