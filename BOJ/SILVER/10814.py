n = int(input())

info = []
for i in range(n):
    info.append(list(input().split()))

info.sort(key = lambda x: int(x[0])) # 문제에서 주어진대로 반드시 정수로 변환 후 정렬!

for i in range(n):
    print(info[i][0], info[i][1])
