n = int(input())

coord = []
for _ in range(n):
    coord.append(list(map(int, input().split())))

coord.sort(key = lambda x: (x[0], x[1]))

for i in range(n):
    print(coord[i][0], coord[i][1])
