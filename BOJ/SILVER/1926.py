# dfs
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000000)


n, m = map(int, input().split())

pic = []
for _ in range(n):
    pic.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global cnt
    cnt += 1
    pic[x][y] = 0 # 방문처리
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and pic[nx][ny] == 1:
            dfs(nx, ny)


cnts = []
for i in range(n):
    for j in range(m):
        if pic[i][j] == 1:
            cnt = 0
            dfs(i, j)
            cnts.append(cnt)


print(len(cnts))
if len(cnts) == 0:
    print(0)
else:
    print(max(cnts))
    
    
# bfs
from collections import deque
n, m = map(int, input().split())

pic = []
for _ in range(n):
    pic.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    pic[x][y] = 0 # 방문처리
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and pic[nx][ny] == 1:
                q.append([nx, ny])
                pic[nx][ny] = 0
                cnt += 1
    return cnt

cnts = []
for i in range(n):
    for j in range(m):
        if pic[i][j] == 1:
            cnts.append(bfs(i, j))
            
print(len(cnts))

if len(cnts) == 0:
    print(0)
else:
    print(max(cnts))
