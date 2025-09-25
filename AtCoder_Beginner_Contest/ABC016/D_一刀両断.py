A_x, A_y, B_x, B_y = map(int, input().split())
N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

# 交点の数
count = 0

for i in range(N):
    C_x, C_y = XY[i]
    D_x, D_y = XY[(i + 1) % N]

    # ベクトルABとベクトルCDの外積
    cross1 = (B_x - A_x) * (C_y - A_y) - (B_y - A_y) * (C_x - A_x)
    cross2 = (B_x - A_x) * (D_y - A_y) - (B_y - A_y) * (D_x - A_x)
    cross3 = (D_x - C_x) * (A_y - C_y) - (D_y - C_y) * (A_x - C_x)
    cross4 = (D_x - C_x) * (B_y - C_y) - (D_y - C_y) * (B_x - C_x)

    # 交差判定
    if cross1 * cross2 < 0 and cross3 * cross4 < 0:
        count += 1

print(count // 2 + 1)
