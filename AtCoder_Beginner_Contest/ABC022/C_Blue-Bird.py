N, M = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    u, v, l = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append((v, l))
    edges[v].append((u, l))

# 各頂点から各頂点への最短距離
dist = [[float("inf")] * N for _ in range(N)]

for i in range(N):
    dist[i][i] = 0
for u in range(N):
    for v, l in edges[u]:
        dist[u][v] = min(dist[u][v], l)

# ワ―シャルフロイド法
for k in range(1, N):
    for i in range(1, N):
        for j in range(1, N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

min_dist = float("inf")

# 頂点1に隣接する2つの頂点
for v1, l1 in edges[0]:
    for v2, l2 in edges[0]:
        if v1 == v2:
            continue
        min_dist = min(min_dist, l1 + dist[v1][v2] + l2)

print(min_dist if min_dist != float("inf") else -1)
