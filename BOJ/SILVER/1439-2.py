nums = input()

groups = 1
count = []
count0 = 0

for i in range(len(nums)-1):
    count0 += 1
    if nums[i] != nums[i+1]: # 그룹 달라짐
        groups += 1 # 그룹 개수 추가
        count.append(count0)
        count0 = 0

print(groups//2)
