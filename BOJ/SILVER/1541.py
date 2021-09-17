eq = input()

result = 0
minus = eq.split('-')
sums = []
for m in minus:
    s = 0
    for i in m.split('+'):
        s += int(i)
    sums.append(s)

print(sums[0] - sum(sums[1:]))
