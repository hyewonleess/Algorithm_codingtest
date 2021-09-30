from collections import deque

n, m = map(int, input().split())

route = []
for I in range(n):
    route.append(list(map(int, input())))
    
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y)) # 큐에 삽입
    
    while q: # q가 비어있을 때까지 반복
        x, y = q.popleft() # 큐에서 제거
        for i in range(4):
            nx = x + dx[i] # 상하좌우 탐색
            ny = y + dy[i]
            
            if nx <= -1 or nx >= n or ny <=-1 or ny >=m: # 범위 벗어나면 패스
                continue
            
            if route[nx][ny] == 0: # 0이면 이동 불가하므로 패스
                continue
            
            if route[nx][ny] == 1: # 1이면 이동 가능하므로
                route[nx][ny] = route[x][y] + 1 # 루트 + 1
                q.append((nx, ny)) # 큐에 추가하여 방문처리
    return route[n-1][m-1]

print(bfs(0, 0))
