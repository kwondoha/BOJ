a,b = map(int, input().split())
c,d = map(int, input().split())

def func(a, b):
    while b != 0:
        a, b = b, a % b
    return a
  
arr=[]
arr.append(a*d+c*b)
arr.append(b*d)

e=func(arr[0], arr[1])
arr[0],arr[1]=arr[0]//e, arr[1]//e
print(*arr)