N, M = map(int, input().split())

X = 0
for i in range(M + 1):
    X += N ** i

print(X if X <= 10 ** 9 else "inf")
