# 1st solution: 164ms
n = int(input())
dist = list(map(int, input().split()))
gas = list(map(int, input().split()))
gas = gas[:-1]

current = gas[0]
currents = []

for g in gas:
    if current > g:
        current = g
    currents.append(current)
    
total = 0
for i in range(len(currents)):
    total += dist[i] * currents[i]
    
print(total)



# 2nd solution
n = int(input())
dist = list(map(int, input().split()))
gas = list(map(int, input().split()))
gas = gas[:-1]

current = gas[0]
total = 0

for i in range(len(gas)):
    if current > gas[i]:
        current = gas[i]
    total += current * dist[i]
    
print(total)
