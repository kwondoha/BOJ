n,m = list(map(int, input().split()))
arr = []

def bf():
  if len(arr)==m:
    print (*arr)
  for i in range(1,n+1):
    if i not in arr:
      arr.append(i)
      bf()
      arr.pop()

bf()