while True:
  a,b=map(int, input().split())
  if a==0 :
    break
  elif b//a*a==b :
    print('factor')
  elif a//b*b==a :
    print('multiple')
  else:
    print('neither')