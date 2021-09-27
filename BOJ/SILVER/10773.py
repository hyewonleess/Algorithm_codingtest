n = int(input())

nums = []
for _ in range(n):
    nu = int(input())
    if nu == 0:
        nums.pop()
    else:
        nums.append(nu)

print(sum(nums))
