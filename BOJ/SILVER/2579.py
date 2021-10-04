n = int(input())
s = []
for _ in range(n):
    s.append(int(input()))
    
d = [0]*(n+1)

d[1] = s[0]
for i in range(2, n+1):
    if i == 2:
        d[i] = s[i-1] + s[i-2]
    else:
        d[i] = max(d[i-2]+s[i-1], d[i-3]+s[i-2]+s[i-1])
    
print(d[n])
