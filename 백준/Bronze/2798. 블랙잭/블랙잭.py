N, M = map(int,(input().split()))
inp = list(map(int, input().split()))
result = 0
max = 0

for i in range(0,N-2):
  for j in range(i+1,N-1):
    for k in range(j+1,N):
      if inp[i]+inp[j]+inp[k]<=M:
        result=inp[i]+inp[j]+inp[k]
        if max<= result:
          max=result

print(max)