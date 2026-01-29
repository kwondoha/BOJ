#2667
from collections import deque

n=int(input())
grid = [list(map(int, input().strip())) for _ in range(n)]

def bfs(gird,x,y):
  #상하좌우 이동표현
  dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
  q = deque([(x,y)]) # 시작 위치를 큐에 삽입
  grid[x][y] = 0
  cnt = 1

  while q:
      x, y = q.popleft() # 현재 위치를 큐에서 팝

      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
          grid[nx][ny] = 0
          q.append((nx,ny))
          cnt+=1
  return cnt
      

count = [bfs(grid, i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
print(len(count))
count.sort()
for i in range(len(count)) : print(count[i])