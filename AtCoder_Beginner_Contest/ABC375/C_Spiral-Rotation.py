N = int(input())
A =  [input() for _ in range(N)]
B = [["."] * N for _ in range(N)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        # 外側から何層目か
        layer = min(i, j, N - i + 1, N - j + 1)

        # 0~3回90度右回転させる
        x, y = i, j
        for _ in range(layer % 4):
            x, y = y, N + 1 - x
        B[x - 1][y - 1] = A[i - 1][j - 1]

for row in B:
    print("".join(row))


# ========== 別解 ==========
N = int(input())
A = [input() for _ in range(N)]

for i in range(1, N + 1):
    row = []

    for j in range(1, N + 1):
        # 何回90度右回転させるか
        count = min(i, j, N + 1 - i, N + 1 - j) % 4

        # 0~3回90度右回転させる前の座標
        if count == 0:
            row.append(A[i - 1][j - 1])
        elif count == 1:
            row.append(A[N - j][i - 1])
        elif count == 2:
            row.append(A[N - i][N - j])
        else:
            row.append(A[j - 1][N - i])

    print("".join(row))
