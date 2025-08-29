N, Q = map(int, input().split())

L = 0
R = 1
min_count = 0

for _ in range(Q):
    H, T = input().split()
    T = int(T) - 1

    # 右回りでいいかどうか
    is_right = True
    # 右回りの操作回数
    count = 0

    if H == "L":
        for i in range(N - 1):
            if (L + i) % N == R:
                is_right = False
            elif (L + i) % N == T:
                break

            count += 1

        if is_right:
            min_count += count
        else:
            min_count += N - count

        L = T

    elif H == "R":
        for i in range(N - 1):
            if (R + i) % N == L:
                is_right = False
            elif (R + i) % N == T:
                break

            count += 1

        if is_right:
            min_count += count
        else:
            min_count += N - count

        R = T

print(min_count)


# ========== 別解 ==========
N, Q = map(int, input().split())

L = 0
R = 1
count = 0

for _ in range(Q):
    H, T = input().split()
    T = int(T) - 1

    if H == "L":
        if L < R:
            L += N
        if T < R:
            T += N

        count += abs(T - L)
        L = T % N

    else:
        if R < L:
            R += N
        if T < L:
            T += N

        count += abs(T - R)
        R = T % N

print(count)
