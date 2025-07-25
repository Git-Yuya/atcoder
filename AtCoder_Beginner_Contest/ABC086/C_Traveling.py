N = int(input())
txy = [[0, 0, 0]]
for _ in range(N):
    txy.append(list(map(int, input().split())))

# 旅行プランが可能かどうかのフラグ
is_traveled = True

# 順番に旅行プランが可能かを判定
for i in range(N):
    t_diff = txy[i + 1][0] - txy[i][0]
    xy_diff = abs(txy[i + 1][1] - txy[i][1]) + abs(txy[i + 1][2] - txy[i][2])

    if t_diff < xy_diff:
        is_traveled = False
        break
    else:
        if t_diff % 2 != xy_diff % 2:
            is_traveled = False
            break

print("Yes" if is_traveled else "No")


# ========== 別解 ==========
def solve() -> bool:
    """
    旅行プランが可能かどうかを判定

    Returns:
        bool: 旅行プランが可能かどうか
    """
    N = int(input())

    # 初期値
    pt, px, py = 0, 0, 0

    for _ in range(N):
        t, x, y = map(int, input().split())

        t_diff, x_diff, y_diff = t - pt, abs(x - px), abs(y - py)

        if t_diff < x_diff + y_diff:
            return False
        if t_diff % 2 != (x_diff + y_diff) % 2:
            return False

        # 一つ前の時間と座標を更新
        pt, px, py = t, x, y

    return True


print("Yes" if solve() else "No")
