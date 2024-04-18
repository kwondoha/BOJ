from collections import deque

n = int(input())
deq = deque([i for i in range(1, n + 1)])
index = deque(map(int, input().split()))
result =[]

while deq:
  result.append(deq.popleft())
  x = index.popleft()
  if x > 0 :
    deq.rotate(-(x-1))
    index.rotate(-(x-1))
  else :
    deq.rotate(-x)
    index.rotate(-x)

print(*result)