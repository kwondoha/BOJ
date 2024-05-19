n=int(input())
arr=list(map(int,input().split()))

if n==1:
  print(arr[0]*arr[0])
else: 
  print(min(arr)*max(arr))