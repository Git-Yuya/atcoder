N = int(input())

grid = [["?" for _ in range(N)] for _ in range(N)]

for i in range(1, N + 1):
    j = N + 1 - i
    if i <= j:
        if i % 2 == 1:
            for k in range(i, j + 1):
                for l in range(i, j + 1):
                    grid[k - 1][l - 1] = "#"
        else:
            for k in range(i, j + 1):
                for l in range(i, j + 1):
                    grid[k - 1][l - 1] = "."

for row in grid:
    print("".join(row))


# ========== 別解 ==========
N = int(input())

grid = [["."] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        # 外側からの距離が偶数である場合
        if min(i, j, N - i - 1, N - j - 1) % 2 == 0:
            grid[i][j] = "#"

for row in grid:
    print("".join(row))
