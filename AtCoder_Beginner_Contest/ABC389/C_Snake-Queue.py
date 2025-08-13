from collections import deque

Q = int(input())

# 蛇の長さを管理する待ち行列
snake = deque()
# 蛇の長さの累積和
prefix = [0]
# 列から抜けた蛇の数
removed = 0
# 列から抜けた蛇の長さの総和
removed_length = 0

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        l = query[1]
        snake.append(l)
        prefix.append(prefix[-1] + l)

    elif query[0] == 2:
        removed += 1
        removed_length += snake.popleft()

    elif query[0] == 3:
        k = query[1]
        pos = prefix[k - 1 + removed] - removed_length
        print(pos)


# ========== 別解 ==========
Q = int(input())

# 蛇の長さの累積和
prefix = [0]
# 現在の先頭インデックス
top = 0

for i in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        l = query[1]
        prefix.append(prefix[-1] + l)

    elif query[0] == 2:
        top += 1

    elif query[0] == 3:
        k = query[1]
        pos = prefix[k - 1 + top] - prefix[top]
        print(pos)
