cor = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
arr = input()
cnt = 0

for c in cor:
  arr = arr.replace(c, '*')

for i in range(len(cor)):
  if cor[i] in arr:
    cnt+=1

print(len(arr) - cnt)