_ = int(input())
card = map(int,input().split())
_ = int(input())
card2 = map(int,input().split())

hash = {}
for n in card:
    if n in hash:
        hash[n] += 1
    else:
        hash[n] = 1

arr=[]
for i in card2:
  if i in hash:
    arr.append(hash[i])
  else:
    arr.append(0)

print(*arr)