# my solution: 시간초과
n = int(input())

nums = []
for _ in range(n):
    nums.append(int(input()))
    
uni = list(set(nums))

counts = []
for u in uni:
    counts.append(nums.count(u))

idx = counts.index(max(counts))
print(uni[idx])



# alternative solution - 딕셔너리 이용
import sys
t = sys.stdin.readline()
n = int(t)

nums = {}
for _ in range(n):
    nu = int(input())
    if nu in nums:
        nums[nu] += 1
    else:
        nums[nu] = 1

nums = sorted(nums.items(), key = lambda x: (-x[1], x[0]))
print(nums[0][0])
