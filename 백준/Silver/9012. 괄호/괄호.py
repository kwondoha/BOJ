n = int(input())

for _ in range(n):
  num=0
  stack=input()
  for i in stack:
    if num < 0 :
      break
    if i == '(' :
      num+=1
    elif i == ')' :
      num-=1
  if num == 0 :
    print('YES')
  else :
    print('NO')