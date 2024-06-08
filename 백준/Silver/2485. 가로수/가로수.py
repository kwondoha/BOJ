def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
arr = [int(input()) for _ in range(n)]

di = abs(arr[1] - arr[0])
for i in range(2, n):
    di = gcd(di, abs(arr[i] - arr[i - 1]))

diff = arr[-1] - arr[0]
cnt = diff // di

print(cnt - n + 1)