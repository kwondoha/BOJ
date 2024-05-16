m=int(input())
n=int(input())
arr=[]

for i in range(m, n+1):
  if not i == 1:
    arr.append(i)
  for j in range(2,i-1,1):
    if i%j == 0 :
      arr.remove(i)
      break

if len(arr) == 0:
  print(-1)
else:
  print(sum(arr))
  print(min(arr))