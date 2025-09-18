N = int(input())
A = [int(input()) for _ in range(N)]

max_1 = max(A)
max_2 = -1

for a in A:
    if a != max_1:
        max_2 = max(max_2, a)

print(max_2)
