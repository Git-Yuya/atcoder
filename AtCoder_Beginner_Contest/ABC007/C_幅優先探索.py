from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = [input() for _ in range(R)]

q = deque()
q.append((sy - 1, sx - 1, 0))
visited = [[False] * C for _ in range(R)]
visited[sy - 1][sx - 1] = True
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while q:
    y, x, dist = q.popleft()

    if (y, x) == (gy - 1, gx - 1):
        print(dist)
        break

    for dy, dx in directions:
        next_y, next_x = y + dy, x + dx
        if 0 <= next_y < R and 0 <= next_x < C:
            if not visited[next_y][next_x] and c[next_y][next_x] == ".":
                visited[next_y][next_x] = True
                q.append((next_y, next_x, dist + 1))
