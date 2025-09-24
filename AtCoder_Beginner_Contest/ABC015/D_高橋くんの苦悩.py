W = int(input())
N, K = map(int, input().split())

# dp[i][j]: 枚数がi枚以下で幅がj以下のときの重要度の最大値
dp = [[0] * (W + 1) for _ in range(K + 1)]

for _ in range(N):
    A, B = map(int, input().split())

    # 枚数と幅を逆順でループすることで、同じカードを複数回選ばないようにする
    for i in range(K, 0, -1):
        for j in range(W, A - 1, -1):
            dp[i][j] = max(dp[i][j], dp[i - 1][j - A] + B)

print(dp[K][W])
