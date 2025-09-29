N = int(input())

print((N + 1) // 2)

for _ in range(N // 2):
    print(2)

if N % 2 == 1:
    print(1)
