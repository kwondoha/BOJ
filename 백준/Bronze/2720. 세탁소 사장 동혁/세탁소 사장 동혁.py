t = int(input())
m = [25,10,5,1]
result = []

for i in range(t):
  n = int(input())

  for i in m:
    result.append(str(n//i))
    n %= i
  
print(*result)
