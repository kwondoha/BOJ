n=int(input())
arr=list(map(int, input().split()))

arr2=arr
arr=list(set(arr))
arr.sort()

index_map = {value: index for index, value in enumerate(arr)}
arr2_mapped = [index_map[value] for value in arr2]

print(*arr2_mapped)