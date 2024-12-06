import re;m=1;t=0;mul=lambda x,y:x*y*m
for d,c in re.findall("(do(?:n't)?)\(\)|(mul\(\d+,\d+\))",open('3').read()):
 m=d=='do'if d else m
 if c:t+=eval(c)
print(t)