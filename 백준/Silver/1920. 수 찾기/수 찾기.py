import bisect

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
arr2 = list(map(int, input().split()))


for i in arr2:
  idx = bisect.bisect_left(arr, i)
  if idx < n and arr[idx] == i :
    print(1)
  else:
    print(0)