N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

min_AB = [min(a, b) for a, b in zip(A, B)]
sum_min_AB = sum(min_AB)

for _ in range(Q):
    c, X, V = input().split()
    X, V = int(X), int(V)

    if c == "A":
        old_min = min_AB[X - 1]
        A[X - 1] = V
        min_AB[X - 1] = min(A[X - 1], B[X - 1])
        sum_min_AB += min_AB[X - 1] - old_min

    elif c == "B":
        old_min = min_AB[X - 1]
        B[X - 1] = V
        min_AB[X - 1] = min(A[X - 1], B[X - 1])
        sum_min_AB += min_AB[X - 1] - old_min

    print(sum_min_AB)


# ========== 別解 ==========
N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

min_AB = [min(a, b) for a, b in zip(A, B)]
sum_min_AB = sum(min_AB)

for _ in range(Q):
    c, X, V = input().split()
    X, V = int(X) - 1, int(V)

    # 更新前の最小値を引く
    sum_min_AB -= min_AB[X]

    if c == "A":
        A[X] = V
    elif c == "B":
        B[X] = V
    min_AB[X] = min(A[X], B[X])

    # 更新後の最小値を足す
    sum_min_AB += min_AB[X]

    print(sum_min_AB)
