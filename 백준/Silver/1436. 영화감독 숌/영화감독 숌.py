count=int(input())
arr = []

i=666
while True:
  if '666' in str(i):
    arr.append(i)
  if len(arr)==count:
    print(arr[count-1])
    break;
  i+=1