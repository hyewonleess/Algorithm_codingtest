# my solution: 148ms
import re

n = int(input())

nums = []
for _ in range(n):
    ls = []
    nu = input()
    ls.append(nu)
    ls.append(len(nu))
    nums.append(ls)
    
for nu in nums:
    s = 0
    num_str = re.findall("\d+", nu[0])
    num_str = ''.join(num_str)
    for i in num_str:
        s += int(i)
    nu.append(s)

nums.sort(key = lambda x: (x[1], x[2], x[0]))

for i in nums:
    print(i[0])
    
    
  
 # suggested solution - 사용자정의 함수를 이용하여 정렬
n = int(input())

def sum_num(s):
    su = 0
    for i in s:
        if i.isdigit():
            su += int(i)
    return su

nums = [input() for _ in range(n)]
nums.sort(key = lambda x: (len(x), sum_num(x), x))

for nu in nums:
    print(nu)
