from collections import deque

H, W, D = map(int, input().split())
S = [list(input()) for _ in range(H)]

visited = [[False] * W for _ in range(H)]
dq = deque()

# 加湿器がある場所をキューに追加
for i in range(H):
    for j in range(W):
        if S[i][j] == "H":
            dq.append([i, j, 0])

ans = 0

# 幅優先探索
while dq:
    x, y, d = dq.popleft()

    # 距離がDを超えたらスキップ
    if d > D:
        continue
    # すでに訪問済みならスキップ
    if visited[x][y]:
        continue

    visited[x][y] = True
    ans += 1

    # 上下左右に移動
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_x, next_y = x + dx, y + dy
        # 範囲外または訪問済みならスキップ
        if not (0 <= next_x < H and 0 <= next_y < W) or visited[next_x][next_y]:
            continue
        # 壁ならスキップ
        if S[next_x][next_y] == "#":
            continue
        # 次のマスをキューに追加
        dq.append([next_x, next_y, d + 1])

print(ans)
