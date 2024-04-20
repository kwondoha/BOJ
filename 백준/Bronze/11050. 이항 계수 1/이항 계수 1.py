import math
n,k=map(int, input().split())
nn=math.factorial(n)
kk=math.factorial(k)
nk=math.factorial(n-k)
print(nn//kk//nk)