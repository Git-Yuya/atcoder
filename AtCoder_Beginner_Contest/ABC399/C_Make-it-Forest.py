from collections import defaultdict, deque

N, M = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 訪問済みかどうか
visited = [False] * (N + 1)
# 連結成分の数
components = 0

for i in range(1, N + 1):
    if not visited[i]:
        components += 1
        queue = deque([i])
        visited[i] = True

        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

# 森にするためには(連結成分の数 - 1)の辺を削除
print(M - (N - components))


# ========== 別解 ==========
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [i for i in range(N)]

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]  
        x = parent[x]
    return x

K = N  

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    root_u = find(u)
    root_v = find(v)
    if root_u != root_v:
        parent[root_v] = root_u
        K -= 1

print(M - (N - K))
