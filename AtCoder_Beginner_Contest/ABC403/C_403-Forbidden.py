N, M, Q = map(int, input().split())

# N人の閲覧権限を管理
access_set = [set() for _ in range(N)]
all_access = [False] * N

for _ in range(Q):
    query = list(map(int, input().split()))

    # 特定の閲覧権限を付与
    if query[0] == 1:
        X, Y = query[1], query[2]
        access_set[X - 1].add(Y)

    # 全ての閲覧権限を付与
    elif query[0] == 2:
        X = query[1]
        all_access[X - 1] = True

    # 閲覧権限の確認
    elif query[0] == 3:
        X, Y = query[1], query[2]
        if all_access[X - 1] or Y in access_set[X - 1]:
            print("Yes")
        else:
            print("No")
