from collections import deque

n = int(input())

h = []
for _ in range(n):
    h.append(list(map(int, input())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    h[x][y] = 0
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<n and h[nx][ny] == 1:
                h[nx][ny] = 0
                cnt += 1
                q.append([nx, ny])
    return cnt

cnts = []

for i in range(n):
    for j in range(n):
        if h[i][j] == 1:
            cnts.append(bfs(i, j))
            
cnts.sort()

print(len(cnts))
for i in cnts:
    print(i)
