N, M = map(int, input().split())
B = sorted(list(map(int, input().split())), reverse=True)
W = sorted(list(map(int, input().split())), reverse=True)

# 白玉と黒玉の総和の最大値
max_sum = 0
# 黒玉の総和
sum_black = 0
# 白玉の総和
sum_white = 0
# 白玉の最大値
max_white = 0

for i in range(N):
    sum_black += B[i]
    if i < M:
        sum_white += W[i]
    max_white = max(max_white, sum_white)
    max_sum = max(max_sum, sum_black + max_white)

print(max_sum)


# ========== 別解 ==========
N, M = map(int, input().split())
B = sorted(list(map(int, input().split())), reverse=True)
W = sorted(list(map(int, input().split())), reverse=True)

ans = 0
for i in range(N):
    if i <= M - 1:
        if B[i] >= 0 and W[i] >= 0:
            ans += B[i] + W[i]
        elif B[i] >= 0 and W[i] < 0:
            ans += B[i]
        elif B[i] + W[i] > 0:
            ans += B[i] + W[i]
    else:
        if B[i] > 0:
            ans += B[i]

print(ans)
