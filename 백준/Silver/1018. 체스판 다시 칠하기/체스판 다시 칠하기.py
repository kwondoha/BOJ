n,m = map(int, input().split())
board = []
count = []

for i in range(n):
  board.append(input())

for i in range(n-7):
  for j in range(m-7):
    b=0
    w=0
    for ii in range(i,i+8):
      for jj in range(j,j+8):
        if (ii+jj)%2==0:
          if board[ii][jj]=='B':
            w+=1
          else:
            b+=1 
        else:
          if board[ii][jj]=='B':
            b+=1
          else:
            w+=1

    count.append(w)
    count.append(b)

print(min(count))