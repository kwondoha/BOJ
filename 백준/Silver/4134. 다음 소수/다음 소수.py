cnt = int(input())

def prime(num):
  if num <= 1:
    return False
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      return False
  return True

for x in range(cnt):
  m = int(input())
  if m == 0 or m == 1:
    print(2)
  for i in range(m, m * m):
    if prime(i) == True:
      print(i)
      break