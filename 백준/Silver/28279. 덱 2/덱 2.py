import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
dq = deque()

for _ in range(n):
  c = input().split()
  if c[0] == '1' :
    dq.appendleft(c[1])
  elif c[0] == '2' :
    dq.append(c[1])
  elif c[0] == '3':
    if dq :
      print(dq.popleft())
    else :
      print(-1)
  elif c[0] == '4':
    if dq :
      print(dq.pop())
    else :
      print(-1)
  elif c[0] == '5':
    print(len(dq))
  elif c[0] == '6':
    if dq :
      print(0)
    else :
      print(
          1)
  elif c[0] == '7':
    if dq :
      print(dq[0])
    else :
      print(-1)
  elif c[0] == '8':
    if dq :
      print(dq[-1])
    else :
      print(-1)