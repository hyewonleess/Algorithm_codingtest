from collections import deque
n = int(input())


que = deque()
for _ in range(n):
    s = input().split()
    
    if s[0] == 'push':
        que.append(s[1])
        
    elif s[0] == 'pop':
        if not que:
            print(-1)
        else:
            print(que.popleft())
            
    elif s[0] == 'size':
        print(len(que))
        
    elif s[0] == 'empty':
        if not que:
            print(1)
        else:
            print(0)
            
    elif s[0] == 'front':
        if not que:
            print(-1)
        else:
            print(que[0])
    
    elif s[0] == 'back':
        if not que:
            print(-1)
        else:
            print(que[-1])
