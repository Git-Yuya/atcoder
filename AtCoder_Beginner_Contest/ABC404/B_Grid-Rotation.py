N = int(input())
S = [list(input().strip()) for _ in range(N)]
T = [list(input().strip()) for _ in range(N)]

min_count = N ** 2

for i in range(4):
    # 90度右回転
    if i >= 1:
        S = [list(row) for row in zip(*S[::-1])]

    # SとTの異なるセルの数
    diff_cell = sum(1 for r in range(N) for c in range(N) if S[r][c] != T[r][c])

    min_count = min(min_count, diff_cell + i)

print(min_count)
