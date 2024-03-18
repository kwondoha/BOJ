n=str(input())
arr=[]
for i in n:
  arr.append(i)

arr=sorted(arr,reverse=True)
arr=''.join(map(str, arr))
print(int(arr))