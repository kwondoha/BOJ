a,b = map(int, input().split())

def d(a, b):
    while b:
        a, b = b, a % b
    return a

print(a*b//d(a, b))