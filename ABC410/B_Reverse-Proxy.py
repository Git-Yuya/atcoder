N, Q = map(int, input().split())
X = list(map(int, input().split()))

# N個の箱
boxes = [0] * N
# ボールをどの箱に入れたか
balls = []

for x in X:
    if x >= 1:
        boxes[x - 1] += 1
        balls.append(x)

    elif x == 0:
        min_box = min(boxes)
        for j in range(N):
            if boxes[j] == min_box:
                boxes[j] += 1
                balls.append(j + 1)
                break

print(*balls)
