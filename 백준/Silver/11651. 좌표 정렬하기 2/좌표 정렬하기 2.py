n=int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
matrix.sort(key=lambda x: (x[1], x[0]))
for i in matrix:
    print(*i)