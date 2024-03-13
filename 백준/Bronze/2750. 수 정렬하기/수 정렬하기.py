count = int(input())
arr = []

for i in range(count):
  arr.append(int(input()))

for i in range(count-1):
  for j in range(i+1,count):
    if arr[i]>arr[j]:
      temp=arr[i]
      arr[i]=arr[j]
      arr[j]=temp
      
for i in range(count):
  print(arr[i])