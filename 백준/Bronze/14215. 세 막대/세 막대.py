arr=list(map(int, input().split()))
if max(arr) < sum(arr)-max(arr) :
  print(sum(arr))
else :
  print((sum(arr)-max(arr))*2-1)