from collections import deque

n,k=map(int, input().split())
q=deque()
li = []

for i in range(1,n+1):
  q.append(i)

while q :
  for i in range(k-1):
    q.append(q.popleft())
  li.append(q.popleft())

print('<'+', '.join(map(str,li)),end='' +'>')