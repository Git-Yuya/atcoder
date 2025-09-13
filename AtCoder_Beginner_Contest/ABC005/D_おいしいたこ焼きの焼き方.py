N = int(input())
D = [[0 for _ in range(N)]] + [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
P = [int(input()) for _ in range(Q)]

# 累積和
prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix_sum[i][j] = D[i][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

# 面積ごとの美味しさの最大値
max_values = [0] * (N ** 2 + 1)
for a in range(1, N + 1):
    for b in range(1, N + 1):
        for c in range(a, N + 1):
            for d in range(b, N + 1):
                area = (c - a + 1) * (d - b + 1)
                total = prefix_sum[c][d] - prefix_sum[a - 1][d] - prefix_sum[c][b - 1] + prefix_sum[a - 1][b - 1]
                max_values[area] = max(max_values[area], total)

# 面積が大きいほど値が大きくなるように前処理
for i in range(1, N ** 2 + 1):
    max_values[i] = max(max_values[i], max_values[i - 1])

for p in P:
    print(max_values[p])
