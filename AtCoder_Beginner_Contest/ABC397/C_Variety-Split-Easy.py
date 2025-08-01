from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

# 各数字のインデックスを記録
indices = defaultdict(list)
for i, a in enumerate(A):
    indices[a].append(i)

# いもす法
# インデックスの累積和
cum_sum = [0] * N
for _, index_list in indices.items():
    cum_sum[index_list[0]] += 1
    cum_sum[index_list[-1]] -= 1

for i in range(1, N):
    cum_sum[i] += cum_sum[i - 1]

# 分割点
split_index = cum_sum.index(max(cum_sum))

print(len(set(A[:split_index + 1])) + len(set(A[split_index + 1:])))


# ========== 別解 ==========
N = int(input())
A = list(map(int, input().split()))

# 全種類数
alls = 0
# いもす法のためのリスト
imos = [0] * N
# 各数字の最後に出現したインデックスを記録
R = [-1] * N

for i, a in enumerate(A):
    # 初めての数字が出た場合
    if R[a - 1] == -1:
        imos[i] += 1
        alls += 1

    # 最後に出現したインデックスを記録
    R[a - 1] = i

# 各数字の最後の出現位置でimosをデクリメント
for i in range(N):
    imos[R[i]] -= 1

# 最大値と累積値
mx = acc = 0
# いもす法で累積和を計算し、最大値を求める
for i in range(N):
    acc += imos[i]
    mx = max(mx, acc)

print(alls + mx)


# ========== 別解 ==========
N = int(input())
A = list(map(int, input().split()))

max_variety = 0
left_set = set()
right_set = set()
left_variety = [0] * N
right_variety = [0] * N

# 左側の分割点ごとの種類数
for i in range(N - 1):
    left_set.add(A[i])
    left_variety[i] = len(left_set)

# 右側の分割点ごとの種類数
for i in reversed(range(1, N)):
    right_set.add(A[i])
    right_variety[i] = len(right_set)

# 分割点ごとに最大値を求める
for i in range(N - 1):
    max_variety = max(max_variety, left_variety[i] + right_variety[i + 1])

print(max_variety)
