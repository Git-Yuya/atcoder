N = int(input())
S = list(input() for _ in range(N))

# 連結した文字列のリスト
T = []

for i in range(N):
    for j in range(N):
        if i == j:
            continue

        # 文字列S[i]とS[j]を連結
        T.append(S[i] + S[j])

print(len(set(T)))
