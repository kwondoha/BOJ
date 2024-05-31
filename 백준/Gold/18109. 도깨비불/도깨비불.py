#18109
arr=input()
arr=list(arr)

i=0
while i <len(arr)-1: #중성 정리
  if arr[i] == 'h' and arr[i+1] in ['k','o','l']:
    arr[i]='h'+arr[i+1]
    del(arr[i+1])
    i+=2
  elif arr[i] == 'n' and arr[i+1] in ['j','p','l']:
    arr[i]='n'+arr[i+1]
    del(arr[i+1])
    i+=2
  elif arr[i] == 'm' and arr[i+1] == 'l':
    arr[i]='m'+arr[i+1]
    del(arr[i+1])  
    i+=2
  else:
    i+=1


first=['r','R','s','e','E','f','a','q','Q','t','T','d','w','W','c','z','x','v','g']
second=['k','o','i','O','j','p','u','P','h','hk','ho','hl','y','n','nj','np','nl','b','m','ml','l']
third=['r', 'R', 'rt', 's', 'sw', 'sg', 'e', 'f', 'fr', 'fa', 'fq', 'ft', 'fx', 'fv', 'fg', 'a', 'q', 'qt', 't', 'T', 'd', 'w', 'c', 'z', 'x', 'v', 'g']

cnt_sec = sum(1 for i in arr if i in second) #모음의 개수

do=0

i=0
while i <len(arr)-2: #종성 정리
  if arr[i] == 'r' and arr[i+1] == 't' and (arr[i+2] in first or arr[i+2] == ' '):
    arr[i]=arr[i]+arr[i+1]
    del(arr[i+1])
    i+=2
  elif arr[i] == 's' and arr[i+1] in ['w','g'] and (arr[i+2] in first or arr[i+2] == ' '):
    arr[i]=arr[i]+arr[i+1]
    del(arr[i+1])
    i+=2   
  elif arr[i] == 'f' and arr[i+1] in ['r','a','q','t','x','v','g'] and (arr[i+2] in first or arr[i+2] == ' '):
    arr[i]=arr[i]+arr[i+1]
    del(arr[i+1])
    i+=2 
  elif arr[i] == 'q' and arr[i+1] == 't' and (arr[i+2] in first or arr[i+2] == ' '):
    arr[i]=arr[i]+arr[i+1]
    del(arr[i+1])
    i+=2
  else:
    i+=1

#마지막 받침이 쌍받침 또는 겹받침인 경우
if (arr[-1] == 't' and arr[-2] in ['r','q']) or (arr[-1] in ['w','g'] and arr[-2] == 's') :
  arr[-2]=arr[-2]+arr[-1]
  del(arr[-1])
elif (arr[-1] in ['r','a','q','t','x','v','g'] and arr[-2] == 'f'):
  arr[-2]=arr[-2]+arr[-1]
  del(arr[-1])

for i in range(len(arr)-2):
  if arr[i-1] in first and arr[i] in second and arr[i+1] in third and arr[i+2] in second:
    do+=1
  elif arr[i] == 'r' and arr[i+1] == 't' and arr[i+2] in second:
    do+=1
  elif arr[i] == 's' and arr[i+1] in ['w','g'] and arr[i+2] in second:
    do+=1
  elif arr[i] == 'f' and arr[i+1] in ['r','a','q','t','x','v','g'] and arr[i+2] in second:
    do+=1
  elif arr[i] == 'q' and arr[i+1] == 't' and arr[i+2] in second:
    do+=1

print(do)