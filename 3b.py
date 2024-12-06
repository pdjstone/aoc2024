import re
domul=True
total=0
with open('3') as f:
  for m in re.findall(r"(do)\(\)|(don\'t)\(\)|(mul)\((\d+),(\d+)\)", f.read()):
      if m[0]:
          domul=True
      if m[1]:
          domul=False
      if m[2] and domul:
          total += int(m[3]) * int(m[4])
      print(m, domul, total)
print(total)