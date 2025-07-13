N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    Ai, Bi = map(int, input().split())
    # 頂点Aiに隣接する頂点Biを追加
    G[Ai - 1].append(Bi - 1)
    # 頂点Biに隣接する頂点Aiを追加
    G[Bi - 1].append(Ai - 1)


def dfs(s: int) -> list[int]:
    """
    深さ優先探索を用いて、頂点sから各頂点への最短距離を求める関数

    Args:
        s (int): 探索を開始する頂点

    Returns:
        dist (list[int]): 頂点sから各頂点への距離
    """
    # 頂点sからの距離
    dist = [-1] * N
    dist[s] = 0

    st = [s]
    while st:
        v = st.pop()
        # 頂点vに隣接する各頂点nv
        for nv in G[v]:
            # nvが未探索の場合
            if dist[nv] == -1:
                st.append(nv)
                dist[nv] = dist[v] + 1

    return dist


# 頂点0からの最大距離の頂点を一つ選ぶ
dist_0 = dfs(0)
mv = max(enumerate(dist_0), key=lambda x: x[1])[0]

# 頂点mvからの最大距離
dist_mv = dfs(mv)

print(max(dist_mv) + 1)


# ========== 別解 ==========
import sys
from collections import deque


def check():
    def input_fn():
        return sys.stdin.readline().rstrip()
    N = int(input_fn())
    # N個の頂点を持つグラフの隣接リスト
    edges = [[] for _ in range(N)]
    # グラフの辺情報
    for _ in range(N - 1):
        a, b = map(int, input_fn().split())
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)

    # 各頂点がまだ探索されていないかどうかを示すリスト
    yet = [True] * N
    # 頂点0は訪問済み
    yet[0] = False
    # キューを初期化
    q = deque([(0, 0)])
    # 最も遠い頂点とその距離を記録する変数を初期化
    far_node = dis = 0

    # 頂点0から最も遠い頂点を探索
    while q:
        # キューから次の頂点と距離を取得
        node, cnt = q.popleft()
        # 現在の距離がこれまでの最大距離を上回った場合
        if dis < cnt:
            far_node = node
            dis = cnt

        # 現在の頂点nodeに隣接する頂点
        for nx in edges[node]:
            # まだ訪問されていない頂点がある場合
            if yet[nx]:
                yet[nx] = False
                q.append((nx, cnt + 1))

    yet = [True] * N
    yet[far_node] = False
    q = deque([(far_node, 0)])

    # 頂点far_nodeから最も遠い頂点の距離disを計算
    while q:
        node, cnt = q.popleft()
        if dis < cnt:
            dis = cnt
        for nx in edges[node]:
            if yet[nx]:
                yet[nx] = False
                q.append((nx, cnt + 1))

    print(dis + 1)


check()
