n,m = map(int,input().split())

arr1 = set(input() for _ in range(n))
arr2 = list(input() for _ in range(m))
cnt=0

for i in range(m):
  if arr2[i] in arr1:
    cnt+=1

print(cnt)