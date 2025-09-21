import heapq

INF = 10 ** 18


def dijkstra(start, graph, n):
    # 始点から各頂点への最短距離
    dist = [INF] * n
    dist[start] = 0

    pq = [(0, start)]
    while pq:
        d, v = heapq.heappop(pq)
        if d > dist[v]:
            continue
        for nv, w in graph[v]:
            nd = d + w
            if nd < dist[nv]:
                dist[nv] = nd
                heapq.heappush(pq, (nd, nv))
    return dist


N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, t))
    graph[b].append((a, t))

ans = INF
for i in range(N):
    d = dijkstra(i, graph, N)
    ans = min(ans, max(d))

print(ans)


# ========== 別解 ==========
INF = 10 ** 18

N, M = map(int, input().split())

dist = [[INF] * N for _ in range(N)]

for _ in range(M):
    a, b, t = map(int, input().split())
    dist[a - 1][b - 1] = t
    dist[b - 1][a - 1] = t

for i in range(N):
    dist[i][i] = 0

# ワーシャルフロイド法
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

print(min(max(row) for row in dist))
