N, M = map(int, input().split())

# 各壁が砲台で守られている数（最後の壁はダミー）
count = [0] * (N + 1)

# いもす法
for _ in range(M):
    L, R = map(int, input().split())
    count[L - 1] += 1
    count[R] -= 1

# 累積和を計算
for i in range(1, N + 1):
    count[i] += count[i - 1]

print(min(count[:-1]))
