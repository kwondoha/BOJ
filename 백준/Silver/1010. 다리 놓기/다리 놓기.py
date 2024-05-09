t=int(input())
def fac(x) :
    if x == 0:
      return 1
    else:
      return x * fac(x - 1)

for i in range(t) :
  n,m=map(int, input().split())
  print(fac(m)//(fac(n)*fac(m-n)))