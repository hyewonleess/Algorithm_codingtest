import sys
n = int(sys.stdin.readline())


lst = []
for _ in range(n):
    s = sys.stdin.readline().split()
    
    if s[0] == 'push':
        lst.append(s[1])
        
    elif s[0] == 'pop':
        if not lst:
            print(-1)
        else:
            print(lst.pop())
            
    elif s[0] == 'size':
        print(len(lst))
        
    elif s[0] == 'empty':
        if not lst:
            print(1)
        else:
            print(0)
            
    elif s[0] == 'top':
        if not lst:
            print(-1)
        else:
            print(lst[-1])
