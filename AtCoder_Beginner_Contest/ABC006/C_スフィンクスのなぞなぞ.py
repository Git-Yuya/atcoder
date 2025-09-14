N, M = map(int, input().split())

# 大人の人数
adults = -1
# 老人の人数
seniors = -1
# 赤ちゃんの人数
babies = -1

if 2 * N <= M <= 4 * N:
    # 大人の人数をNと仮定
    adults = N
    M -= 2 * N

    # 赤ちゃんの人数
    babies = M // 2
    adults -= babies
    M -= babies * 2

    # 老人の人数
    seniors = M
    adults -= seniors

print(adults, seniors, babies)
