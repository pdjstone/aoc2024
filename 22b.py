
def nn(n):
  n=((n<<6)^n)&0xffffff
  n=((n>>5)^n)
  n=((n<<11)^n)&0xffffff
  return n

def ni(n):
  ln=n
  ds=[]
  for i in range(2000):
    n=nn(n)
    
    d=(n%10)-(ln%10)
    #print(n,n%10,d)
    ds+=[d]
    if len(ds)>4:
      ds.pop(0)
    if len(ds)>3:  
      yield tuple(ds),n%10
    ln=n
    
ns=(1,2,3,2024)
ns=map(int,open('22'))

p=0
allseqs=set()
ss=[]
for n in ns:
 seqs={}
 for ds,a in ni(n):
   if ds not in seqs:
     seqs[ds]=a
     allseqs.add(ds)
 ss+=[seqs]

bestscore=0
bestseq=None
for seq in allseqs:
  score=0
  for seqs in ss:
    score+=seqs.get(seq,0)
  if score>bestscore:
    bestscore=score
    
print(bestscore)
