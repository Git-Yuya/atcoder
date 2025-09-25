N, M = map(int, input().split())

# 各ユーザーIDの友達リスト
friends = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    friends[A - 1].append(B - 1)
    friends[B - 1].append(A - 1)

for i in range(N):
    # 友達の友達
    friend_friends = set()

    for f_id in friends[i]:
        if f_id != i:
            for ff_id in friends[f_id]:
                if ff_id != i and ff_id not in friends[i]:
                    friend_friends.add(ff_id)

    print(len(friend_friends))


# ========== 別解 ==========
N, M = map(int, input().split())

# 友達同士の距離
friends = [[100 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    A, B = A - 1, B - 1
    friends[A][B] = 1
    friends[B][A] = 1

for i in range(N):
    friends[i][i] = 0

# ワーシャルフロイド法
for k in range(N):
    for i in range(N):
        for j in range(N):
            friends[i][j] = min(friends[i][j], friends[i][k] + friends[k][j])

for n in range(N):
    print(friends[n].count(2))
