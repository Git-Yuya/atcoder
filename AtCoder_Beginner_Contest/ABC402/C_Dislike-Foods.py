N, M = map(int, input().split())

# それぞれの食材がどの料理に使われているか
ingredients = [[] for _ in range(N)]
# 料理に含まれる苦手な食材の個数
dislike_count = [-1] * M

for m in range(M):
    K, *A = map(int, input().split())
    dislike_count[m] = K
    for ingredient in A:
        ingredients[ingredient - 1].append(m)

# 克服する食材
B = list(map(int, input().split()))
# 現在食べられる料理
current_foods = 0

for b in B:
    # 食材bを克服
    for food in ingredients[b - 1]:
        dislike_count[food] -= 1

        # 苦手な食材がなくなった料理があった場合
        if dislike_count[food] == 0:
            current_foods += 1

    print(current_foods)


# ========== 別解 ==========
N, M = map(int, input().split())
KA = [list(map(int, input().split())) for _ in range(M)]
B = list(map(int, input().split()))

# 各食材が克服された順番を記録
idx = [0] * (N + 1)
for i, e in enumerate(B):
    idx[e] = i + 1  # 食材eがBの何番目で克服されるか

# 各順番で新たに食べられるようになる料理の個数
cnt = [0] * (N + 1)
# 各料理について、克服された食材の中で一番遅い順番を調査
for lst in KA:
    ma = 0
    for i in lst[1:]:  # 料理に含まれる食材
        ma = max(ma, idx[i])  # その料理で一番遅く克服される食材の順番
    cnt[ma] += 1

ans = 0
# 各順番ごとに累積
for a in cnt[1:]:
    ans += a
    print(ans)
