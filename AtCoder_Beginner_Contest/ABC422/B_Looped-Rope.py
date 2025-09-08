H, W = map(int, input().split())
S = [input() for _ in range(H)]

is_ok = True

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            # 上下左右で隣り合うクロのマスの数
            count = 0

            if i > 0 and S[i - 1][j] == "#":
                count += 1
            if i < H - 1 and S[i + 1][j] == "#":
                count += 1
            if j > 0 and S[i][j - 1] == "#":
                count += 1
            if j < W - 1 and S[i][j + 1] == "#":
                count += 1

            if not (count == 2 or count == 4):
                is_ok = False
                break

print("Yes" if is_ok else "No")
