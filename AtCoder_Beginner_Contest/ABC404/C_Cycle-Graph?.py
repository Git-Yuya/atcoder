N, M = map(int, input().split())

# 各頂点の辺
edges = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    edges[A - 1].append(B - 1)
    edges[B - 1].append(A - 1)

# 次数が2
for i in range(N):
    if len(edges[i]) != 2:
        print("No")
        exit()

# 各頂点の訪問状態
visited = [False] * N
# 1つ前の頂点
prev_v = 0

# 連結性
while True:
    visited[prev_v] = True
    next_v = -1

    for neighbor in edges[prev_v]:
        if not visited[neighbor]:
            next_v = neighbor
            break

    if next_v == -1:
        print("Yes" if all(visited) else "No")
        break

    prev_v = next_v


# ========== 別解 ==========
def all_connected(n: int, edges: list[tuple[int, int]]) -> bool:
    """
    連結かどうかを判定

    Args:
        n (int): 頂点の数
        edges (list[tuple[int, int]]): 辺のリスト

    Returns:
        bool: 連結ならTrue, そうでなければFalse
    """
    size = [1] * n
    parent = [i for i in range(n)]

    def find(x: int) -> int:
        """
        親をたどって根を見つける
        
        Args:
            x (int): 頂点のインデックス
        
        Returns:
            x (int): 根のインデックス
        """
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x 

    def union(x: int, y: int) -> None:
        """
        xとyを結合する
        
        Args:
            x (int): 頂点xのインデックス
            y (int): 頂点yのインデックス
        """
        if size[x] >= size[y]:
            size[x] += size[y]
            parent[y] = x 
        else:
            size[y] += size[x]
            parent[x] = y

    for x, y in edges:
        px = find(x)
        py = find(y)
        if px !=  py:
            union(px, py)

    for i in range(n):
        if size[i] == n:
            return True 

    return False


def has_cycle(n: int, edges: list[tuple[int, int]]) -> bool:
    """
    サイクルかどうかを判定

    Args:
        n (int): 頂点の数
        edges (list[tuple[int, int]]): 辺のリスト

    Returns:
        bool: サイクルであればTrue, そうでなければFalse
    """
    degree = [0] * n

    for u, v in edges:
        degree[u] += 1
        degree[v] += 1

    for i in range(n):
        if degree[i] != 2:
            return False

    return True


N, M = map(int, input().split())

edges = []
for _ in range(M):
    A, B = map(int, input().split())
    edges.append((A - 1, B - 1))

if N == M and all_connected(N, edges) and has_cycle(N, edges):
    print("Yes")
else:
    print("No")
