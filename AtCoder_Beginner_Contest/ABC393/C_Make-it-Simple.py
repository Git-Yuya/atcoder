from collections import defaultdict

N, M = map(int, input().split())

# 自己ループの数
self_loops = 0
# 自己ループ以外の辺
edges = defaultdict(int)

for _ in range(M):
    u, v = map(int, input().split())
    if u == v:
        self_loops += 1
    elif u < v:
        edges[(u, v)] += 1
    else:
        edges[(v, u)] += 1

# 多重辺の数
multi_edges = 0
for count in edges.values():
    if count > 1:
        multi_edges += count - 1

print(self_loops + multi_edges)


# ========== 別解 ==========
N, M = map(int, input().split())

d = set()

ans = 0
for _ in range(M):
    u, v = map(int, input().split())
    if u > v:
        u, v = v, u
    if u == v or (u, v) in d:
        ans += 1
    else:
        d.add((u, v))

print(ans)
