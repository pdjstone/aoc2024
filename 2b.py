def pos(n):
    return n > 0

def neg(n):
    return n < 0

def in_limits(n):
    return 1 <= abs(n) <= 3
     
def safe(ns):
    diffs = [b-a for a,b in zip(ns[1:], ns[:-1])]
    return all(map(in_limits, diffs)) and (all(map(pos, diffs)) or all(map(neg, diffs)))

def safe_with_dampener(ns):
    return any((safe(x) for x in iter_remove_one_from_list(ns)))
        
def iter_remove_one_from_list(ns):
    for i in range(len(ns)):
        yield [n for j, n in enumerate(ns) if i != j]
   
total = 0
for line in open('2'):
    ns = [*map(int, line.split())]
    if safe(ns) or safe_with_dampener(ns):
        total += 1
print(total)
    