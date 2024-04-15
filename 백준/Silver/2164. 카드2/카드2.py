from collections import deque

q = deque()
n=int(input())
for i in range(1,n+1):
  q.append(i)

while True:
  if len(q)==1:
    break
  q.popleft()
  if len(q)==1:
    break
  q.append(q.popleft())
print(q[0])