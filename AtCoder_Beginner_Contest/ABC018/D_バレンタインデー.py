from itertools import combinations

N, M, P, Q, R = map(int, input().split())
xyz = [list(map(int, input().split())) for _ in range(R)]

max_happiness = 0

# 女子の組み合わせを全探索
for comb in combinations(range(N), P):
    # 各男子を選んだ時の幸福度の合計
    happiness = [0] * M
    for x, y, z in xyz:
        if x - 1 in comb:
            happiness[y - 1] += z

    happiness.sort(reverse=True)
    max_happiness = max(max_happiness, sum(happiness[:Q]))

print(max_happiness)
