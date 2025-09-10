N, M = map(int, input().split())

# 各議員の知り合いの議員
factions = [[] for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1

    factions[x].append(y)
    factions[y].append(x)

# 派閥の最大人数
max_faction = 0

# 知り合い同士の派閥
for i in range(1 << N):
    # 派閥に所属する議員
    faction = []
    for j in range(N):
        if (i >> j) & 1:
            faction.append(j)

    # 派閥を構成できるか
    is_faction = True
    for j in faction:
        for k in faction:
            if j == k:
                continue
            if k not in factions[j]:
                is_faction = False
                break
        if not is_faction:
            break

    if is_faction:
        max_faction = max(max_faction, len(faction))

print(max_faction)
