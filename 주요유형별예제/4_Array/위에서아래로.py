# 기본정렬문제
n = int(input())
num_list = []
for _ in range(n):
    num_list.append(int(input()))
    
num_list.sort(reverse = True)

for i in num_list:
    print(i, end = ' ')
