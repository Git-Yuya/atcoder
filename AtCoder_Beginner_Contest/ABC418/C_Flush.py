import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

# Aの累積和
prefix_sum = [0]
for a in A:
    prefix_sum.append(prefix_sum[-1] + a)

for _ in range(Q):
    B = int(input())

    max_A = A[-1]
    if B > max_A:
        print(-1)
        continue

    # A[i] < B-1 となる最大のiを探索
    idx = bisect.bisect_left(A, B - 1)
    # A[0..idx-1]はA[i]をそのまま使い、A[idx..N-1]はB-1を使う
    sum_min = prefix_sum[idx] + (N - idx) * (B - 1)

    print(sum_min + 1)


# ========== 別解 ==========
import sys
input = lambda: sys.stdin.readline().strip()

N, Q = map(int, input().split())
A = list(map(int, input().split()))

# Aの合計値
sum_A = sum(A)
# Aの値の最大値を仮定
m = 10 ** 6

# 各値ごとの出現回数をカウントする配列
c = [0] * (m + 1)
for i in A:
    c[i] += 1

# 各Bに対する答えを格納する配列
ans = [-1] * (m + 1)
# 累積和
s = 0

for i in range(1, m + 1):
    # i未満は元のAの値、i以上はi-1にする場合の最小値の和+1
    ans[i] = s + (i - 1) * N + 1
    # 合計値がAの合計を超える場合は-1
    if ans[i] > sum_A:
        ans[i] = -1
    # 累積和を更新
    s += i * c[i]
    # iの個数分Nを減らす
    N -= c[i]

for _ in range(Q):
    B = int(input())
    print(ans[B])
