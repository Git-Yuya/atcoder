S = list(input())
T = list(input())

# SとTの文字が違う箇所の数
diff_sum = sum(1 for i in range(len(S)) if S[i] != T[i])

if diff_sum == 0:
    print(0)

else:
    X = []

    for i in range(diff_sum):
        # 置き換え候補のインデックス
        candidate_idx = -1

        for j in range(len(S)):
            if S[j] != T[j]:
                candidate_idx = j
                if S[j] > T[j]:
                    break

        S[candidate_idx] = T[candidate_idx]
        X.append("".join(S))

    print(len(X))
    for x in X:
        print(x)
