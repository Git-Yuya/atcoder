N = int(input())
d = []
for _ in range(N):
    d.append(int(input()))

d_set = set(d)

print(len(d_set))


# ========== 別解 ==========
N = int(input())
d = []
for _ in range(N):
    d.append(int(input()))

# 降順にソート
d.sort(reverse=True)

# 鏡餅の段数
tiers = 1

# 段数を計算
for i in range(1, N):
    if d[i - 1] > d[i]:
        tiers += 1

print(tiers)
