print(sum(abs(b-a)for a,b in zip(*map(sorted,zip(*(map(int,l.split())for l in open('1')))))))
