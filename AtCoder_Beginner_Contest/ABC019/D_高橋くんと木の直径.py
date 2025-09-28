import sys

N = int(input())

u = 1
dist_max = 0
v_max = -1

# 頂点1を基準にして最も遠い頂点v_maxを探す
for v in range(2, N + 1):
    print("?", u, v)
    sys.stdout.flush()
    dist = int(input())

    if dist > dist_max:
        dist_max = dist
        v_max = v

# 頂点v_maxを基準にして最も遠い頂点までの距離を求める
for w in range(1, N + 1):
    if w == v_max:
        continue

    print("?", v_max, w)
    sys.stdout.flush()
    dist = int(input())

    dist_max = max(dist_max, dist)

print("!", dist_max)
