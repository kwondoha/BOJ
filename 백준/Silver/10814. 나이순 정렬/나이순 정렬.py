n=int(input())
arr=[list(input().split()) for _ in range(n)]

for i in range(len(arr)):
  arr[i][0]=int(arr[i][0])

arr.sort(key=lambda x: x[0])

for i in arr:
  print(*i)