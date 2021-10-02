from collections import deque

n = int(input())

col = []

for _ in range(n):
    col.append(list(input()))


visited = [[0]*n for _ in range(n)] 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
                if col[x][y] == col[nx][ny]:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
    return visited

# 적록색약 아닌 경우
cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt, end = ' ')

# 적록색약
for i in range(n):
    for j in range(n):
        if col[i][j] == 'G':
            col[i][j] = 'R'
visited = [[0]*n for _ in range(n)] 
            
cnt2 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt2 += 1
print(cnt2)
