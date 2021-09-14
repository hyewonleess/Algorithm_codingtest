# 1st solution: 76ms
n, k = map(int, input().split())
coins = []

for i in range(n):
    coins.append(int(input()))

count = 0

for val in reversed(coins): # 큰 값부터 차례로 탐색
    if val <= k: # 동전 값이 k보다 작은 경우만 시행
        count += k // val # 현재 남은 k 값을 동전 값으로 나눈 몫
        k -= (k // val) * val # k 값 업데이트
    
    if k == 0: # k = 0 일 때 break
        break

print(count)





# 2nd solution: 58ms
n, k = map(int, input().split())
coins = []

for i in range(n):
    coins.append(int(input()))
    
count = 0

while k > 0: # k 가 0이 되면 while 문 break
    coin = coins.pop() # coins 리스트에서 가장 마지막 값(큰 값)부터 pop으로 추출 - 리스트에서 자동 삭제
    count += k// coin # k 보다 큰 값들은 알아서 count 가 0으로 들어감 - 1st solution 처럼 if 로 따로 처리 할 필요성 없음
    k %= coin # k 값 

print(count)
