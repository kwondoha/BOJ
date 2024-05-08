import sys
from collections import deque
input = sys.stdin.readline

n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split())) 
m=int(input())
c=list(map(int, input().split()))

index = [i for i in range(n) if a[i] == 0]
deq = deque(b[i] for i in index)
deq.extendleft(c)

for i in range(len(index)):
  b[index[i]] = deq.popleft()

deq.reverse()
print(*deq)