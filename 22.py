
def nn(n):
  n=((n<<6)^n)&0xffffff
  n=((n>>5)^n)
  n=((n<<11)^n)&0xffffff
  return n
ns=(1,10,100,2024)
ns=map(int,open('22'))

p=0
for n in ns:
 for i in range(2000):
  n=nn(n)
 p+=n

print(p)
