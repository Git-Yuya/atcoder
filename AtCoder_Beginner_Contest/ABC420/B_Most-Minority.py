N, M = map(int, input().split())
S = [input() for _ in range(N)]

# 各人の得点
scores = [0] * N

for i in range(M):
    count_0 = 0
    count_1 = 0
    for j in range(N):
        if S[j][i] == "0":
            count_0 += 1
        elif S[j][i] == "1":
            count_1 += 1
    for j in range(N):
        if S[j][i] == "0" and count_0 < count_1:
            scores[j] += 1
        elif S[j][i] == "1" and count_0 > count_1:
            scores[j] += 1

max_score = max(scores)
ans_list = []

for i in range(N):
    if scores[i] == max_score:
        ans_list.append(i + 1)

print(*ans_list)


# ========== 別解 ==========
N, M = map(int, input().split())
S = [input() for _ in range(N)]

# 各人の得点
scores = [0] * N

for vote_j in zip(*S):
    c = "0"
    if vote_j.count("0") > vote_j.count("1"):
        c = "1"

    for i in range(N):
        if vote_j[i] == c:
            scores[i] += 1

max_score = max(scores)
print(*[i + 1 for i in range(N) if scores[i] == max_score])
