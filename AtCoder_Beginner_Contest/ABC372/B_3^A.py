M = int(input())

A = []
while M > 0:
    for i in reversed(range(11)):
        if 3 ** i <= M:
            A.append(i)
            M -= 3 ** i
            break

print(len(A))
print(*A)
