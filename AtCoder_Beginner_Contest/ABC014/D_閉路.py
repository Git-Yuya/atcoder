import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    x, y = map(int, input().split())
    graph[x - 1].append(y - 1)
    graph[y - 1].append(x - 1)
Q = int(input())

# dbl[i][j]: 頂点jの2^i個親
log_N = N.bit_length()
dbl = [[-1] * N for _ in range(log_N)]

# 頂点0を根としたときの各頂点の深さ
depth = [-1] * N

def dfs(v, p, d):
    depth[v] = d
    dbl[0][v] = p
    for nv in graph[v]:
        if nv == p:
            continue
        dfs(nv, v, d + 1)
dfs(0, -1, 0)

# ダブリングテーブルの構築
for i in range(1, log_N):
    for v in range(N):
        if dbl[i - 1][v] != -1:
            dbl[i][v] = dbl[i - 1][dbl[i - 1][v]]
        else:
            dbl[i][v] = -1

def lca(u, v):
    # uをvより深い位置にする
    if depth[u] < depth[v]:
        u, v = v, u

    # uをvと同じ深さまで引き上げる
    for i in range(log_N - 1, -1, -1):
        if ((depth[u] - depth[v]) >> i) & 1:
            u = dbl[i][u]

    if u == v:
        return u

    # uとvを同じ高さまで引き上げる
    for i in range(log_N - 1, -1, -1):
        if dbl[i][u] != dbl[i][v]:
            u = dbl[i][u]
            v = dbl[i][v]
    return dbl[0][u]

for _ in range(Q):
    a, b = map(int, input().split())
    common_ancestor = lca(a - 1, b - 1)
    dist = depth[a - 1] + depth[b - 1] - 2 * depth[common_ancestor] + 1
    print(dist)
