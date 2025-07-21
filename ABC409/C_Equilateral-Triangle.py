N, L = map(int, input().split())
d = list(map(int, input().split()))

# 点1から各点の位置
dot_pos = [0] * N
# 円周の各位置に存在する点の数
dot_count = [1] + [0] * (L - 1)

for i in range(1, N):
    dot_pos[i] = (dot_pos[i - 1] + d[i - 1]) % L
    dot_count[dot_pos[i]] += 1

if L % 3 == 0:
    triangle_count = 0
    # 正三角形であるための点間の距離
    triangle_dist = L // 3

    for i in range(triangle_dist):
        triangle_count += dot_count[i] * dot_count[i + triangle_dist] * dot_count[i + 2 * triangle_dist]
    print(triangle_count)

else:
    print(0)
