import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
  d = input().split()
  if d[0] ==  '1' :
    stack.append(d[1])
  elif d[0] == '2' :
    if stack:
      sys.stdout.write(f"{stack.pop()}\n")
    else :
      sys.stdout.write("-1\n")
  elif d[0] == '3' :
      sys.stdout.write(f"{len(stack)}\n")
  elif d[0] == '4' :
    if stack:
      sys.stdout.write("0\n")
    else:
      sys.stdout.write("1\n")
  elif d[0] == '5' :
    if stack:
      sys.stdout.write(f"{stack[-1]}\n")
    else:
      sys.stdout.write("-1\n")