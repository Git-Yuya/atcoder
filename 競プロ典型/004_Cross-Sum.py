# 入力
H, W = map(int, input().split())
A = []
for _ in range(H):
    A.append(list(map(int, input().split())))

# 各行の合計
row_sums = [sum(A[i]) for i in range(H)]
# 各列の合計
col_sums = [sum(A[i][j] for i in range(H)) for j in range(W)]

for i in range(H):
    for j in range(W):
        cross_sum = row_sums[i] + col_sums[j] - A[i][j]
        print(cross_sum, end=" ")
    print()




##### 別解 #####
# 入力
# H, W = map(int, input().split())
# table = [[int(i) for i in input().split()] for _ in range(H)]

# # 各列の合計
# col_sums = [sum(col_values) for col_values in zip(*table)]

# for row in table:
#     # 現在の行の合計
#     row_sum = sum(row)
#     # 行と列の合計から交差する部分を差し引いた値
#     cross_sum = [str(row_sum + col_sums[col_idx] - row[col_idx]) for col_idx in range(len(col_sums))]
#     # 出力
#     print(" ".join(cross_sum))
