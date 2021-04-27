n = input()

num = int(n[0])

for i in range(1, len(n)):
    if int(n[i]) <= 1:
        num += int(n[i])
    else:
        num *= int(n[i])
print(num)
