W, H = map(int, input().split())
N = int(input())
X_list, Y_list = [], []
for _ in range(N):
    X, Y = map(int, input().split())
    X_list.append(X)
    Y_list.append(Y)

# 長方形領域内での最大値
memo = {}

def solve(x1, y1, x2, y2):
    if x1 > x2 or y1 > y2:
        return 0

    state = (x1, y1, x2, y2)
    if state in memo:
        return memo[state]

    max_score = 0
    for i in range(N):
        x, y = X_list[i], Y_list[i]
        if not (x1 <= x <= x2 and y1 <= y <= y2):
            continue
        score = (x2 - x1 + 1) + (y2 - y1 + 1) - 1
        if x1 <= x - 1 and y1 <= y - 1:
            score += solve(x1, y1, x - 1, y - 1)
        if x1 <= x - 1 and y + 1 <= y2:
            score += solve(x1, y + 1, x - 1, y2)
        if x + 1 <= x2 and y1 <= y - 1:
            score += solve(x + 1, y1, x2, y - 1)
        if x + 1 <= x2 and y + 1 <= y2:
            score += solve(x + 1, y + 1, x2, y2)
        max_score = max(max_score, score)
    memo[state] = max_score

    return max_score

print(solve(1, 1, W, H))
