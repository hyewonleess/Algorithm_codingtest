# 내 풀이
n, m = map(int, input().split())

dp = [10001] * (m+1)
coins = []
for i in range(n):
    coin = int(input())
    coins.append(coin)

for i in range(1, m+1):
    for j in coins:
        if i== j:
            dp[i] = 1
        if i > j and dp[i-j] != 10001:
            dp[i] = min(dp[i], dp[i-j] + 1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
    
    
# 해설
n, m = map(int, input().split())

dp = [10001] * (m+1)
coins = []
for i in range(n):
    coins.append(int(input()))

dp[0] = 0

for i in range(n): # 모든 화폐단위에 대해 for문
    for j in range(coins[i], m+1):
        if dp[j-coins[i]] != 10001:
            dp[j] = min(dp[j], dp[j-coins[i]]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
