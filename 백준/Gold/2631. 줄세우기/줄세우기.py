n=int(input())
arr=[]

for i in range(n):
  arr.append(int(input()))

def LIS(arr):
  if not arr: return []
  dp = [1]*n
  pre = [-1]*n

  for i in range(1,n):
    for j in range(i):
      if arr[i] > arr[j] and dp[i] < dp[j] + 1:
        dp[i] = dp[j] + 1
        pre[i] = j

  mm = dp.index(max(dp))

  lis=[]
  while mm != -1:
    lis.append(arr[mm])
    mm = pre[mm]
  
  return len(lis)

print(n-LIS(arr))