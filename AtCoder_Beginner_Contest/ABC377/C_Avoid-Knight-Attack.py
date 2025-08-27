N, M = map(int, input().split())

# 置けないマス
invalid_squares = set()

for _ in range(M):
    a, b = map(int, input().split())
    invalid_squares.add((a, b))

    if a + 2 <= N and b + 1 <= N:
        invalid_squares.add((a + 2, b + 1))
    if a + 1 <= N and b + 2 <= N:
        invalid_squares.add((a + 1, b + 2))
    if 1 <= a - 1 and b + 2 <= N:
        invalid_squares.add((a - 1, b + 2))
    if 1 <= a - 2 and b + 1 <= N:
        invalid_squares.add((a - 2, b + 1))
    if 1 <= a - 2 and 1 <= b - 1:
        invalid_squares.add((a - 2, b - 1))
    if 1 <= a - 1 and 1 <= b - 2:
        invalid_squares.add((a - 1, b - 2))
    if a + 1 <= N and 1 <= b - 2:
        invalid_squares.add((a + 1, b - 2))
    if a + 2 <= N and 1 <= b - 1:
        invalid_squares.add((a + 2, b - 1))

print(N * N - len(invalid_squares))


# ========== 別解 ==========
N, M = map(int,input().split())

# 置けないマス
invalid_squares = set()
for _ in range(M):
    a, b = map(int,input().split())
    invalid_squares.add((a,b))

    for i in [-1, 1]:
        for j in [-2, 2]:
            invalid_squares.add((a + i, b + j))
            invalid_squares.add((a + j, b + i))

ans = N * N
for i, j in invalid_squares:
    if 1 <= i <= N and 1 <= j <= N:
        ans -= 1

print(ans)
