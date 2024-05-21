n=int(input())
arr=[]
arr.append('ChongChong')
for i in range(n):
  a,b=input().split()
  if a in arr and b in arr:
    continue
  elif b in arr:
    arr.append(a)
  elif a in arr:
    arr.append(b)
  
print(len(set(arr)))