from itertools import combinations as C
m = [*open('8')]
w = len(m)
m = ''.join(l[:-1] for l in m)
p = set()
for c in {*m}-{'.'}:
  for a,b in C((i for i in range(w*w) if m[i]==c), 2):
    ax = a%w; ay = a//w
    bx = b%w; by = b//w
    for i in range(-w,w):
      nx = ax + i * (bx-ax)
      ny = ay + i * (by-ay)
      if 0 <= nx < w and 0 <= ny < w:
        p|={nx*w+ny}
print(len(p))