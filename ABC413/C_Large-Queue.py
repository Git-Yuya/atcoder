from collections import deque

Q = int(input())
A = deque()

for _ in range(Q):
    queue = list(map(int, input().split()))

    if queue[0] == 1:
        c, x = queue[1], queue[2]
        A.append((c, x))

    elif queue[0] == 2:
        k = queue[1]
        del_sum = 0

        while k > 0:
            c, x = A[0]

            # Aの要素(c, x)からまとめて取り出せる場合
            if c <= k:
                del_sum += c * x
                k -= c
                A.popleft()

            # Aの要素(c, x)から一部だけ取り出す場合
            else:
                A[0] = (c - k, x)
                del_sum += k * x
                k = 0

        print(del_sum)
