from collections import deque

N = int(input())
a, b = map(int, input().split())
M = int(input())
edges = [[] for _ in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    edges[x - 1].append(y - 1)
    edges[y - 1].append(x - 1)

MOD = 10 ** 9 + 7

# aからの最短距離
dist = [-1] * N
dist[a - 1] = 0

# aからそれぞれの頂点への最短経路の数
count = [0] * N
count[a - 1] = 1

q = deque()
q.append(a - 1)

# BFS
while q:
    v = q.popleft()
    for nv in edges[v]:
        if dist[nv] == -1:
            dist[nv] = dist[v] + 1
            count[nv] = count[v]
            q.append(nv)

        elif dist[nv] == dist[v] + 1:
            count[nv] += count[v]
            count[nv] %= MOD

print(count[b - 1] % MOD)
