import sys
from collections import deque, Counter

sys.setrecursionlimit(10 ** 9)

class Dinic:
    """
    Dinicのアルゴリズムを用いて最大流を求めるクラス。

    1. BFSで始点からの距離（レベル）を計算し、層状のグラフ（レベルグラフ）を作成
    2. DFSでレベルグラフ上でフローを流せる経路（増加パス）を探し、可能な限りフローを流す
    3. 1と2を、増加パスが見つからなくなるまで繰り返す
    """
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = {v: Counter() for v in range(num_vertices)}
        self.level = dict()  # 各頂点のレベル（始点からの距離）
        self.it = dict()     # 各頂点の探索済みの隣接頂点のインデックス

    def add_edge(self, u, v, capacity):
        # 順方向の辺を追加
        self.graph[u][v] += capacity
        # 逆方向の辺を追加（容量0で初期化）
        self.graph[v][u] += 0

    def _bfs(self, source, sink):
        self.level = {i: -1 for i in range(self.num_vertices)}
        dq = deque([source])
        self.level[source] = 0

        while len(dq) > 0:
            u = dq.popleft()
            for v in self.graph[u]:
                if (self.level[v] < 0) and (self.graph[u][v] > 0):
                    self.level[v] = self.level[u] + 1
                    dq.append(v)

        # sinkに到達可能かどうか
        return self.level[sink] != -1

    def _dfs(self, u, sink, flow):
        if u == sink:
            return flow

        for v in list(self.graph[u].keys())[self.it[u]:]:
            self.it[u] += 1
            if (self.level[u] < self.level[v]) and (self.graph[u][v] > 0):
                min_flow = flow if flow < self.graph[u][v] else self.graph[u][v]
                pushed_flow = self._dfs(v, sink, min_flow)

                if pushed_flow > 0:
                    self.graph[u][v] -= pushed_flow
                    self.graph[v][u] += pushed_flow
                    return pushed_flow
        return 0

    def max_flow(self, source, sink):
        total_flow = 0
        while self._bfs(source, sink):
            self.it = {i: 0 for i in range(self.num_vertices)}
            while True:
                flow = self._dfs(source, sink, float("inf"))
                if flow == 0:
                    break
                total_flow += flow
        return total_flow


N, M, E = map(int, input().split())
p = list(map(int, input().split()))
ab = [tuple(map(int, input().split())) for _ in range(E)]

dinic = Dinic(N + 1)
for a, b in ab:
    dinic.add_edge(a, b, 1)
    dinic.add_edge(b, a, 1)
for pi in p:
    dinic.add_edge(pi, N, 1)

source, sink = 0, N
max_flow = dinic.max_flow(source, sink)

print(max_flow)
