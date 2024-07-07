n = int(input())
arr = list(map(int, input().split()))

m = max(arr)
for i in range(n):
  arr[i] = float(arr[i]) / float(m) *100

print(sum(arr) / len(arr))