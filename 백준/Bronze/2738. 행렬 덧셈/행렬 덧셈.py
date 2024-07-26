n, m = map(int, input().split())
first_matrix = []
second_matrix = []

for i in range(n):
    f = list(map(int, input().split()))
    first_matrix.append(f)
    
for i in range(n):
    s = list(map(int, input().split()))
    second_matrix.append(s)

for i in range(n):
    for j in range(m):
        result = first_matrix[i][j] + second_matrix[i][j]
        print(result, end = " ")
    print()