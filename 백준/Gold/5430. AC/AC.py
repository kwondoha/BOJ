import sys

input = sys.stdin.readline
count_test=int(input())

def AC():
    deff=list(input())
    cnt_arr=int(input())
    arr=input().strip()[1:-1].split(',')

    if cnt_arr==0:
        arr=[]
        
    r=0
    er=False
    for i in range(len(deff)):
        if deff[i] == 'D':
            if len(arr)==0 :
                print("error")
                er=True
                break
            elif r%2==0 :
                arr.pop(0)
            elif r%2==1 :
                arr.pop()
        elif deff[i] == 'R':
            r+=1

    if not er:
        if r%2==1 :
            arr.reverse()
        print('[' + ','.join(arr) + ']')

for _ in range(count_test):
  AC()