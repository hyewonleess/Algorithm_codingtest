# 유형: Greedy Algorithm

nums = input()
to_zero = 0; to_one = 0

if nums[0] == '1':
    to_zero += 1
else:
    to_one += 1
    

for i in range(len(nums)-1):
    if nums[i] != nums[i+1]:
        if nums[i+1] == '1':
            to_zero +=1
        elif nums[i+1] == '0':
            to_one += 1
            
print(min(to_zero, to_one))
