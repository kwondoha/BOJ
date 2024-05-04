while True :
  arr=list(map(int, input().split()))
  if set(arr) == {0} : break
  if max(arr) < sum(arr)-max(arr) :
    if len(set(arr))==1 :
      print('Equilateral')
    elif len(set(arr))==2 :
      print('Isosceles')
    else:
      print('Scalene')
  else :
    print('Invalid')