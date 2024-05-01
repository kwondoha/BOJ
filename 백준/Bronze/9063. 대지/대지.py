n=int(input())
aa=[]
bb=[]
for i in range(n):
  a,b=map(int, input().split())
  aa.append(a)
  bb.append(b)

print((max(aa)-min(aa))*(max(bb)-min(bb)))