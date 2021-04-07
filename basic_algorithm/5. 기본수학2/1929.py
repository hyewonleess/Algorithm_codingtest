# 에라토스테네스의 채 활용
m, n = map(int, input().split())

array = [True for _ in range(n+1)]
array[1] = False

for i in range(2, int(n**0.5)+1):
    if array[i] == True:
        j = 2
        while i*j <= n:
            array[i*j] = False
            j += 1

for i in range(m, n+1):
    if array[i] == True:
        print(i)
