import heapq

H, W, T = map(int, input().split())
s = [input() for _ in range(H)]

# スタートとゴールの位置
si, sj = -1, -1
gi, gj = -1, -1
for i in range(H):
    for j in range(W):
        if s[i][j] == "S":
            si, sj = i, j
        if s[i][j] == "G":
            gi, gj = i, j

left, right = 1, T + 1

# 二分探索
while right - left > 1:
    mid = (left + right) // 2
    dist = [[10 ** 9 + 1] * W for _ in range(H)]
    dist[si][sj] = 0

    # (距離, x, y)
    q = []
    heapq.heappush(q, (0, si, sj))

    # ダイクストラ法
    while q:
        d, x, y = heapq.heappop(q)
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < H and 0 <= ny < W:
                if s[nx][ny] == "#":
                    time = mid
                else:
                    time = 1

                # 距離の更新
                if dist[nx][ny] > d + time:
                    dist[nx][ny] = d + time
                    heapq.heappush(q, (dist[nx][ny], nx, ny))

    if dist[gi][gj] <= T:
        left = mid
    else:
        right = mid

print(left)
