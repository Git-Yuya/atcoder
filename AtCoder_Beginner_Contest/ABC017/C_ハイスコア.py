N, M = map(int, input().split())

# すべての遺跡を探索した時の宝石の得点
scores = [0] * (M + 1)
# すべての遺跡を探索した時の得点
total_score = 0

# いもす法
for i in range(N):
    l, r, s = map(int, input().split())

    scores[l - 1] += s
    scores[r] -= s
    total_score += s

for i in range(1, M + 1):
    scores[i] += scores[i - 1]

print(total_score - min(scores[:-1]))
