arr = []
arr.append(int(input()))
arr.append(int(input()))
arr.append(int(input()))

if sum(arr) == 180 :
  if len(set(arr))==1 :
    print('Equilateral')
  elif len(set(arr))==2 :
    print('Isosceles')
  else:
    print('Scalene')
else :
  print('Error')