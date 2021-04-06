m = int(input())
n = int(input())

num_list = list(range(m, n+1)) 
primes = []

for num in num_list:
    no_prime = 0
    if num <= 1:
        no_prime = 1
    for j in range(2, num):
        if num % j == 0:
            no_prime +=1
            break
    if no_prime == 0:
        primes.append(num)
    
if len(primes) > 0:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)
