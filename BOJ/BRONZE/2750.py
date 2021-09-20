n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
    
nums.sort()
for i in nums:
    print(i)
    
# 또는 join 이용하여 출력
print('\n'.join(map(str, nums)))
