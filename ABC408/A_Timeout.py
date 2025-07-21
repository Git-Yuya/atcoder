N, S = map(int, input().split())
T = list(map(int, input().split()))

# 起きているかどうか
is_awake = True
# 1つ前の肩たたき時間
prev = 0

for t in T:
    if t - prev >= S + 0.5:
        is_awake = False
        break
    prev = t

print("Yes" if is_awake else "No")
