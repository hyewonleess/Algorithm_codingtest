n = int(input())
food = list(map(int, input().split()))

dp = [0]*(n+1)
dp[1] = food[1]

for i in range(2, n+1):
    dp[i] = max(dp[i-1], dp[i-2] + food[i-1])
    
print(dp[n])
