n,m = map(int,input().split())
d = set(input() for _ in range(n))
b = set(input() for _ in range(m))

arr = d&b
arr=sorted(arr)
print(len(arr))

for i in arr:
  print(i)