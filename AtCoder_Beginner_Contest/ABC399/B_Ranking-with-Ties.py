N = int(input())
P = list(map(int, input().split()))

# 競技者のスコアを降順にソート
sorted_scores = sorted(set(P), reverse=True)
# それぞれの順位
rankings = [-1] * N
# 現在の順位
r = 1

for score in sorted_scores:
    k = 0
    for i in range(N):
        if P[i] == score:
            rankings[i] = r
            k += 1
    r += k

for rank in rankings:
    print(rank)


# ========== 別解 ==========
N = int(input())
P = [int(i) for i in input().split()]

sorted_P = sorted(P, reverse=True)
for i in range(N):
    print(sorted_P.index(P[i]) + 1)
