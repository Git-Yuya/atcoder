# 入力
A = int(input())
B = int(input())
C = int(input())
X = int(input())

# 合計金額
total = 0
# 硬貨の選び方
count = 0

# 各硬貨を1枚ずつ増やす
for a in range(A + 1):
    total = 500 * a
    if total > X:
        break
    for b in range(B + 1):
        total = 500 * a + 100 * b
        if total > X:
            break
        for c in range(C + 1):
            total = 500 * a + 100 * b + 50 * c
            if total > X:
                break
            elif total == X:
                count += 1

# 出力
print(count)      




##### 別解 #####
# # 入力
# A = int(input())
# B = int(input())
# C = int(input())
# X = int(input())

# # 硬貨の選び方
# count = 0

# # 500円と100円を選んだ状態の合計金額に応じてカウント
# for i in range(A + 1):
#     for j in range(B + 1):
#         y = 500 * i + 100 * j
#         if (y < X) and (C > 0) and ((X - y) / 50 <= C):
#             count += 1
#         elif y == X:
#             count += 1
#             break

# # 出力
# print(count)
