n,m = map(int, input().split())
arr = []

def bt(x):
  if len(arr)==m:
    print(*arr)
    return
  for i in range(x,n+1):
    arr.append(i)
    bt(i)
    arr.pop()

bt(1)