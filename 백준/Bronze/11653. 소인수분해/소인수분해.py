n=int(input())
m=2
while True:
  if n==1:
    break
  if n%m == 0:
    print(m)
    n=n/m
  else:
    m+=1