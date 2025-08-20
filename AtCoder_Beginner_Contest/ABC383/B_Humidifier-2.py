H, W, D = map(int, input().split())
S = [input() for _ in range(H)]

# 加湿されるマスの最大値
max_humidified = 0

for h in range(H):
    for w in range(W):
        if S[h][w] == ".":
            for h2 in range(H):
                for w2 in range(W):
                    if S[h2][w2] == ".":
                        # 加湿されているかどうか
                        is_humidified = [[False] * W for _ in range(H)]

                        for dh in range(h - D, h + D + 1):
                            for dw in range(w - D, w + D + 1):
                                if (0 <= dh < H) and (0 <= dw < W):
                                    if S[dh][dw] == "." and abs(dh - h) + abs(dw - w) <= D:
                                        is_humidified[dh][dw] = True

                        for dh2 in range(h2 - D, h2 + D + 1):
                            for dw2 in range(w2 - D, w2 + D + 1):
                                if (0 <= dh2 < H) and (0 <= dw2 < W):
                                    if S[dh2][dw2] == "." and abs(dh2 - h2) + abs(dw2 - w2) <= D:
                                        is_humidified[dh2][dw2] = True

                        # 加湿されるマスの数をカウント
                        humidified_count = sum(row.count(True) for row in is_humidified)
                        max_humidified = max(max_humidified, humidified_count)

print(max_humidified)


# ========== 別解 ==========
H, W, D = map(int, input().split())
S = [input() for _ in range(H)]

# 床のマス
floor = []
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            floor.append((i, j))

floor_num = len(floor)
covered = []
for i in range(floor_num):
    x1, y1 = floor[i]
    mask = 0
    # 各床マスについて、加湿器を置いたときに加湿される床マスをビットで表現
    for j in range(floor_num):
        x2, y2 = floor[j]
        if abs(x1 - x2) + abs(y1 - y2) <= D:
            mask |= 1 << j
    covered.append(mask)

# 2つの床マスの組み合わせで、加湿される床マスの最大数を求める
max_humidified = 0
for i in range(floor_num):
    for j in range(i + 1, floor_num):
        combined = covered[i] | covered[j]
        count = bin(combined).count("1")
        if count > max_humidified:
            max_humidified = count

print(max_humidified)
