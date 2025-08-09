N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

missing = []
for i in range(1, N + 1):
    if i not in A:
        missing.append(i)

print(len(missing))
print(*missing)
