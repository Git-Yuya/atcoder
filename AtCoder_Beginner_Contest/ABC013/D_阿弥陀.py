N, M, D = map(int, input().split())
A = list(map(int, input().split()))

# D=1のときの最終的な位置
pos = list(range(N))
for a in reversed(A):
    pos[a - 1], pos[a] = pos[a], pos[a - 1]

# ダブリングテーブル
# dbl[i][j]: jを2^i回操作した後の位置
log_max = 30
dbl = [[-1] * N for _ in range(log_max)]
dbl[0] = pos[:]
for i in range(1, log_max):
    for j in range(N):
        dbl[i][j] = dbl[i - 1][dbl[i - 1][j]]

# 各xについてD回操作した後の位置
ans = list(range(N))
for i in range(log_max):
    if (D >> i) & 1:
        for j in range(N):
            ans[j] = dbl[i][ans[j]]

for x in ans:
    print(x + 1)
