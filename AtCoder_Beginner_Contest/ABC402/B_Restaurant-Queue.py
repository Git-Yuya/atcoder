from collections import deque

Q = int(input())

# 行列に並ぶ人が持っているメニュー番号
menu = deque()

for _ in range(Q):
    query = list(map(int, input().split()))

    # 待ち行列に一人追加
    if query[0] == 1:
        X = query[1]
        menu.append(X)

    # 待ち行列の先頭を案内
    elif query[0] == 2:
        print(menu.popleft())


# ========== 別解 ==========
Q = int(input())
a = []

for _ in range(Q):
    queue = list(map(int, input().split()))
    operation = queue[0]

    if operation == 1:
        x = queue[1]
        a.append(x)

    else:
        print(a[0])
        a.pop(0)
