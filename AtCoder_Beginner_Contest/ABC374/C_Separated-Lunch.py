N = int(input())
K = list(map(int, input().split()))

# 割り当ての最小値
min_num = 20 * (10 ** 8)
# 全体の人数
sum_K = sum(K)

for i in range(1 << N):
    # 昼休みをとる部署の人数
    lunch = []
    for j in range(N):
        if i & (1 << j):
            lunch.append(K[j])

    # 昼休みをとる合計人数
    sum_lunch = sum(lunch)
    # グループA,Bの大きい方
    large_AB = max(sum_lunch, sum_K - sum_lunch)

    min_num = min(min_num, large_AB)

print(min_num)


# ========== 別解 ==========
import itertools
import bisect

N = int(input())
K = list(map(int, input().split()))

# リストを2つに分割
K1 = K[:N//2]
K2 = K[N//2:]

def subset_sums(arr):
    """
    部分集合の和を列挙
    """
    sums = []
    for i in range(len(arr) + 1):
        for comb in itertools.combinations(arr, i):
            sums.append(sum(comb))
    return sums

# K1とK2の部分集合の和をそれぞれ列挙
sums1 = subset_sums(K1)
sums2 = subset_sums(K2)
sums2.sort()

# 全体の人数
sum_K = sum(K)

# 合計人数の半分に近い部分和を探索
half_sum = sum_K // 2
best_diff = float("inf")
best_total = 0

# sums1の各要素に対して、sums2の中で最適な組み合わせを二分探索
for s1 in sums1:
    # 目標値
    target = half_sum - s1
    # sums2でtargetに最も近い値を探す
    idx = bisect.bisect_left(sums2, target)

    # sums2[idx]を確認
    if idx < len(sums2):
        s2 = sums2[idx]
        current_total = s1 + s2
        diff = abs(sum_K - 2 * current_total)
        if diff < best_diff:
            best_diff = diff
            best_total = current_total

    # sums2[idx-1]も確認
    if idx > 0:
        s2 = sums2[idx - 1]
        current_total = s1 + s2
        diff = abs(sum_K - 2 * current_total)
        if diff < best_diff:
            best_diff = diff
            best_total = current_total

print(max(best_total, sum_K - best_total))
