n,m = map(int, input().split())
arr = []

def bt(x):
  if len(arr)==m:
    print(*arr)
    return
  for i in range(x,n+1):
    if i not in arr:
      arr.append(i)
      bt(i+1)
      arr.pop()

bt(1)