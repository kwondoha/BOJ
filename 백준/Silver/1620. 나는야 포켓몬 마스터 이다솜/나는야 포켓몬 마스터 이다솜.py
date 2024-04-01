n,m = map(int,input().split())
dogam={}
test=[]

for i in range(n):
  dogam[i+1]=input()

for i in range(m):
  test.append(input())

dogam2={v:k for k,v in dogam.items()}

for i in test:
  if i.isdigit():
    print(dogam[int(i)])
  else:
    print(dogam2[i])