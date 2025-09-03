from collections import defaultdict
from itertools import permutations

N = int(input())
M_G = int(input())
edges_G = [set() for _ in range(N)]
for _ in range(M_G):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    edges_G[u].add(v)
    edges_G[v].add(u)

M_H = int(input())
edges_H = [set() for _ in range(N)]
for _ in range(M_H):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    edges_H[a].add(b)
    edges_H[b].add(a)

A_dict = defaultdict(int)
for i in range(N - 1):
    A_list = list(map(int, input().split()))
    for j in range(i + 1, N):
        A_dict[(i, j)] = A_list[j - i - 1]

# 支払う金額の最小値
min_money = float("inf")

# pはグラフGの頂点の並び替え
for p in permutations(range(N)):
    money = 0

    for i in range(N):
        for j in range(i + 1, N):
            # GにあってHにない場合
            if (p[i] in edges_G[p[j]]) and (i not in edges_H[j]):
                money += A_dict[(i, j)]
            # GになくてHにある場合
            if (p[i] not in edges_G[p[j]]) and (i in edges_H[j]):
                money += A_dict[(i, j)]

    min_money = min(min_money, money)

print(min_money)
