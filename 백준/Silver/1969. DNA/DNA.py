n, m = map(int, input().split())
dna = [input() for _ in range(n)]
acgt = ['A','C','G','T']
s=''
hd = 0

for j in range(m):
  a,t,g,c = 0,0,0,0
  for i in range(n):
    if dna[i][j] == 'A' :
      a+=1
    elif dna[i][j] == 'T' :
      t+=1
    elif dna[i][j] == 'G' :
      g+=1
    else :
      c+=1
  count = [a,c,g,t]
  s+=acgt[count.index(max(count))]

  for i in range(n):
    if dna[i][j] != acgt[count.index(max(count))] :
      hd+=1

print(s)
print(hd)