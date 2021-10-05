def solution(n, wine):
    d = [0]*(n+1)
    d[1] = wine[0]
    for i in range(2, n+1):
        if i == 2:
            d[i] = d[i-1] + wine[i-1]
        else:
            d[i] = max(d[i-2]+wine[i-1], d[i-3]+wine[i-2]+wine[i-1], d[i-1])
    return d[n]

n = int(input())
wine = []
for _ in range(n):
    wine.append(int(input()))
solution(n, wine)
