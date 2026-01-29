a=int(input())
b=int(input())
c=int(input())

arr = list(map(int, str(a*b*c).strip()))
cnt = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(arr)):
  cnt[arr[i]]+=1
for i in range(10):
  print(cnt[i])