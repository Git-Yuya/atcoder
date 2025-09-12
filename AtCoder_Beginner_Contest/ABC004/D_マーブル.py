def f(first, num):
    """
    Args:
        first (int): 色の開始位置
        num (int): 色の個数
    """
    # 色の終了位置
    last = first + num - 1

    # 区間がすべて正の数である場合
    if first >= 0:
        total_cost = num * (first + last) // 2
    # 区間がすべて負の数である場合
    elif last <= 0:
        total_cost = - num * (first + last) // 2
    # 区間が負の数と正の数にまたがる場合
    else:
        total_cost = first * (first - 1) // 2 + (last + 1) * last // 2

    return total_cost


R, G, B = map(int, input().split())

# 操作回数の最小値
min_count = 10 ** 6

# iはGの開始位置
for i in range(-300, 301):
    # R, G, Bの各色の開始位置を決定し、f関数で操作回数を計算
    min_count = min(
        min_count,
        f(min(i - R, -100 - R // 2) + 100, R) + 
        f(i, G) + 
        f(max(i + G, 100 - B // 2) - 100, B)
    )

print(min_count)
