import decimal
import sys
input=sys.stdin.readline

context=decimal.getcontext()
context.rounding=decimal.ROUND_HALF_UP
b=[]

n=int(input())
arr=[]

for i in range(n):
  arr.append(int(input()))

arr=sorted(arr)

a=round(decimal.Decimal(sum(arr)/n),0)

dic=dict()
for i in range(n):
  if arr[i] in dic.keys():
    dic[arr[i]]=dic.get(arr[i])+1
  else:
    dic[arr[i]]=1

b=[]
for key, value in dic.items():
  if value == max(dic.values()):
    b.append(key)

print(0 if a == -0 else a)
print(arr[(n//2)])
print(b[1] if len(b) != 1 else b[0])
print(abs(arr[-1]-arr[0]))