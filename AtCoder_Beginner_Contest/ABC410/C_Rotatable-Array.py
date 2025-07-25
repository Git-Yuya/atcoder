N, Q = map(int, input().split())
A = [x for x in range(1, N + 1)]

# 最初から何個ずれているか
offset = 0

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        p, x = query[1], query[2]
        A[(p - 1 + offset) % N] = x

    elif query[0] == 2:
        p = query[1]
        print(A[(p - 1 + offset) % N])

    elif query[0] == 3:
        k = query[1]
        offset += k
        offset %= N
