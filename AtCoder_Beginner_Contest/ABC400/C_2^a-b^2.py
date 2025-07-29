import math

N = int(input())

# 良い整数の個数
good_count = 0

for a in range(1, 60):
    # 平方根の上限
    b_max = math.isqrt(N // (2 ** a))
    # aはすべての2の因数を含むと仮定しているのでbは奇数
    good_count += (b_max + 1) // 2

print(good_count)


# ========== 別解 ==========
import math

N = int(input())

# 良い整数の個数
good_count = 0

# aを1と2のみに制限
for a in range(1, 3):
    good_count += math.isqrt(N // (2 ** a))

print(good_count)


# ========== 別解 ==========
def search(n: int) -> int:
    """
    指定された数値nに対して、平方根の整数部分を二分探索

    Args:
        n (int): 平方根を求めたい正の整数

    Returns:
        right (int): nの平方根の整数部分 (floor(sqrt(n)))
    """
    left = 1
    right = n

    while right - left > 0:
        mid = (left + right + 1) // 2
        if mid ** 2 > n:
            right = mid - 1
        else:
            left = mid

    return right


N = int(input())

ans = 0
for a in range(1, 60):
    if 2 ** a > N:
        break
    n = N // (2 ** a)
    ans += (search(n) + 1) // 2

print(ans)
