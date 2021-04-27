# 내 풀이
data = input()

import re

string = data
nums = re.findall('\d', data)
for i in nums:
    string = string.replace(i, "")
    
new_str = sorted(string)

result = ""; sums = 0
for i in new_str:
    result += i

for j in nums:
    sums += int(j)
    
print(result+str(sums))


# 해답
data = input()
result = []
value = 0

for i in data:
    if i.isalpha(): # 문자열여부 확인
        result.append(i)
    else:
        value += int(i)
        
result.sort()

if value != 0:
    result.append(str(value))
    
print(''.join(result))
