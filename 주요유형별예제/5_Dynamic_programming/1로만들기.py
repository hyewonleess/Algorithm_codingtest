n = int(input())
dp = [0 for _ in range(n+1)]

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1 # 1을 빼는 경우
    
    if i%2 == 0: # 2의 배수
        dp[i] = min(dp[i//2]+1, dp[i])
    
    if i%3 == 0: # 3의 배수
        dp[i] = min(dp[i//3]+1, dp[i])
        
    if i%5 == 0: # 5의 배수
        dp[i] = min(dp[i//5]+1, dp[i])

print(dp[n])
