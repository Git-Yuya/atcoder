# 入力
N = int(input())
S = [input() for _ in range(N)]

# 文字列の長さの最大値
M = max(len(s) for s in S)
# Tを"*"のみで初期化
T = [["*"] * N for _ in range(M)]

# TにSの文字を代入
for i in range(N):
    for j in range(len(S[i])):
        T[j][N - i - 1] = S[i][j]

for i in range(M):
    # Tの末尾の"*"を削除
    while T[i][-1] == "*":
        T[i].pop()

    # 出力
    print("".join(T[i]))




##### 別解 #####
# # 入力
# N = int(input())
# S = [input() for _ in range(N)]

# # 文字列の長さの最大値
# M = max(len(s) for s in S)
# # 各文字列に対して、Mに足りない部分を"*"で補間
# S = [s + "*" * (M - len(s)) for s in S]

# T = []
# # 各文字列の同じインデックスの文字をまとめてタプルにしてTに追加
# for a in zip(*S):
#     T.append(a)
# # 各タプルを文字列に結合
# T = ["".join(t) for t in T]

# for t in T:
#     # 文字列tを逆順
#     temp = t[::-1]
#     # 末尾に"*"が続く限り、削除を続ける
#     while temp.endswith("*"):
#         temp = temp[:-1]
#     # 出力
#     print(temp)
