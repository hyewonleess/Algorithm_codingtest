# my solution
n, c = map(int, input().split())
nums = list(map(int, input().split()))

ss = []
for i in nums:
    s = []
    s.append(i)
    s.append(nums.count(i))
    s.append(nums.index(i))
    ss.append(s)
    
ss.sort(key = lambda x: (-x[1], x[2]))

for s in ss:
    print(s[0], end = " ")
    
    
    
# alternative solution
text = map(int, input().split())
num = list(map(int, input().split()))

num_count={}

for i in num:
    if i not in num_count:
        num_count[i]=1
    else:
        num_count[i]+=1

ans = sorted(num_count.items(), reverse=True, key=lambda x: x[1])

string = ""

for i in ans:
    string += (str(i[0]) + " ")*i[1]

print(string)
