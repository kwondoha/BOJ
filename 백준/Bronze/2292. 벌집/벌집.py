n = int(input())
x = 1
cnt = 1

while n > x:
    x += (cnt * 6)
    cnt += 1

print(cnt)