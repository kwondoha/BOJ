n=int(input())
log={}

for i in range(n):
  key,value=map(str,input().split())
  log[key]=value

log = dict(sorted(log.items(), reverse=True))

for key,value in log.items():
  if value=='enter':
    print(key)