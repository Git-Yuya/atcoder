# 入力
s = list(input())

# ビー玉が置かれるマスの数
count = 0

# 1が書かれたマスの数をカウント
for si in s:
    if int(si) == 1:
        count += 1

# 出力
print(count)




##### 別解 #####
# # 入力
# s = input()

# # 文字列から1の数をカウント
# count = s.count("1")

# # 出力
# print(count)
