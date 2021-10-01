from collections import deque

m, n = map(int, input().split())

tom = []
q = deque()

for i in range(n):
    tom.append(list(map(int, input().split())))
    
    for j in range(m):
        if tom[i][j] == 1:
            q.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
    
def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and tom[nx][ny] == 0:
                tom[nx][ny] = tom[x][y] + 1
                q.append([nx, ny])
                
bfs()
days = 0


# 출력 1
for i in tom:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    days = max(days, max(i))
    
print(days-1)

# 출력 2
iszero = False
for i in tom:
    for j in i:
        if j == 0:
            iszero = True
    days = max(days, max(i))

if iszero == False:
    print(days-1)
elif iszero == True:
    print(-1)
