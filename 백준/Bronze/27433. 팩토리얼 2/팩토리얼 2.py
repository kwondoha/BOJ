n = int(input().strip())

def fac(n):
  if n == 0 or n == 1 :
    return 1
  return n * fac(n-1)

print(fac(n))