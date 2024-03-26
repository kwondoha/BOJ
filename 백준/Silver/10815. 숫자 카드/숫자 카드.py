n=int(input())
card = set(map(int,input().split()))
m=int(input())
card2 = list(map(int,input().split()))
arr = [1 if x in card else 0 for x in card2]

print(*arr)