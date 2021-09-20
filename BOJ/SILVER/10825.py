n = int(input())

score = []
for _ in range(n):
    inp = input().split()
    score.append([inp[0], int(inp[1]), int(inp[2]), int(inp[3])])
    
score.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for sc in score:
    print(sc[0])
