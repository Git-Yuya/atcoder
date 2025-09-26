N, M = map(int, input().split())
f = [int(input()) for _ in range(N)]

# dp[i]: サプリメントi個目まで摂取したときの選び方
dp = [0] * (N + 1)
dp[0] = 1

# dpの累積和
S = [0] * (N + 1)
S[0] = 1

# 各味の直近出現位置
last = [-1] * (M + 1)

# 直近で同じ味を摂取した位置+1
# 直近で同じ味を摂取した位置までのサプリメントは選べない
left = 0

MOD = 10 ** 9 + 7

for i in range(1, N + 1):
    # 現在の味
    current_f = f[i - 1]

    # 左端の更新
    if last[current_f] != -1:
        left = max(left, last[current_f] + 1)

    if left - 1 >= 0:
        # 条件を満たす区間の和
        dp[i] = (S[i - 1] - S[left - 1]) % MOD
    else:
        dp[i] = (S[i - 1]) % MOD

    S[i] = (S[i - 1] + dp[i]) % MOD
    last[current_f] = i - 1

print(dp[N] % MOD)
