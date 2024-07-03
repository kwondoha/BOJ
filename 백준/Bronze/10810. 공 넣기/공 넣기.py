n, m = map(int,input().split())
basket = [0] * n

for i in range(m):
    i, j, k = map(int,input().split())
    for x in range(i - 1, j):
        basket[x] = k

basket = map(str,basket)
print(*basket)