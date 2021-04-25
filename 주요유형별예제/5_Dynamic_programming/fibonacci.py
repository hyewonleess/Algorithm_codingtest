# top-down
nums = [0]*100
def fibo(n):
    if n == 1 or n == 2:
        return 1
    
    if nums[n] != 0:
        return nums[n]
    
    nums[n] = fibo(n-1) + fibo(n-2)
    
    return nums[n]
  
  
# bottom-up
nums = [0]*100

nums[1] = 1
nums[2] = 1
n = 99

for i in range(3, n+1):
    nums[i] = nums[i-1] + nums[i-2]
    
print(nums[n])
