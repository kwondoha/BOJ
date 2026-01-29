from collections import deque

n=int(input())
arr = [input().strip() for _ in range(n)]

cnt=n
for i in range(n):
  q=deque()
  for j in range(len(arr[i])):
    if arr[i][j] not in q :
      q.append(arr[i][j])
    elif (arr[i][j] in q) and (arr[i][j-1] != arr[i][j]) :
      cnt-=1
      break

print(cnt)