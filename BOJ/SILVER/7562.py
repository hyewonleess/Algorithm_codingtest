from collections import deque

t = int(input())
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    graph[x][y] = 0
    
    while q:
        x, y = q.popleft()
        if x == end[0] and y == end[1]:
            return graph[end[0]][end[1]]
            
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
                
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == -1:
                    q.append([nx, ny])
                    graph[nx][ny] = graph[x][y] + 1


for _ in range(t):
    n = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    graph = [[-1]*n for _ in range(n)]
    result = bfs(start[0], start[1])
    print(result)
