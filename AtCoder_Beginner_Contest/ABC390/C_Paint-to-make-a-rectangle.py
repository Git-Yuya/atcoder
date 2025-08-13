H, W = map(int, input().split())
grid = [input() for _ in range(H)]

# 黒の外側の座標
min_left = W
max_right = 0
min_top = H
max_bottom = 0

for i in range(H):
    for j in range(W):
        if grid[i][j] == "#":
            min_left = min(min_left, j)
            max_right = max(max_right, j)
            min_top = min(min_top, i)
            max_bottom = max(max_bottom, i)

# 黒の範囲内で白がないか確認
for i in range(min_top, max_bottom + 1):
    for j in range(min_left, max_right + 1):
        if grid[i][j] == ".":
            print("No")
            exit()

print("Yes")
