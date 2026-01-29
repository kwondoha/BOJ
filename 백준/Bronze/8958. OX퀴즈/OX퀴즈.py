t=int(input())
for _ in range(t):
  arr=list(str(input().strip()))
  sum=0
  s=0
  for i in range(len(arr)):
    if arr[i] == 'O':
      s+=1
      sum+=s
    else:
      s=0
  print(sum)