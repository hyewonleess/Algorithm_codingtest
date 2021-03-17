from collections import deque

n, m = map(int, input().split())
map = [list(map(int, input())) for _ in range(n)]

def bfs(x, y):
  # bfs -  queue 구조 
  queue = deque()
  queue.append((x, y))
  
  # 이동방향 설정
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  while queue:
    x, y = queue.popleft()
    
    # (x, y)의 상하좌우 탐색
    for i in  range(4):
      new_x = x + dx[i]
      new_y = y + dy[i]
      
      # 범위 벗어나면 pass
      if new_x < 0 or new_x >= n or new_y < 0 or new_y >=m:
        continue
      
      # 괴물 있는경우(0) pass
      if map[new_x][new_y] == 0:
        continue

      if map[new_x][new_y] == 1:
        map[new_x][new_y] = map[x][y] + 1 # 이동거리 1씩 추가
        queue.append((new_x, new_y))

    return map[n-1][m-1] 

print(bfs(0, 0))
