w,g=open('24').read().split('\n\n')

ops={' AND ':'&',' XOR ':'^',' OR ':'|'}

knowns={}
instrs=[]
for l in w.split('\n'):
  n,v=l.strip().split(': ')
  knowns[n]=int(v)

for g in g.strip().split('\n'):
  i,o=g.split(' -> ')
  for op,no in ops.items():
    if op in i:
      a,b=i.split(op)
      break
  instrs.append((o,a,no,b))

print(knowns)
nextinstrs=[]
while instrs:
 for output,in1,op,in2 in instrs:
   if in1 in knowns and in2 in knowns:
     in1v=knowns[in1]
     in2v=knowns[in2]
     knowns[output]=eval(f'{in1v}{op}{in2v}')
   else:
     nextinstrs.append((output,in1,op,in2))
 instrs=nextinstrs
 nextinstrs=[]  

val=0
for k,v in knowns.items():
  if k[0]!='z':continue
  s=int(k[1:])
  val|=v<<s
print(val)
