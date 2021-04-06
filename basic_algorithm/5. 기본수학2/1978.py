import math

n = int(input())
num_list = list(map(int, input().split()))

array = [True]*len(num_list)

for i, num in enumerate(num_list):
    if num == 1:
        array[i] = False
    for j in range(2, int(math.sqrt(num))+1):
        if num % j == 0:
            array[i] = False
            
print(sum(array))



# related codes: 소수 구하는 방법 두가지
def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def is_prime2(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
