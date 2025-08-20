from collections import defaultdict
from itertools import combinations

a, b, c, d, e = map(int, input().split())

# 各人の点数
scores = defaultdict(int)

for i in range(1, 6):
    for person, score in zip(combinations(["A", "B", "C", "D", "E"], i), combinations([a, b, c, d, e], i)):
        scores["".join(person)] += sum(score)
scores = sorted(scores.items(), key=lambda x: (-x[1], x[0]))

for person, score in scores:
    print(person)


# ========== 別解 ==========
score_list = list(map(int, input().split()))

ans = []
for bit in range(1, 32):
    score = 0
    name = ""
    for i in range(5):
        if bit & (1 << i):
            score += score_list[i]
            if i == 0:
                name += "A"
            elif i == 1:
                name += "B"
            elif i == 2:
                name += "C"
            elif i == 3:
                name += "D"
            else:
                name += "E"
    ans.append([score, name])

ans.sort(key=lambda ans: ans[1])
ans.sort(key=lambda ans: ans[0], reverse=True)

for score, name in ans:
    print(name)
