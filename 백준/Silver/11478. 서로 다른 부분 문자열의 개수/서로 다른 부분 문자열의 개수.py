arr=[]
string=input()
n=len(string)

for i in range(n):
  for j in range(i+1,n+1):
    arr.append(string[i:j])
    
print(len(set(arr)))