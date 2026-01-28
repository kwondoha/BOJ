from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]

# 상하좌우 이동표현
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

q = deque([(0, 0)]) # 시작 위치를 큐에 삽입
while q:
    x, y = q.popleft() # 현재 위치를 큐에서 팝
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k] # 다음 좌표 계산
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1: # 이동 가능 and 미방문 체크
            grid[nx][ny] = grid[x][y] + 1 # 지나온 위치의 수
            q.append((nx, ny)) # 다음 위치를 큐에 삽입

print(grid[n-1][m-1])