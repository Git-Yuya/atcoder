# 入力
N = int(input())
d = []
for _ in range(N):
    d.append(int(input()))

# 集合
d_set = set(d)

# 出力
print(len(d_set))




##### 別解 #####
# # 入力
# N = int(input())
# d = []
# for _ in range(N):
#     d.append(int(input()))

# # dを降順にソート
# d.sort(reverse=True)

# # 鏡餅の段数
# tiers = 1

# # 段数を計算
# for i in range(1, N):
#     if d[i - 1] > d[i]:
#         tiers += 1

# # 出力
# print(tiers)
