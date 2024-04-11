while True :
  string = input()
  arr=[]

  if string == '.' :
      break

  for s in string :
    if s != ' ' :
      arr.append(s)

  stack=[]
  check=True
  for i in arr :
    if i == '(' or i == '[' :
      stack.append(i)
    elif i == ')' :
      if stack and stack[-1] == '(' :
        stack.pop()
      else :
        check=False
        break
    elif i == ']' :
      if stack and stack[-1] == '[' :
        stack.pop()
      else :
        check=False
        break
        
  if check and not stack :
    print('yes')
  else :
    print('no')