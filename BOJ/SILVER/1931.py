n = int(input())

times = []
for i in range(n):
    times.append(list(map(int, input().split())))

# Step 1: 정렬 시작 - 시작 시간 먼저 정렬 후, 끝나는 시간 정렬
# (1, 10) -> (10, 10) 인 경우 둘 다 회의 추가 가능하지만, (10, 10) -> (1, 10) 이면 회의 추가 못하므로 "시작 시간"에 대한 정렬을 미리 해야함
times = sorted(times, key = lambda a: a[0])
times = sorted(times, key = lambda a: a[1])

# Step 2: 시작시간이 마지막으로 끝난 시간보다 늦으면 회의 가능
count = 0; last = 0
for start, end in times:
    if start >= last:
        count += 1
        last = end

print(count)
