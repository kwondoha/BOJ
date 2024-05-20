n=int(input())
arr=[]
sum=0
arr2=[]
for i in range(n):
  arr.append(input())

for i in arr:
  if i=='ENTER':
    sum+=len(set(arr2))
    arr2=[]
  else:
    arr2.append(i)

sum+=len(set(arr2))
print(sum)