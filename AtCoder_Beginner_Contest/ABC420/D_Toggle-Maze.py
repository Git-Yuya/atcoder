from collections import deque


def bfs(grid, height, width, start, goal):
    def check_cell(cell, parity):
        if cell == "#":
            return False
        if cell == "o":
            return parity == 0
        if cell == "x":
            return parity == 1
        return True

    start_x, start_y = start
    goal_x, goal_y = goal

    visited = [[[False] * 2 for _ in range(width)] for _ in range(height)]
    visited[start_x][start_y][0] = True
    q = deque()
    q.append((start_x, start_y, 0, 0))

    while q:
        x, y, parity, dist = q.popleft()

        if (x, y) == (goal_x, goal_y):
            return dist

        # 上下左右の4方向を探索
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < height and 0 <= next_y < width:
                c = grid[next_x][next_y]
                if check_cell(c, parity):
                    # "?"マスに入るとパリティを反転
                    next_parity = parity ^ 1 if c == "?" else parity

                    if not visited[next_x][next_y][next_parity]:
                        visited[next_x][next_y][next_parity] = True
                        q.append((next_x, next_y, next_parity, dist + 1))

    return -1


H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]

start = (-1, -1)
goal = (-1, -1)
for i in range(H):
    for j in range(W):
        if A[i][j] == "S":
            start = (i, j)
        elif A[i][j] == "G":
            goal = (i, j)

print(bfs(A, H, W, start, goal))


# ========== 別解 ==========
from collections import deque

H, W = map(int, input().split())
A = [input() for _ in range(H)]

start = (-1, -1)
goal = (-1, -1)
for i in range(H):
    for j in range(W):
        if A[i][j] == "S":
            start = (i, j)
        elif A[i][j] == "G":
            goal = (i, j)

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
start_x, start_y = start
goal_x, goal_y = goal

visited = [[[False] * W for _ in range(H)] for _ in range(2)]
visited[0][start_x][start_y] = True

q = deque()
q.append((0, start_x, start_y, 0))

while q:
    status, x, y, dist = q.popleft()

    if (x, y) == goal:
        print(dist)
        break

    for dx, dy in moves:
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < H and 0 <= next_y < W:
            if (
                A[next_x][next_y] in [".", "S", "G"] or
                (A[next_x][next_y] == "o" and status == 0) or
                (A[next_x][next_y] == "x" and status == 1)
            ) and not visited[status][next_x][next_y]:
                visited[status][next_x][next_y] = True
                q.append((status, next_x, next_y, dist + 1))

            # "?"マスに入ると状態が反転
            if A[next_x][next_y] == "?" and not visited[1 - status][next_x][next_y]:
                visited[1 - status][next_x][next_y] = True
                q.append((1 - status, next_x, next_y, dist + 1))

else:
    print(-1)
